
from pathlib import Path

from src.maze import Maze


def load_movingai_map(map_file):
    """
    Load a Moving AI benchmark map and convert it
    into the numerical grid format used by our Maze class.
    """

    map_file = Path(map_file)

    with open(map_file, "r", encoding="utf-8") as file:
        lines = [line.rstrip("\r\n") for line in file]

    # Read map dimensions from the header
    height = int(next(line.split()[1] for line in lines if line.startswith("height ")))
    width = int(next(line.split()[1] for line in lines if line.startswith("width ")))

    # Find the beginning of the actual map
    map_start = lines.index("map") + 1
    map_rows = lines[map_start:map_start + height]

    if len(map_rows) != height:
        raise ValueError("Map does not contain the expected number of rows.")

    if any(len(row) != width for row in map_rows):
        raise ValueError("One or more map rows have an incorrect width.")

    # Convert map symbols into the project's grid format
    grid = []

    for row in map_rows:
        converted_row = []

        for cell in row:
            if cell in (".", "G", "S"):
                converted_row.append(0)  # Free cell
            elif cell in ("@", "O", "T", "W"):
                converted_row.append(1)  # Blocked cell
            else:
                raise ValueError(f"Unknown map symbol: {cell}")

        grid.append(converted_row)

    return grid


def load_scenarios(scenario_file):
    """
    Read start and goal positions from a Moving AI scenario file.
    """

    scenarios = []

    with open(scenario_file, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("version"):
                continue

            columns = line.split()

            if len(columns) < 9:
                raise ValueError(f"Invalid scenario row: {line}")

            scenario = {
                "bucket": int(columns[0]),
                "map_name": columns[1],
                "width": int(columns[2]),
                "height": int(columns[3]),
                "start": (int(columns[5]), int(columns[4])),
                "goal": (int(columns[7]), int(columns[6])),
                "optimal_length": float(columns[8]),
            }

            scenarios.append(scenario)

    return scenarios


def load_movingai_scenario(map_file, scenario_file, scenario_index=0):
    """
    Create a Maze object using an external map and one scenario.
    """

    grid = load_movingai_map(map_file)
    scenarios = load_scenarios(scenario_file)

    if not 0 <= scenario_index < len(scenarios):
        raise IndexError("Scenario index is outside the available range.")

    scenario = scenarios[scenario_index]

    if scenario["width"] != len(grid[0]) or scenario["height"] != len(grid):
        raise ValueError("Scenario dimensions do not match the map.")

    start = scenario["start"]
    goal = scenario["goal"]

    maze = Maze(grid, start=start, goal=goal)

    if not maze.is_valid(start):
        raise ValueError(f"Start position is blocked or invalid: {start}")

    if not maze.is_valid(goal):
        raise ValueError(f"Goal position is blocked or invalid: {goal}")

    return maze, scenario

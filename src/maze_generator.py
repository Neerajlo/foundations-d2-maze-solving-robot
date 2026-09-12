import random

from maze import Maze


def generate_maze(rows, cols, seed=None):

    if rows <= 0 or cols <= 0:
        raise ValueError("Rows and columns must both be positive.")

    random_generator = random.Random(seed)

    # Every cell initially has four walls.
    walls = {}

    for row in range(rows):
        for col in range(cols):
            walls[(row, col)] = {
                "UP": True,
                "RIGHT": True,
                "DOWN": True,
                "LEFT": True
            }

    # Keep track of visited cells.
    visited = set()

    # Opposite walls.
    opposite = {
        "UP": "DOWN",
        "RIGHT": "LEFT",
        "DOWN": "UP",
        "LEFT": "RIGHT"
    }

    directions = {
        "UP": (-1, 0),
        "RIGHT": (0, 1),
        "DOWN": (1, 0),
        "LEFT": (0, -1)
    }

    def carve_passage(current):
        """Recursively carve passages through the maze."""

        visited.add(current)

        direction_list = list(directions.keys())
        random_generator.shuffle(direction_list)

        row, col = current

        for direction in direction_list:

            dr, dc = directions[direction]
            neighbor = (row + dr, col + dc)

            # Skip if neighbor is outside the maze.
            if not (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols):
                continue

            # Skip if already visited.
            if neighbor in visited:
                continue

            # Remove wall between current cell and neighbor.
            walls[current][direction] = False
            walls[neighbor][opposite[direction]] = False

            # Continue from the neighbor.
            carve_passage(neighbor)

    # Start maze generation from top-left cell.
    carve_passage((0, 0))

    start = (0, 0)
    goal = (rows - 1, cols - 1)

    return Maze(
        rows=rows,
        cols=cols,
        start=start,
        goal=goal,
        walls=walls
    )
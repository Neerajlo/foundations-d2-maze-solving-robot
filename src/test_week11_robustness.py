import random
from collections import deque

from src.maze import Maze
from src.solver import reactive_astar
from src.reactive_astar_experiment import reactive_astar_with_visit_penalty


def check_connectivity(grid, start, goal):
    """Check whether the goal is reachable with full maze knowledge."""
    rows = len(grid)
    cols = len(grid[0])

    queue = deque([start])
    visited = {start}

    while queue:
        row, col = queue.popleft()

        if (row, col) == goal:
            return True, len(visited)

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc

            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and grid[nr][nc] == 0
                and (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                queue.append((nr, nc))

    return False, len(visited)


def run_algorithm_tests(grid, start, goal):
    """Run both Reactive A* implementations on separate maze objects."""
    original = reactive_astar(
        Maze(grid, start=start, goal=goal)
    )

    enhanced = reactive_astar_with_visit_penalty(
        Maze(grid, start=start, goal=goal),
        visit_penalty=0.5
    )

    return original, enhanced


def test_random_obstacles():
    print("\n" + "=" * 55)
    print("RANDOM OBSTACLE STRESS TEST")
    print("=" * 55)

    start = (0, 0)
    goal = (19, 19)

    for density in [0.10, 0.25, 0.35, 0.40]:
        random.seed(42)

        grid = [
            [
                1 if random.random() < density else 0
                for _ in range(20)
            ]
            for _ in range(20)
        ]

        grid[0][0] = 0
        grid[19][19] = 0

        obstacles = sum(row.count(1) for row in grid)

        reachable, cells = check_connectivity(
            grid, start, goal
        )

        original, enhanced = run_algorithm_tests(
            grid, start, goal
        )

        print(f"\nObstacle density: {density * 100:.0f}%")
        print("Obstacles:", obstacles)
        print("Goal reachable with full information:", reachable)
        print("Reachable cells:", cells)

        print(
            "Original:",
            original["success"],
            "Distance:", original["actual_distance"],
            "Nodes:", original["nodes_expanded"]
        )

        print(
            "Enhanced:",
            enhanced["success"],
            "Distance:", enhanced["actual_distance"],
            "Nodes:", enhanced["nodes_expanded"]
        )


def test_narrow_corridor():
    print("\n" + "=" * 55)
    print("NARROW CORRIDOR TEST")
    print("=" * 55)

    grid = [[1] * 7 for _ in range(7)]

    path = (
        [(r, 0) for r in range(7)]
        + [(6, c) for c in range(1, 7)]
        + [(r, 6) for r in range(5, -1, -1)]
    )

    for row, col in path:
        grid[row][col] = 0

    original, enhanced = run_algorithm_tests(
        grid, (0, 0), (0, 6)
    )

    print("Original:", original)
    print("Enhanced:", enhanced)


def test_edge_cases():
    print("\n" + "=" * 55)
    print("EDGE CASE TESTING")
    print("=" * 55)

    # Start equals goal
    print("\nStart equals goal:")

    original, enhanced = run_algorithm_tests(
        [[0]], (0, 0), (0, 0)
    )

    print("Original:", original["success"])
    print("Enhanced:", enhanced["success"])

    # Unreachable goal
    print("\nUnreachable goal:")

    grid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]

    original, enhanced = run_algorithm_tests(
        grid, (0, 0), (0, 2)
    )

    print("Original:", original["success"])
    print("Enhanced:", enhanced["success"])

    # Invalid starting position
    print("\nOut-of-bounds starting position:")

    grid = [
        [0, 0],
        [0, 0]
    ]

    original, enhanced = run_algorithm_tests(
        grid, (-1, 0), (1, 1)
    )

    print("Original:", original["success"])
    print("Enhanced:", enhanced["success"])


def test_malformed_inputs():
    print("\n" + "=" * 55)
    print("MALFORMED INPUT TESTING")
    print("=" * 55)

    test_grids = {
        "Empty grid": [],
        "Empty row": [[]],
        "Unequal row lengths": [[0, 0], [0]],
        "Invalid cell value": [[0, 2], [0, 0]],
        "Negative cell value": [[0, -1], [0, 0]],
        "Floating-point cell": [[0, 0.5], [0, 0]],
        "Boolean cells": [[False, True], [False, False]]
    }

    for name, grid in test_grids.items():
        print(f"\n{name}:")

        try:
            maze = Maze(grid)

            print("Constructor: Accepted")

            try:
                print(
                    "Start cell valid:",
                    maze.is_valid((0, 0))
                )
            except Exception as error:
                print(
                    "Validation error:",
                    type(error).__name__,
                    str(error)
                )

        except Exception as error:
            print(
                "Constructor error:",
                type(error).__name__,
                str(error)
            )


def main():
    print("=" * 55)
    print("WEEK 11 ROBUSTNESS TESTING")
    print("=" * 55)

    test_edge_cases()
    test_malformed_inputs()
    test_irregular_grid_access()
    test_random_obstacles()
    test_narrow_corridor()

    print("\n" + "=" * 55)
    print("WEEK 11 TESTING COMPLETED")
    print("=" * 55)

def test_irregular_grid_access():
    print("\n" + "=" * 55)
    print("IRREGULAR GRID ACCESS TEST")
    print("=" * 55)

    grid = [[0, 0], [0]]

    try:
        maze = Maze(grid, start=(0, 0), goal=(1, 0))
        print("Constructor: Accepted irregular grid")

        print("Testing missing cell (1,1):")
        print(maze.is_valid((1, 1)))

    except Exception as error:
        print("Expected failure detected:")
        print(type(error).__name__, error)
if __name__ == "__main__":
    main()
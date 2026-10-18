import random
import json
from pathlib import Path


SEEDS = [42, 43, 44]


def generate_maze(rows, cols, seed):
    random.seed(seed)

    # Start with all open cells
    maze = [[0 for _ in range(cols)] for _ in range(rows)]

    # Create a guaranteed path from start to goal
    path = [(0, 0)]
    r, c = 0, 0

    while r < rows - 1 or c < cols - 1:
        if r == rows - 1:
            c += 1
        elif c == cols - 1:
            r += 1
        elif random.random() < 0.5:
            r += 1
        else:
            c += 1

        path.append((r, c))

    path_cells = set(path)

    # Add random walls without blocking the guaranteed path
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in path_cells:
                if random.random() < 0.25:
                    maze[r][c] = 1

    # Keep start and goal open
    maze[0][0] = 0
    maze[rows - 1][cols - 1] = 0

    return maze


def save_maze(maze, maze_id):
    output_dir = Path("data/raw")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"{maze_id}.json"

    with open(output_file, "w") as f:
        json.dump(maze, f)

    print(f"Saved: {output_file}")


if __name__ == "__main__":
    sizes = {
        "small": (10, 10),
        "medium": (20, 20),
        "large": (30, 30),
    }

    for size_name, (rows, cols) in sizes.items():
        for seed in SEEDS:
            maze_id = f"{size_name}_{seed}"
            maze = generate_maze(rows, cols, seed)
            save_maze(maze, maze_id)
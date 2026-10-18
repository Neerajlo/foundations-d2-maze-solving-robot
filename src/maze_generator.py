import json
import random
from pathlib import Path


def generate_maze(rows, cols, seed=42):
    random.seed(seed)

    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    # Keep a guaranteed path from start to goal.
    r, c = 0, 0
    path = {(r, c)}

    while r < rows - 1 or c < cols - 1:
        if r == rows - 1:
            c += 1
        elif c == cols - 1:
            r += 1
        elif random.random() < 0.5:
            r += 1
        else:
            c += 1
        path.add((r, c))

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in path and random.random() < 0.25:
                grid[r][c] = 1

    return grid


def main():
    output_dir = Path("data/raw")
    output_dir.mkdir(parents=True, exist_ok=True)

    sizes = {
        "small": (10, 10),
        "medium": (20, 20),
        "large": (30, 30),
    }

    for name, (rows, cols) in sizes.items():
        for seed in (42, 43, 44):
            grid = generate_maze(rows, cols, seed)
            output = output_dir / f"{name}_{seed}.json"

            with open(output, "w", encoding="utf-8") as file:
                json.dump(grid, file)

            print(f"Generated {output}")


if __name__ == "__main__":
    main()
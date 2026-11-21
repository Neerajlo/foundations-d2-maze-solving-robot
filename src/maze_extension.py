import json
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = ROOT / "data" / "raw"
OUTPUT_DIR = ROOT / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "maze_metadata.csv"

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    results = []

    for path in sorted(INPUT_DIR.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            grid = data.get("grid", data.get("maze", data)) if isinstance(data, dict) else data

            rows = len(grid)
            cols = len(grid[0])
            if not rows or any(len(row) != cols for row in grid):
                raise ValueError("Invalid grid")

            obstacles = sum(cell == 1 for row in grid for cell in row)
            total = rows * cols
            density = obstacles / total * 100

            difficulty = "Easy" if density < 20 else "Medium" if density < 35 else "Hard"

            results.append({
                "maze_id": path.stem,
                "rows": rows,
                "columns": cols,
                "total_cells": total,
                "obstacles": obstacles,
                "free_cells": total - obstacles,
                "obstacle_density_percent": round(density, 2),
                "difficulty": difficulty
            })
            print("Analyzed:", path.name)

        except (ValueError, TypeError, KeyError, IndexError) as error:
            print("Skipped:", path.name, error)

    if results:
        with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)

        print("\nWEEK 10 EXTENSION COMPLETED")
        print("Mazes analyzed:", len(results))
        print("Saved:", OUTPUT_FILE)
    else:
        print("No valid maze files found.")

if __name__ == "__main__":
    main()

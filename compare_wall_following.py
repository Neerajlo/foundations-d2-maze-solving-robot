import csv
import json
from pathlib import Path

from src.maze import Maze
from src.bfs import bfs
from src.robot import wall_following

RAW_DIR = Path("data/raw")
RESULT_DIR = Path("results")
RESULT_DIR.mkdir(parents=True, exist_ok=True)

output_file = RESULT_DIR / "wall_following_comparison.csv"

fields = [
    "maze_id",
    "algorithm",
    "success",
    "path_length",
    "nodes_expanded",
    "path"
]

records = []

for file in sorted(RAW_DIR.glob("*.json")):
    maze = Maze.from_json(file)

    for name, algorithm in [
        ("BFS", bfs),
        ("Wall Following", wall_following)
    ]:
        result = algorithm(maze)

        record = {
            "maze_id": file.stem,
            "algorithm": name,
            "success": result["success"],
            "path_length": result["path_length"],
            "nodes_expanded": result["nodes_expanded"],
            "path": json.dumps(result["path"])
        }

        records.append(record)

        print(
            f"{file.stem} | {name} | "
            f"Success: {result['success']} | "
            f"Path: {result['path_length']} | "
            f"Nodes: {result['nodes_expanded']}"
        )

with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(records)

print(f"\nCSV saved successfully: {output_file}")
print(f"Total records: {len(records)}")
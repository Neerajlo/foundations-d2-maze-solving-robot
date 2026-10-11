import json
import time
import csv
from pathlib import Path

from src.maze import Maze
from src.solver import bfs, dfs, astar


RAW_DIR = Path("data/raw")
RESULT_DIR = Path("results")
RESULT_DIR.mkdir(exist_ok=True)

experiments = []

for maze_file in sorted(RAW_DIR.glob("*.json")):

    with open(maze_file, "r") as f:
        data = json.load(f)

    maze = Maze(data)

    for algorithm_name, algorithm in [
        ("BFS", bfs),
        ("DFS", dfs),
        ("A*", astar),
    ]:

        start_time = time.perf_counter()

        path, nodes_expanded = algorithm(maze)

        runtime = time.perf_counter() - start_time

        experiments.append({
            "maze": maze_file.stem,
            "algorithm": algorithm_name,
            "path_length": len(path),
            "nodes_expanded": nodes_expanded,
            "runtime_seconds": runtime,
            "path_found": bool(path),
        })

output_file = RESULT_DIR / "maze_results.csv"

with open(output_file, "w", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=experiments[0].keys()
    )
    writer.writeheader()
    writer.writerows(experiments)

print(f"Saved: {output_file}")
print(f"Total experiments: {len(experiments)}")
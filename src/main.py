import csv
import time
import tracemalloc
from pathlib import Path

from src.maze import Maze
from src.bfs import bfs
from src.solver import dfs, astar


RAW_DIR = Path("data/raw")
RESULT_DIR = Path("results")
RESULT_DIR.mkdir(parents=True, exist_ok=True)


def main():
    if not RAW_DIR.exists() or not list(RAW_DIR.glob("*.json")):
        print("No mazes found. Generate them first.")
        return

    results = []

    algorithms = [
        ("BFS", bfs),
        ("DFS", dfs),
        ("A*", astar),
    ]

    for maze_file in sorted(RAW_DIR.glob("*.json")):
        maze = Maze.from_json(maze_file)
        print(f"\nMaze: {maze_file.stem}")

       
        for name, algorithm in algorithms:
            tracemalloc.start()
            start_time = time.perf_counter()
            outcome = algorithm(maze)
            elapsed = time.perf_counter() - start_time
            current_memory, peak_memory = tracemalloc.get_traced_memory()
            tracemalloc.stop()


            result = {
                "maze_id": maze_file.stem,
                "algorithm": name,
                "path_length": outcome["path_length"],
                "nodes_expanded": outcome["nodes_expanded"],
                "runtime_seconds": round(elapsed, 8),
                "peak_memory_kb": round(peak_memory / 1024, 2),  
                "replan_count": 0,
                "path_found": outcome["success"],
            }
            results.append(result)

            print(
                f"{name}: found={result['path_found']}, "
                f"path_length={result['path_length']}, "
                f"nodes_expanded={result['nodes_expanded']}, "
                f"time={elapsed:.6f}s"
            )

    output_file = RESULT_DIR / "maze_results.csv"
    fields = [
    "maze_id",
    "algorithm",
    "path_length",
    "nodes_expanded",
    "runtime_seconds",
    "peak_memory_kb",
    "replan_count",
    "path_found",
]

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(results)

    print(f"\nResults saved to: {output_file}")
    print(f"Total result records: {len(results)}")


if __name__ == "__main__":
    main()
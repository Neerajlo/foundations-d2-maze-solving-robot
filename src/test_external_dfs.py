
import time
import tracemalloc

from src.solver import dfs
from src.external_dataset_loader import load_movingai_scenario


MAP_FILE = "datasets/maze512-1-0.map"
SCENARIO_FILE = "datasets/maze512-1-0.map.scen"
SCENARIO_INDEX = 12113


def main():
    print(" EXTERNAL DATASET DFS TEST")
    print("----------------------------------")

    # Load the same external scenario used for BFS
    maze, scenario = load_movingai_scenario(
        MAP_FILE,
        SCENARIO_FILE,
        SCENARIO_INDEX
    )

    print("Dataset: Moving AI benchmark")
    print("Maze dimensions:", maze.rows, "x", maze.cols)
    print("Start:", maze.start)
    print("Goal:", maze.goal)
    print("Reference optimal length:", scenario["optimal_length"])

    # Measure DFS execution time and peak memory
    tracemalloc.start()
    start_time = time.perf_counter()

    result = dfs(maze)

    runtime = time.perf_counter() - start_time
    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("\nDFS RESULTS")
    print("Success:", result["success"])
    print("Path length:", result["path_length"])
    print("Nodes expanded:", result["nodes_expanded"])
    print("Runtime (seconds):", round(runtime, 6))
    print("Peak memory (KB):", round(peak_memory / 1024, 2))

    print(
        "Path matches reference length:",
        result["path_length"] == scenario["optimal_length"]
    )


if __name__ == "__main__":
    main()

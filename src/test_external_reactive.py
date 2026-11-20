import time
import tracemalloc

from src.solver import reactive_astar
from src.external_dataset_loader import load_movingai_scenario


MAP_FILE = "datasets/maze512-1-0.map"
SCENARIO_FILE = "datasets/maze512-1-0.map.scen"
SCENARIO_INDEX = 100

def main():
    print(" EXTERNAL DATASET REACTIVE A* TEST")
    print("--------------------------------------")

    # Load the external benchmark maze
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

    # Measure Reactive A* execution time and peak memory
    tracemalloc.start()
    start_time = time.perf_counter()

    result = reactive_astar(maze)

    runtime = time.perf_counter() - start_time
    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("\nREACTIVE A* RESULTS")
    print("Success:", result["success"])
    print("Actual distance:", result["actual_distance"])
    print("Nodes expanded:", result["nodes_expanded"])
    print("Runtime (seconds):", round(runtime, 6))
    print("Peak memory (KB):", round(peak_memory / 1024, 2))
    print("Replan count:", result["replan_count"])
    print("Obstacles discovered:", result["obstacles_discovered"])
    print("Final position:", result["final_position"])


if __name__ == "__main__":
    main()

import csv
import time
import tracemalloc

from src.bfs import bfs
from src.solver import dfs
from src.dstar_lite import DStarLite
from src.external_dataset_loader import load_movingai_scenario


MAP_FILE = "datasets/maze512-1-0.map"
SCENARIO_FILE = "datasets/maze512-1-0.map.scen"

SCENARIO_INDICES = [12113, 12119, 12112]


def measure_algorithm(algorithm_name, maze):
    tracemalloc.start()
    start_time = time.perf_counter()

    if algorithm_name == "BFS":
        result = bfs(maze)
    elif algorithm_name == "DFS":
        result = dfs(maze)
    elif algorithm_name == "D* Lite":
        planner = DStarLite(maze)
        result = planner.plan()
    else:
        raise ValueError("Unknown algorithm")

    runtime = time.perf_counter() - start_time
    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "success": result["success"],
        "path_length": result["path_length"],
        "nodes_expanded": result["nodes_expanded"],
        "runtime": round(runtime, 6),
        "peak_memory_kb": round(peak_memory / 1024, 2),
    }


def main():
    print("WEEK 9 - MULTIPLE EXTERNAL SCENARIO TEST")
    print("----------------------------------------")

    all_results = []

    for scenario_index in SCENARIO_INDICES:
        maze, scenario = load_movingai_scenario(
            MAP_FILE,
            SCENARIO_FILE,
            scenario_index
        )

        print("\nScenario:", scenario_index)
        print("Start:", maze.start)
        print("Goal:", maze.goal)
        print("Reference optimal length:", scenario["optimal_length"])

        for algorithm in ["BFS", "DFS", "D* Lite"]:
            result = measure_algorithm(algorithm, maze)

            matches = (
                result["path_length"] == scenario["optimal_length"]
            )

            print("\nAlgorithm:", algorithm)
            print("Success:", result["success"])
            print("Path length:", result["path_length"])
            print("Nodes expanded:", result["nodes_expanded"])
            print("Runtime:", result["runtime"], "seconds")
            print("Peak memory:", result["peak_memory_kb"], "KB")
            print("Matches reference:", matches)

            all_results.append({
                "scenario": scenario_index,
                "algorithm": algorithm,
                "start": maze.start,
                "goal": maze.goal,
                "reference_length": scenario["optimal_length"],
                "success": result["success"],
                "path_length": result["path_length"],
                "nodes_expanded": result["nodes_expanded"],
                "runtime_seconds": result["runtime"],
                "peak_memory_kb": result["peak_memory_kb"],
                "matches_reference": matches,
            })

    output_file = "results/external_dataset_comparison.csv"

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=all_results[0].keys()
        )
        writer.writeheader()
        writer.writerows(all_results)

    print("\n----------------------------------------")
    print("MULTIPLE SCENARIO TEST COMPLETED")
    print("Results saved to:", output_file)


if __name__ == "__main__":
    main()

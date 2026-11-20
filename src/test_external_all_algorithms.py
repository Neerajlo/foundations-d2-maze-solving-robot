import csv
import time
import tracemalloc
from pathlib import Path

from src.bfs import bfs
from src.solver import dfs, astar, reactive_astar
from src.dstar_lite import DStarLite
from src.external_dataset_loader import load_movingai_scenario


# External Moving AI benchmark files
MAP_FILE = "datasets/maze512-1-0.map"
SCENARIO_FILE = "datasets/maze512-1-0.map.scen"

# Fully informed algorithm scenarios
FULL_OBSERVATION_SCENARIOS = [12113, 12119, 12112]

# Partial-observation Reactive A* scenarios
REACTIVE_SCENARIOS = [100, 101, 102]

# Output file
OUTPUT_FILE = Path("results/week9_external_all_algorithms.csv")
def measure_algorithm(algorithm_name, maze):
    """Measure execution time, memory and performance."""

    tracemalloc.start()
    start_time = time.perf_counter()

    if algorithm_name == "BFS":
        result = bfs(maze)

    elif algorithm_name == "DFS":
        result = dfs(maze)

    elif algorithm_name == "A*":
        result = astar(maze)

    elif algorithm_name == "D* Lite":
        planner = DStarLite(maze)
        result = planner.plan()

    elif algorithm_name == "Reactive A*":
        result = reactive_astar(maze)

    else:
        raise ValueError(f"Unknown algorithm: {algorithm_name}")

    runtime = time.perf_counter() - start_time

    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "success": result["success"],
        "path_length": result["path_length"],
        "nodes_expanded": result["nodes_expanded"],
        "runtime_seconds": round(runtime, 6),
        "peak_memory_kb": round(peak_memory / 1024, 2),
        "replan_count": result.get("replan_count", 0),
        "obstacles_discovered": result.get("obstacles_discovered", 0),
    }
def run_experiments():
    """Run external benchmark experiments for all five algorithms."""

    all_results = []

    # Group A: Algorithms with full maze knowledge
    full_algorithms = ["BFS", "DFS", "A*", "D* Lite"]

    print("\nWEEK 9 - EXTERNAL DATASET BENCHMARK")
    print("========================================")

    for scenario_index in FULL_OBSERVATION_SCENARIOS:

        maze, scenario = load_movingai_scenario(
            MAP_FILE,
            SCENARIO_FILE,
            scenario_index
        )

        print(f"\nFULL OBSERVATION - Scenario {scenario_index}")
        print("Reference optimal length:", scenario["optimal_length"])

        for algorithm in full_algorithms:

            result = measure_algorithm(algorithm, maze)

            matches = (
                result["path_length"] == scenario["optimal_length"]
            )

            print(f"\nAlgorithm: {algorithm}")
            print("Success:", result["success"])
            print("Path length:", result["path_length"])
            print("Nodes expanded:", result["nodes_expanded"])
            print("Runtime:", result["runtime_seconds"], "seconds")
            print("Peak memory:", result["peak_memory_kb"], "KB")
            print("Matches reference:", matches)

            all_results.append({
                "scenario": scenario_index,
                "observation_model": "Full observation",
                "algorithm": algorithm,
                "reference_length": scenario["optimal_length"],
                "success": result["success"],
                "path_length": result["path_length"],
                "nodes_expanded": result["nodes_expanded"],
                "runtime_seconds": result["runtime_seconds"],
                "peak_memory_kb": result["peak_memory_kb"],
                "replan_count": result["replan_count"],
                "obstacles_discovered": result["obstacles_discovered"],
                "matches_reference": matches,
            })

    # Group B: Reactive A* with partial observation
    for scenario_index in REACTIVE_SCENARIOS:

        maze, scenario = load_movingai_scenario(
            MAP_FILE,
            SCENARIO_FILE,
            scenario_index
        )

        print(f"\nPARTIAL OBSERVATION - Scenario {scenario_index}")
        print("Reference optimal length:", scenario["optimal_length"])

        result = measure_algorithm("Reactive A*", maze)

        print("\nAlgorithm: Reactive A*")
        print("Success:", result["success"])
        print("Actual distance:", result["path_length"])
        print("Nodes expanded:", result["nodes_expanded"])
        print("Runtime:", result["runtime_seconds"], "seconds")
        print("Peak memory:", result["peak_memory_kb"], "KB")
        print("Replans:", result["replan_count"])
        print("Obstacles discovered:", result["obstacles_discovered"])

        all_results.append({
            "scenario": scenario_index,
            "observation_model": "Partial observation",
            "algorithm": "Reactive A*",
            "reference_length": scenario["optimal_length"],
            "success": result["success"],
            "path_length": result["path_length"],
            "nodes_expanded": result["nodes_expanded"],
            "runtime_seconds": result["runtime_seconds"],
            "peak_memory_kb": result["peak_memory_kb"],
            "replan_count": result["replan_count"],
            "obstacles_discovered": result["obstacles_discovered"],
            "matches_reference": "Not directly comparable",
        })

    return all_results
def main():
    all_results = run_experiments()

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "scenario",
            "observation_model",
            "algorithm",
            "reference_length",
            "success",
            "path_length",
            "nodes_expanded",
            "runtime_seconds",
            "peak_memory_kb",
            "replan_count",
            "obstacles_discovered",
            "matches_reference",
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_results)

    print("\n========================================")
    print("WEEK 9 EXTERNAL BENCHMARK COMPLETED")
    print("Total experiments:", len(all_results))
    print("Results saved to:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
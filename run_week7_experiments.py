
import csv
import io
import random
import statistics
import time
import tracemalloc
from contextlib import redirect_stdout
from pathlib import Path

from src.maze import Maze
from src.maze_generator import generate_maze
from src.bfs import bfs
from src.solver import dfs, astar, reactive_astar
from src.partial_observation import run_partial_observation


# --------------------------------------------------
# EXPERIMENT CONFIGURATION
# --------------------------------------------------

SEEDS = range(100, 110)

SIZES = {
    "small": (10, 10),
    "medium": (20, 20),
    "large": (30, 30),
}

RESULT_DIR = Path("results/week7")

RAW_FILE = RESULT_DIR / "experiment_results.csv"
SUMMARY_FILE = RESULT_DIR / "experiment_summary.csv"
FAILURE_FILE = RESULT_DIR / "experiment_failures.csv"


# --------------------------------------------------
# MEASURE ALGORITHM PERFORMANCE
# --------------------------------------------------

def measure_algorithm(algorithm, maze):

    tracemalloc.start()
    start_time = time.perf_counter()

    outcome = algorithm(maze)

    runtime = time.perf_counter() - start_time

    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "success": outcome["success"],
        "path_length": outcome.get("path_length", 0),
        "nodes_expanded": outcome.get("nodes_expanded", 0),
        "runtime_seconds": runtime,
        "peak_memory_kb": peak_memory / 1024,
        "replan_count": outcome.get("replan_count", 0),
        "obstacles_discovered": outcome.get(
            "obstacles_discovered", 0
        ),
    }


# --------------------------------------------------
# RUN ONE EXPERIMENT
# --------------------------------------------------

def run_experiment(
    maze_id,
    size_name,
    seed,
    scenario,
    algorithm_name,
    algorithm,
    grid
):

    # Create a fresh maze for every algorithm.
    maze = Maze([row[:] for row in grid])

    try:

        if scenario == "partial_observation":

            if algorithm_name == "D* Lite":

                # The navigation function measures its own
                # runtime and peak memory.
                with redirect_stdout(io.StringIO()):
                    outcome = run_partial_observation(maze)

                result = {
                    "success": outcome["success"],
                    "path_length": outcome["path_length"],
                    "nodes_expanded": outcome["nodes_expanded"],
                    "runtime_seconds": outcome["runtime_seconds"],
                    "peak_memory_kb": outcome["peak_memory_kb"],
                    "replan_count": outcome["replan_count"],
                    "obstacles_discovered": outcome[
                        "obstacles_discovered"
                    ],
                }

            else:

                result = measure_algorithm(algorithm, maze)

        else:

            result = measure_algorithm(algorithm, maze)

        return {
            "maze_id": maze_id,
            "maze_size": size_name,
            "rows": maze.rows,
            "cols": maze.cols,
            "seed": seed,
            "scenario": scenario,
            "algorithm": algorithm_name,
            "success": result["success"],
            "path_length": result["path_length"],
            "nodes_expanded": result["nodes_expanded"],
            "runtime_seconds": result["runtime_seconds"],
            "peak_memory_kb": result["peak_memory_kb"],
            "replan_count": result["replan_count"],
            "obstacles_discovered": result[
                "obstacles_discovered"
            ],
            "error": "",
        }

    except Exception as error:

        return {
            "maze_id": maze_id,
            "maze_size": size_name,
            "rows": maze.rows,
            "cols": maze.cols,
            "seed": seed,
            "scenario": scenario,
            "algorithm": algorithm_name,
            "success": False,
            "path_length": 0,
            "nodes_expanded": 0,
            "runtime_seconds": 0,
            "peak_memory_kb": 0,
            "replan_count": 0,
            "obstacles_discovered": 0,
            "error": str(error),
        }


# --------------------------------------------------
# GENERATE AND RUN ALL EXPERIMENTS
# --------------------------------------------------

def run_all_experiments():

    RESULT_DIR.mkdir(parents=True, exist_ok=True)

    results = []

    full_algorithms = [
        ("BFS", bfs),
        ("DFS", dfs),
        ("A*", astar),
    ]

    partial_algorithms = [
        ("Reactive A*", reactive_astar),
        ("D* Lite", None),
    ]

    total = len(SEEDS) * len(SIZES) * (
        len(full_algorithms) + len(partial_algorithms)
    )

    completed = 0

    for size_name, dimensions in SIZES.items():

        rows, cols = dimensions

        for seed in SEEDS:

            maze_id = f"{size_name}_{seed}"

            # Generate each maze deterministically.
            grid = generate_maze(rows, cols, seed)

            print(f"\nTesting {maze_id}")

            # Fully visible maze experiments.
            for algorithm_name, algorithm in full_algorithms:

                result = run_experiment(
                    maze_id,
                    size_name,
                    seed,
                    "fully_visible",
                    algorithm_name,
                    algorithm,
                    grid,
                )

                results.append(result)
                completed += 1

                print(
                    f"[{completed}/{total}] "
                    f"{algorithm_name}: "
                    f"success={result['success']}"
                )

            # Partial-observation experiments.
            for algorithm_name, algorithm in partial_algorithms:

                result = run_experiment(
                    maze_id,
                    size_name,
                    seed,
                    "partial_observation",
                    algorithm_name,
                    algorithm,
                    grid,
                )

                results.append(result)
                completed += 1

                print(
                    f"[{completed}/{total}] "
                    f"{algorithm_name}: "
                    f"success={result['success']}"
                )

    return results


# --------------------------------------------------
# SAVE RAW RESULTS
# --------------------------------------------------

def save_raw_results(results):

    fields = list(results[0].keys())

    with open(
        RAW_FILE, "w", newline="", encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(results)

    print("\nRaw results saved:", RAW_FILE)


# --------------------------------------------------
# CALCULATE STATISTICAL SUMMARY
# --------------------------------------------------

def calculate_summary(results):

    groups = {}

    for result in results:

        key = (
            result["scenario"],
            result["maze_size"],
            result["algorithm"],
        )

        groups.setdefault(key, []).append(result)

    summary = []

    metrics = [
        "path_length",
        "nodes_expanded",
        "runtime_seconds",
        "peak_memory_kb",
        "replan_count",
        "obstacles_discovered",
    ]

    for key, runs in groups.items():

        scenario, maze_size, algorithm = key

        successful_runs = [
            run for run in runs if run["success"]
        ]

        success_values = [
            100.0 if run["success"] else 0.0
            for run in runs
        ]

        summary.append({
            "scenario": scenario,
            "maze_size": maze_size,
            "algorithm": algorithm,
            "metric": "success_rate_percent",
            "runs": len(runs),
            "mean": statistics.mean(success_values),
            "std_dev": statistics.stdev(success_values),
            "minimum": min(success_values),
            "maximum": max(success_values),
        })

        for metric in metrics:

            # Path length is meaningful only for successful runs.
            if metric == "path_length":
                selected = successful_runs
            else:
                selected = runs

            if not selected:
                continue

            values = [run[metric] for run in selected]

            summary.append({
                "scenario": scenario,
                "maze_size": maze_size,
                "algorithm": algorithm,
                "metric": metric,
                "runs": len(values),
                "mean": statistics.mean(values),
                "std_dev": (
                    statistics.stdev(values)
                    if len(values) > 1 else 0
                ),
                "minimum": min(values),
                "maximum": max(values),
            })

    fields = [
        "scenario",
        "maze_size",
        "algorithm",
        "metric",
        "runs",
        "mean",
        "std_dev",
        "minimum",
        "maximum",
    ]

    with open(
        SUMMARY_FILE, "w", newline="", encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(summary)

    print("Statistical summary saved:", SUMMARY_FILE)


# --------------------------------------------------
# SAVE INDIVIDUAL FAILURE CASES
# --------------------------------------------------

def save_failures(results):

    failures = [
        result for result in results
        if not result["success"]
    ]

    fields = list(results[0].keys())

    with open(
        FAILURE_FILE, "w", newline="", encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(failures)

    print("Failure analysis saved:", FAILURE_FILE)
    print("Total unsuccessful runs:", len(failures))


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

def main():

    print("===================================")
    print(" WEEK 7 - EXPERIMENT EVALUATION")
    print("===================================")

    results = run_all_experiments()

    save_raw_results(results)
    calculate_summary(results)
    save_failures(results)

    print("\n===================================")
    print(" WEEK 7 EXPERIMENTS COMPLETED")
    print("===================================")

    print("Total experiments:", len(results))
    print("Successful experiments:", sum(
        result["success"] for result in results
    ))

    print("\nGenerated files:")
    print(RAW_FILE)
    print(SUMMARY_FILE)
    print(FAILURE_FILE)


if __name__ == "__main__":
    main()

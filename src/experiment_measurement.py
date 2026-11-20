import csv
import gc
import random
import statistics
import time
import tracemalloc
from pathlib import Path

import matplotlib.pyplot as plt

from src.maze import Maze
from src.bfs import bfs
from src.dstar_lite import DStarLite
from src.maze_generator import generate_maze


# --------------------------------------------------
# PROJECT PATHS AND EXPERIMENT CONFIGURATION
# --------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent

RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

RAW_FILE = RESULTS / "week7_raw_results.csv"
SUMMARY_FILE = RESULTS / "week7_summary.csv"

PLOT_DIR = RESULTS / "week7_graphs"
PLOT_DIR.mkdir(exist_ok=True)

SEEDS = list(range(42, 52))

SIZES = {
    "small": (10, 10),
    "medium": (20, 20),
    "large": (30, 30),
}


# --------------------------------------------------
# PERFORMANCE MEASUREMENT
# --------------------------------------------------

def measure(algorithm):
    gc.collect()

    tracemalloc.start()
    start_time = time.perf_counter()

    result = algorithm()

    runtime = time.perf_counter() - start_time

    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return result, runtime, peak_memory / 1024


# --------------------------------------------------
# STATISTICAL FUNCTIONS
# --------------------------------------------------

def mean_sd(values):
    if not values:
        return 0, 0

    average = statistics.mean(values)

    spread = (
        statistics.stdev(values)
        if len(values) > 1
        else 0
    )

    return average, spread


# --------------------------------------------------
# SUMMARY CSV GENERATION
# --------------------------------------------------

def create_summary(raw_rows):

    summary = []
    groups = {}

    for row in raw_rows:

        key = (
            row["maze_size"],
            row["split"],
            row["algorithm"],
        )

        groups.setdefault(key, []).append(row)

    metrics = [
        "success",
        "path_length",
        "nodes_expanded",
        "runtime_seconds",
        "peak_memory_kb",
    ]

    for (size, split, algorithm), records in groups.items():

        output = {
            "maze_size": size,
            "split": split,
            "algorithm": algorithm,
            "runs": len(records),
        }

        for metric in metrics:

            values = [
                float(record[metric])
                for record in records
            ]

            average, spread = mean_sd(values)

            output[f"{metric}_mean"] = round(average, 6)
            output[f"{metric}_sd"] = round(spread, 6)

        output["success_rate_percent"] = round(
            100 * sum(int(r["success"]) for r in records)
            / len(records),
            2,
        )

        summary.append(output)

    if summary:

        with open(
            SUMMARY_FILE,
            "w",
            newline="",
            encoding="utf-8",
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=list(summary[0].keys()),
            )

            writer.writeheader()
            writer.writerows(summary)

    print("\nSummary saved:", SUMMARY_FILE)


# --------------------------------------------------
# GRAPH GENERATION
# Uses successful HELD-OUT TEST runs only
# --------------------------------------------------

def create_graphs(raw_rows):

    metrics = [
        ("nodes_expanded", "Average Nodes Expanded"),
        ("runtime_seconds", "Average Runtime (seconds)"),
        ("peak_memory_kb", "Average Peak Memory (KB)"),
        ("path_length", "Average Path Length"),
    ]

    for metric, title in metrics:

        fig, ax = plt.subplots(figsize=(9, 5))

        for algorithm in ["BFS", "DStarLite"]:

            means = []
            errors = []

            for size in SIZES:

                values = [
                    float(row[metric])
                    for row in raw_rows
                    if row["maze_size"] == size
                    and row["algorithm"] == algorithm
                    and row["split"] == "test"
                    and int(row["success"]) == 1
                ]

                average, spread = mean_sd(values)

                means.append(average)
                errors.append(spread)

            ax.errorbar(
                list(SIZES.keys()),
                means,
                yerr=errors,
                marker="o",
                capsize=5,
                label=algorithm,
            )

        ax.set_title(title)
        ax.set_xlabel("Maze Size")
        ax.set_ylabel(metric)
        ax.legend()
        ax.grid(True, alpha=0.3)

        fig.tight_layout()

        output = PLOT_DIR / f"{metric}_error_bars.png"

        fig.savefig(output, dpi=200)
        plt.close(fig)

        print("Graph saved:", output)


# --------------------------------------------------
# MAIN EXPERIMENT
# --------------------------------------------------

def run_experiment():

    raw_rows = []

    for size_name, (rows, cols) in SIZES.items():

        for seed in SEEDS:

            print(f"Testing {size_name}, seed {seed}...")

            random.seed(seed)

            grid = generate_maze(rows, cols, seed)
            maze = Maze(grid)

            split = (
                "development"
                if seed <= 48
                else "test"
            )

            algorithms = {
                "BFS": lambda m=maze: bfs(m),
                "DStarLite": lambda m=maze: DStarLite(m).plan(),
            }

            for algorithm_name, algorithm in algorithms.items():

                try:

                    result, runtime, memory = measure(algorithm)

                    success = bool(result.get("success", False))

                    path_length = (
                        result.get("path_length", 0)
                        if success else 0
                    )

                    nodes = result.get("nodes_expanded", 0)

                    raw_rows.append({

                        "maze_size": size_name,
                        "seed": seed,
                        "split": split,
                        "algorithm": algorithm_name,
                        "success": int(success),
                        "path_length": path_length,
                        "nodes_expanded": nodes,
                        "runtime_seconds": runtime,
                        "peak_memory_kb": memory,

                    })

                except Exception as error:

                    print(
                        f"Error: {algorithm_name}, "
                        f"{size_name}, seed {seed}: {error}"
                    )

                    raw_rows.append({

                        "maze_size": size_name,
                        "seed": seed,
                        "split": split,
                        "algorithm": algorithm_name,
                        "success": 0,
                        "path_length": 0,
                        "nodes_expanded": 0,
                        "runtime_seconds": 0,
                        "peak_memory_kb": 0,

                    })

    # Save raw experimental data

    if not raw_rows:
        print("No experiment results generated.")
        return

    with open(
        RAW_FILE,
        "w",
        newline="",
        encoding="utf-8",
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=list(raw_rows[0].keys()),
        )

        writer.writeheader()
        writer.writerows(raw_rows)

    print("\nRaw results saved:", RAW_FILE)

    # Generate summary and graphs

    create_summary(raw_rows)
    create_graphs(raw_rows)

    print("\nWEEK 7 EXPERIMENT COMPLETED!")


# --------------------------------------------------
# EXECUTION
# --------------------------------------------------

if __name__ == "__main__":
    run_experiment()
import csv
import statistics
from pathlib import Path

import matplotlib.pyplot as plt


# ==========================================
# PROJECT PATHS
# ==========================================

ROOT = Path(__file__).resolve().parent

RAW_FILE = ROOT / "results" / "week7_raw_results.csv"

PLOT_DIR = ROOT / "results" / "week7_graphs"
PLOT_DIR.mkdir(parents=True, exist_ok=True)

SIZES = ["small", "medium", "large"]

ALGORITHMS = ["BFS", "DStarLite"]


# ==========================================
# LOAD EXISTING EXPERIMENT DATA
# ==========================================

def load_results():

    if not RAW_FILE.exists():
        raise FileNotFoundError(
            f"CSV file not found: {RAW_FILE}"
        )

    with open(
        RAW_FILE,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)
        rows = list(reader)

    if not rows:
        raise ValueError("CSV file is empty.")

    required_columns = [
        "maze_size",
        "algorithm",
        "split",
        "success",
        "path_length",
        "nodes_expanded",
        "runtime_seconds",
        "peak_memory_kb",
    ]

    missing = [
        column for column in required_columns
        if column not in rows[0]
    ]

    if missing:
        raise ValueError(
            f"Missing CSV columns: {missing}"
        )

    print(f"Loaded {len(rows)} experiment records.")

    return rows


# ==========================================
# STATISTICAL CALCULATIONS
# ==========================================

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


# ==========================================
# GRAPH GENERATION
# ==========================================

def create_graphs(rows):

    metrics = [
        (
            "nodes_expanded",
            "Average Nodes Expanded",
            "Nodes Expanded"
        ),
        (
            "runtime_seconds",
            "Average Runtime (Seconds)",
            "Runtime (seconds)"
        ),
        (
            "peak_memory_kb",
            "Average Peak Memory (KB)",
            "Peak Memory (KB)"
        ),
        (
            "path_length",
            "Average Path Length",
            "Path Length"
        ),
    ]

    for metric, title, ylabel in metrics:

        fig, ax = plt.subplots(figsize=(9, 5))

        for algorithm in ALGORITHMS:

            means = []
            errors = []

            for size in SIZES:

                values = [
                    float(row[metric])
                    for row in rows
                    if row["maze_size"].lower() == size
                    and row["algorithm"] == algorithm
                    and row["split"] == "test"
                    and int(float(row["success"])) == 1
                ]

                average, spread = mean_sd(values)

                means.append(average)
                errors.append(spread)

            # Slight offset makes overlapping results visible
            offset = -0.06 if algorithm == "BFS" else 0.06

            x_positions = [
                index + offset
                for index in range(len(SIZES))
            ]

            ax.errorbar(
                x_positions,
                means,
                yerr=errors,
                marker="o" if algorithm == "BFS" else "s",
                linestyle="-" if algorithm == "BFS" else "--",
                linewidth=2,
                capsize=5,
                label=algorithm
            )

        ax.set_title(title)
        ax.set_xlabel("Maze Size")
        ax.set_ylabel(ylabel)

        ax.set_xticks(range(len(SIZES)))
        ax.set_xticklabels(SIZES)

        ax.legend()
        ax.grid(True, alpha=0.3)

        fig.tight_layout()

        output_file = (
            PLOT_DIR / f"{metric}_error_bars.png"
        )

        fig.savefig(output_file, dpi=200)
        plt.close(fig)

        print(f"Graph saved: {output_file}")


# ==========================================
# MAIN EXECUTION
# ==========================================

def main():

    print("\nWEEK 7 GRAPH REGENERATION")
    print("=" * 40)

    rows = load_results()

    create_graphs(rows)

    print("\n" + "=" * 40)
    print("ALL FOUR GRAPHS GENERATED SUCCESSFULLY!")
    print(f"Output folder: {PLOT_DIR}")


if __name__ == "__main__":
    main()
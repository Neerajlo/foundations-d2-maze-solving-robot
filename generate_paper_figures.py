
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project directory
ROOT = Path(__file__).resolve().parent

# Independent datasets
DATASETS = {
    "Dataset A": ROOT / "results" / "experiment_summary.csv",
    "Dataset B": ROOT / "results" / "experiment_runs" / "experiment_summary.csv"
}

# Output directory
OUTPUT_DIR = ROOT / "results" / "paper_figures"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

MAZE_SIZES = ["small", "medium", "large"]

# Observation scenarios
SCENARIOS = {
    "Fully Observable": ["BFS", "DFS", "A*"],
    "Partially Observable": ["Reactive A*", "D* Lite"]
}

# Performance metrics
METRICS = {
    "nodes_expanded": "Nodes Expanded",
    "path_length": "Path Length",
    "runtime_seconds": "Runtime (seconds)",
    "peak_memory_kb": "Peak Memory (KB)"
}

# Different visual styles for algorithms
STYLES = {
    "BFS": {"marker": "o", "linestyle": "-"},
    "DFS": {"marker": "s", "linestyle": "--"},
    "A*": {"marker": "^", "linestyle": "-."},
    "Reactive A*": {"marker": "D", "linestyle": "--"},
    "D* Lite": {"marker": "o", "linestyle": "-"}
}


def generate_figures(dataset_name, csv_path):

    print(f"\nProcessing {dataset_name}")

    if not csv_path.exists():
        raise FileNotFoundError(f"Missing file: {csv_path}")

    df = pd.read_csv(csv_path)

    required_columns = [
        "scenario",
        "maze_size",
        "algorithm",
        "metric",
        "mean",
        "std_dev"
    ]

    missing = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing:
        raise ValueError(f"Missing columns: {missing}")

    for metric, metric_label in METRICS.items():

        fig, axes = plt.subplots(1, 2, figsize=(14, 5))

        for ax, (scenario_name, algorithms) in zip(
            axes, SCENARIOS.items()
        ):

            scenario_key = (
                "fully_visible"
                if scenario_name == "Fully Observable"
                else "partial_observation"
            )

            scenario_data = df[
                (df["scenario"] == scenario_key) &
                (df["metric"] == metric)
            ]

            for algorithm in algorithms:

                data = scenario_data[
                    scenario_data["algorithm"] == algorithm
                ].copy()

                data["maze_size"] = pd.Categorical(
                    data["maze_size"],
                    categories=MAZE_SIZES,
                    ordered=True
                )

                data = data.sort_values("maze_size")

                if len(data) != 3:
                    raise ValueError(
                        f"Expected 3 records for {dataset_name}, "
                        f"{scenario_name}, {algorithm}, {metric}; "
                        f"found {len(data)}"
                    )

                # Horizontal separation for overlapping results
                if scenario_name == "Partially Observable":
                    offset = (
                        -0.045
                        if algorithm == "Reactive A*"
                        else 0.045
                    )
                else:
                    offset = 0

                x_positions = [
                    MAZE_SIZES.index(size) + offset
                    for size in data["maze_size"].astype(str)
                ]

                style = STYLES[algorithm]

                ax.errorbar(
                    x_positions,
                    data["mean"],
                    yerr=data["std_dev"],
                    marker=style["marker"],
                    linestyle=style["linestyle"],
                    linewidth=2,
                    markersize=6,
                    capsize=5,
                    label=algorithm
                )

            ax.set_title(scenario_name)
            ax.set_xlabel("Maze Size")
            ax.set_ylabel(metric_label)

            ax.set_xticks(range(3))
            ax.set_xticklabels(MAZE_SIZES)

            # Performance metrics cannot be negative
            ax.set_ylim(bottom=0)

            ax.legend()
            ax.grid(True, alpha=0.3)

        fig.suptitle(
            f"{dataset_name}: {metric_label}",
            fontsize=15,
            fontweight="bold"
        )

        # Dataset B measurement limitation
        if (
            dataset_name == "Dataset B"
            and metric in ["runtime_seconds", "peak_memory_kb"]
        ):

            fig.text(
                0.5,
                0.015,
                "Note: D* Lite uses a different measurement "
                "implementation in Dataset B.",
                ha="center",
                fontsize=9
            )

            fig.tight_layout(rect=[0, 0.07, 1, 0.93])

        else:
            fig.tight_layout(rect=[0, 0, 1, 0.93])

        dataset_letter = (
            "A" if dataset_name == "Dataset A" else "B"
        )

        output_file = (
            OUTPUT_DIR /
            f"dataset_{dataset_letter}_{metric}.png"
        )

        fig.savefig(
            output_file,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close(fig)

        print(f"Created: {output_file.name}")


def main():

    print("=" * 55)
    print("RESEARCH PAPER FIGURE GENERATION")
    print("=" * 55)

    for dataset_name, csv_path in DATASETS.items():
        generate_figures(dataset_name, csv_path)

    print("\nAll eight figures generated successfully!")
    print(f"Output folder: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()

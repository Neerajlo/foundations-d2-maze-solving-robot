import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# File locations
SUMMARY_FILE = Path("results/week7/experiment_summary.csv")
CHART_DIR = Path("results/week7/charts")

CHART_DIR.mkdir(parents=True, exist_ok=True)

# Load statistical summary
df = pd.read_csv(SUMMARY_FILE)

algorithms = ["Reactive A*", "D* Lite"]
maze_sizes = ["small", "medium", "large"]

# Required Week 7 metrics
metrics = {
    "nodes_expanded": {
        "title": "Nodes Expanded",
        "ylabel": "Mean Nodes Expanded",
        "filename": "nodes_expanded.png"
    },
    "peak_memory_kb": {
        "title": "Peak Memory Usage",
        "ylabel": "Mean Memory (KB)",
        "filename": "memory_usage.png"
    },
    "path_length": {
        "title": "Solution Quality - Path Length",
        "ylabel": "Mean Path Length",
        "filename": "path_length.png"
    }
}

for metric, details in metrics.items():

    subset = df[
        (df["scenario"] == "partial_observation") &
        (df["algorithm"].isin(algorithms)) &
        (df["metric"] == metric)
    ]

    plt.figure(figsize=(9, 6))

    for algorithm in algorithms:

        algorithm_data = subset[
            subset["algorithm"] == algorithm
        ]

        algorithm_data = (
            algorithm_data
            .set_index("maze_size")
            .reindex(maze_sizes)
        )

        means = algorithm_data["mean"].astype(float)
        errors = algorithm_data["std_dev"].astype(float)

        plt.errorbar(
            maze_sizes,
            means,
            yerr=errors,
            marker="o",
            capsize=6,
            linewidth=2,
            label=algorithm
        )

    plt.title(f"Week 7 Comparison: {details['title']}")
    plt.xlabel("Maze Size")
    plt.ylabel(details["ylabel"])
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    output_file = CHART_DIR / details["filename"]

    plt.savefig(output_file, dpi=300)
    plt.close()

    print("Chart saved:", output_file)

print("\nAll Week 7 charts generated successfully!")
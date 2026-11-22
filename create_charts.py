
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
SUMMARY_FILE = Path("results/experiment_summary.csv")
OUTPUT_DIR = Path("results/week12_graphs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load verified experiment summary
df = pd.read_csv(SUMMARY_FILE)

maze_sizes = ["small", "medium", "large"]

scenarios = {
    "fully_visible": ["BFS", "DFS", "A*"],
    "partial_observation": ["Reactive A*", "D* Lite"]
}

metrics = {
    "nodes_expanded": "Average Nodes Expanded",
    "path_length": "Average Path Length",
    "runtime_seconds": "Average Runtime (seconds)",
    "peak_memory_kb": "Average Peak Memory (KB)"
}

for metric, title in metrics.items():

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    for ax, (scenario, algorithms) in zip(
        axes, scenarios.items()
    ):

        scenario_data = df[
            (df["scenario"] == scenario) &
            (df["metric"] == metric)
        ]

        for algorithm in algorithms:

            algorithm_data = scenario_data[
                scenario_data["algorithm"] == algorithm
            ].copy()

            algorithm_data["maze_size"] = pd.Categorical(
                algorithm_data["maze_size"],
                categories=maze_sizes,
                ordered=True
            )

            algorithm_data = algorithm_data.sort_values(
                "maze_size"
            )

            if len(algorithm_data) != 3:
                raise ValueError(
                    f"Missing data: {scenario}, "
                    f"{algorithm}, {metric}"
                )

            ax.errorbar(
                algorithm_data["maze_size"].astype(str),
                algorithm_data["mean"],
                yerr=algorithm_data["std_dev"],
                marker="o",
                capsize=5,
                linewidth=2,
                label=algorithm
            )

        ax.set_title(scenario.replace("_", " ").title())
        ax.set_xlabel("Maze Size")
        ax.set_ylabel(title)
        ax.legend()
        ax.grid(True, alpha=0.3)

    fig.suptitle(
        f"Week 12 Experiment Results: {title}",
        fontsize=14
    )

    fig.tight_layout()

    output_file = OUTPUT_DIR / f"{metric}.png"

    fig.savefig(output_file, dpi=300)
    plt.close(fig)

    print("Generated:", output_file)

print("\nAll four Week 12 graphs generated successfully!")

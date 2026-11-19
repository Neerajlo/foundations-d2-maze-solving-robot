
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Read the statistical summary
df = pd.read_csv("results/experiment_summary.csv")

# Create a folder for charts
output_dir = Path("results/charts")
output_dir.mkdir(parents=True, exist_ok=True)


def create_chart(algorithms, title, filename):
    data = df[
        (df["metric"] == "nodes_expanded") &
        (df["algorithm"].isin(algorithms))
    ]

    plt.figure(figsize=(9, 5))

    for algorithm in algorithms:
        subset = data[data["algorithm"] == algorithm].copy()

        order = ["small", "medium", "large"]
        subset["maze_size"] = pd.Categorical(
            subset["maze_size"],
            categories=order,
            ordered=True
        )
        subset = subset.sort_values("maze_size")

        plt.errorbar(
            subset["maze_size"].astype(str),
            subset["mean"],
            yerr=subset["std_dev"],
            marker="o",
            capsize=5,
            linewidth=2,
            label=algorithm
        )

    plt.title(title)
    plt.xlabel("Maze Size")
    plt.ylabel("Average Nodes Expanded")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    plt.savefig(output_dir / filename, dpi=300)
    plt.close()


# Chart 1: Fully visible maze
create_chart(
    ["BFS", "A*"],
    "BFS vs A* - Nodes Expanded",
    "bfs_vs_astar.png"
)

# Chart 2: Partial observation
create_chart(
    ["Reactive A*", "D* Lite"],
    "Reactive A* vs D* Lite - Nodes Expanded",
    "reactive_astar_vs_dstar.png"
)

print("Both error-bar charts generated successfully!")
print("Saved in:", output_dir)


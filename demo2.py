
import csv
from pathlib import Path
import matplotlib.pyplot as plt

# Read existing experiment results.
input_file = Path("results/algorithm_comparison.csv")
output_dir = Path("results/charts")
output_dir.mkdir(parents=True, exist_ok=True)

with input_file.open("r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Select the two partial-observation algorithms.
selected_algorithms = ["Reactive A*", "D* Lite"]

comparison = [
    row for row in data
    if row["algorithm"] in selected_algorithms
]

if len(comparison) != 2:
    raise ValueError("Could not find both algorithms in the CSV.")

# Metrics to compare.
metrics = [
    ("avg_nodes_expanded", "Average Nodes Expanded", "Nodes"),
    ("avg_runtime_seconds", "Average Runtime", "Seconds"),
    ("avg_peak_memory_kb", "Average Peak Memory", "KB"),
    ("avg_path_length", "Average Path Length", "Steps")
]

# Display exact values in the terminal.
print("\nREACTIVE A* VS D* LITE")
print("=" * 45)

for row in comparison:
    print("\nAlgorithm:", row["algorithm"])
    print("Success rate:", row["success_rate_percent"], "%")
    print("Average path length:", row["avg_path_length"])
    print("Average nodes expanded:", row["avg_nodes_expanded"])
    print("Average runtime:", row["avg_runtime_seconds"], "seconds")
    print("Average memory:", row["avg_peak_memory_kb"], "KB")
    print("Average replans:", row["avg_replan_count"])

# Create four comparison charts.
fig, axes = plt.subplots(2, 2, figsize=(12, 9))
axes = axes.flatten()

colors = ["steelblue", "darkorange"]

for ax, (column, title, unit) in zip(axes, metrics):

    values = [
        float(row[column])
        for row in comparison
    ]

    bars = ax.bar(
        selected_algorithms,
        values,
        color=colors,
        width=0.55
    )

    ax.set_title(title, fontsize=12)
    ax.set_ylabel(unit)
    ax.grid(axis="y", alpha=0.3)

    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{value:.4f}" if unit == "Seconds" else f"{value:.2f}",
            ha="center",
            va="bottom",
            fontsize=9
        )

fig.suptitle(
    "Reactive A* vs D* Lite\n"
    "Partial-Observation Performance (9 Mazes)",
    fontsize=15
)

plt.tight_layout()

# Save the figure.
output_file = output_dir / "demo2.png"
plt.savefig(output_file, dpi=300, bbox_inches="tight")

print("\nChart saved to:", output_file)

plt.show()

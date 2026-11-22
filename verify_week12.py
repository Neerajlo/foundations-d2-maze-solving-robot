import pandas as pd

raw = pd.read_csv("results/experiment_results.csv")
summary = pd.read_csv("results/experiment_summary.csv")

metrics = [
    "path_length",
    "nodes_expanded",
    "runtime_seconds",
    "peak_memory_kb",
]

checks = []

for _, row in summary.iterrows():
    if row["metric"] not in metrics:
        continue

    data = raw[
        (raw["scenario"] == row["scenario"])
        & (raw["maze_size"] == row["maze_size"])
        & (raw["algorithm"] == row["algorithm"])
    ][row["metric"]].dropna()

    count_matches = len(data) == row["runs"]
    mean_matches = abs(data.mean() - row["mean"]) < 0.000001

    checks.append(count_matches and mean_matches)

print("Summary rows checked:", len(checks))
print("Matching:", sum(checks))
print("Mismatches:", len(checks) - sum(checks))

if all(checks):
    print("\nSUCCESS: Summary matches raw experimental data.")
else:
    print("\nWARNING: Some summary values do not match.")
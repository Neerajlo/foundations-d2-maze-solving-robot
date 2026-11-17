import csv
from pathlib import Path
from collections import defaultdict

results_dir = Path("results")

reactive_file = results_dir / "maze_results.csv"
dstar_file = results_dir / "dstar_lite_navigation_results.csv"

data = defaultdict(list)


def load_results():
    # Load BFS, DFS, A*, and Reactive A* results.
    with open(reactive_file, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            data[row["algorithm"]].append({
                "path_length": float(row["path_length"]),
                "nodes_expanded": float(row["nodes_expanded"]),
                "runtime_seconds": float(row["runtime_seconds"]),
                "peak_memory_kb": float(row["peak_memory_kb"]),
                "replan_count": float(row["replan_count"]),
                "success": row["path_found"].lower() == "true"
            })

    # Load D* Lite results.
    with open(dstar_file, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            data["D* Lite"].append({
                "path_length": float(row["path_length"]),
                "nodes_expanded": float(row["nodes_expanded"]),
                "runtime_seconds": float(row["runtime_seconds"]),
                "peak_memory_kb": float(row["peak_memory_kb"]),
                "replan_count": float(row["replan_count"]),
                "success": row["success"].lower() == "true"
            })


def create_comparison():
    fields = [
        "algorithm",
        "mazes_tested",
        "successful_runs",
        "success_rate_percent",
        "avg_path_length",
        "avg_nodes_expanded",
        "avg_runtime_seconds",
        "avg_peak_memory_kb",
        "avg_replan_count"
    ]

    rows = []

    for algorithm, runs in data.items():
        count = len(runs)

        rows.append({
            "algorithm": algorithm,
            "mazes_tested": count,
            "successful_runs": sum(r["success"] for r in runs),
            "success_rate_percent": round(
                sum(r["success"] for r in runs) / count * 100, 2
            ),
            "avg_path_length": round(
                sum(r["path_length"] for r in runs) / count, 2
            ),
            "avg_nodes_expanded": round(
                sum(r["nodes_expanded"] for r in runs) / count, 2
            ),
            "avg_runtime_seconds": round(
                sum(r["runtime_seconds"] for r in runs) / count, 8
            ),
            "avg_peak_memory_kb": round(
                sum(r["peak_memory_kb"] for r in runs) / count, 2
            ),
            "avg_replan_count": round(
                sum(r["replan_count"] for r in runs) / count, 2
            )
        })

    output_file = results_dir / "algorithm_comparison.csv"

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    print("\nAlgorithm comparison completed!")
    print("Results saved to:", output_file)

    for row in rows:
        print(row)


if __name__ == "__main__":
    load_results()
    create_comparison()
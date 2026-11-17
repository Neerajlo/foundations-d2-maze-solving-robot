
import csv
from pathlib import Path

from src.maze import Maze
from src.dstar_lite import DStarLite
from src.bfs import bfs


# Fixed obstacle coordinates from the original experiment.
OBSTACLES = [
    (2, 7), (9, 10), (11, 27), (24, 17),
    (5, 29), (12, 27), (19, 17), (21, 24),
    (5, 17), (1, 9), (27, 24), (26, 28),
    (10, 26), (7, 8), (13, 28), (24, 19),
    (0, 19), (24, 20), (18, 8), (4, 10),
    (10, 8), (5, 7), (20, 18), (5, 13)
]


def copy_maze(maze):
    return Maze(
        [row[:] for row in maze.grid],
        start=maze.start,
        goal=maze.goal
    )


def run_experiment():
    maze_path = Path("data/raw/large_42.json")
    output_path = Path(
        "results/member1_multi_obstacle_test_reproduced.csv"
    )

    # Load the original maze.
    original_maze = Maze.from_json(maze_path)

    dstar_maze = copy_maze(original_maze)
    bfs_maze = copy_maze(original_maze)

    # Initialise D* Lite and calculate the original path.
    planner = DStarLite(dstar_maze)
    initial_result = planner.plan()

    if not initial_result["success"]:
        raise RuntimeError("Initial D* Lite path was not found.")

    initial_path_length = initial_result["path_length"]

    print("Initial path length:", initial_path_length)

    rows = []

    # Introduce obstacles one at a time.
    for number, cell in enumerate(OBSTACLES, start=1):
        row, col = cell

        # Check that the obstacle is originally an open cell.
        if not original_maze.is_valid(cell):
            raise ValueError(
                f"Obstacle {cell} is not an open cell "
                "in the original maze."
            )

        # Update D* Lite using its existing search information.
        dstar_result = planner.update_obstacle(cell)

        # Apply the same obstacle to the BFS comparison maze.
        bfs_maze.grid[row][col] = 1

        expansions = dstar_result[
            "nodes_expanded_this_call"
        ]

        rows.append({
            "record_type": "obstacle",
            "maze": "large_42",
            "size": f"{original_maze.rows}x{original_maze.cols}",
            "obstacle_number": number,
            "obstacle_cell": str(cell),
            "expansions_this_update": expansions,
            "initial_path_length": "",
            "final_dstar_path_length": "",
            "final_bfs_path_length": "",
            "dstar_total_expansions": "",
            "dstar_replanning_expansions": "",
            "bfs_expansions": "",
            "success": dstar_result["success"]
        })

        print(
            f"Obstacle {number:02d}: {cell} | "
            f"New expansions: {expansions} | "
            f"Success: {dstar_result['success']}"
        )

        if not dstar_result["success"]:
            raise RuntimeError(
                f"D* Lite could not find a path after obstacle {cell}."
            )

    # Run a fresh BFS search on the final updated maze.
    final_dstar_result = planner.plan()
    final_bfs_result = bfs(bfs_maze)

    if not final_dstar_result["success"]:
        raise RuntimeError("Final D* Lite path was not found.")

    if not final_bfs_result["success"]:
        raise RuntimeError("Final BFS path was not found.")

    replanning_expansions = (
        planner.nodes_expanded - initial_result["nodes_expanded"]
    )

    summary = {
        "record_type": "summary",
        "maze": "large_42",
        "size": f"{original_maze.rows}x{original_maze.cols}",
        "obstacle_number": len(OBSTACLES),
        "obstacle_cell": "",
        "expansions_this_update": replanning_expansions,
        "initial_path_length": initial_path_length,
        "final_dstar_path_length": final_dstar_result["path_length"],
        "final_bfs_path_length": final_bfs_result["path_length"],
        "dstar_total_expansions": planner.nodes_expanded,
        "dstar_replanning_expansions": replanning_expansions,
        "bfs_expansions": final_bfs_result["nodes_expanded"],
        "success": (
            final_dstar_result["success"]
            and final_bfs_result["success"]
        )
    }

    rows.append(summary)

    # Save results without overwriting the original CSV.
    output_path.parent.mkdir(parents=True, exist_ok=True)

    columns = list(summary.keys())

    with output_path.open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)

    print("\n========== FINAL COMPARISON ==========")
    print("Obstacles:", len(OBSTACLES))
    print("Initial path length:", initial_path_length)
    print("D* Lite final path:", final_dstar_result["path_length"])
    print("BFS final path:", final_bfs_result["path_length"])
    print("D* Lite total expansions:", planner.nodes_expanded)
    print("D* Lite replanning expansions:", replanning_expansions)
    print("BFS fresh-search expansions:", final_bfs_result["nodes_expanded"])
    print("Results saved to:", output_path)


if __name__ == "__main__":
    run_experiment()

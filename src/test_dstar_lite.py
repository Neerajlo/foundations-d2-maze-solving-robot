
from pathlib import Path

from src.maze import Maze
from src.dstar_lite import DStarLite
from src.bfs import bfs


def run_baseline_comparison(maze_file):
    """Compare incremental D* Lite replanning with fresh BFS."""

    # 1. Load the original maze.
    original_maze = Maze.from_json(maze_file)

    # 2. Create independent maze copies.
    dstar_maze = Maze(
        [row[:] for row in original_maze.grid],
        start=original_maze.start,
        goal=original_maze.goal
    )

    bfs_maze = Maze(
        [row[:] for row in original_maze.grid],
        start=original_maze.start,
        goal=original_maze.goal
    )

    # 3. Run the initial D* Lite search.
    planner = DStarLite(dstar_maze)
    initial = planner.plan()

    if not initial["success"] or len(initial["path"]) < 2:
        print(f"\nMaze: {maze_file.stem}")
        print("Initial path not found.")
        return None

    initial_expansions = initial["nodes_expanded"]

    # 4. Find an obstacle that still allows an alternative route.
    blocked_cell = None

    for candidate in initial["path"][1:-1]:

        test_maze = Maze(
            [row[:] for row in original_maze.grid],
            start=original_maze.start,
            goal=original_maze.goal
        )

        row, col = candidate
        test_maze.grid[row][col] = 1

        test_result = bfs(test_maze)

        if test_result["success"]:
            blocked_cell = candidate
            break

    if blocked_cell is None:
        print(f"\nMaze: {maze_file.stem}")
        print("No recoverable obstacle found.")
        return None

    # 5. D* Lite discovers the obstacle and incrementally replans.
    dstar_result = planner.update_obstacle(blocked_cell)

    dstar_replan_expansions = dstar_result.get(
        "nodes_expanded_this_call", 0
    )

    dstar_total_expansions = dstar_result["nodes_expanded"]

    # 6. Apply exactly the same obstacle to the BFS maze.
    row, col = blocked_cell
    bfs_maze.grid[row][col] = 1

    # 7. Run a fresh BFS search on the updated maze.
    bfs_result = bfs(bfs_maze)

    bfs_expansions = bfs_result.get("nodes_expanded", 0)

    # 8. Display the results.
    print("\n========================================")
    print("Maze:", maze_file.stem)
    print("Maze size:", f"{original_maze.rows} x {original_maze.cols}")
    print("Newly discovered obstacle:", blocked_cell)

    print("\nD* Lite Results")
    print("Initial path length:", initial["path_length"])
    print("Initial search expansions:", initial_expansions)
    print("Additional replanning expansions:", dstar_replan_expansions)
    print("Total D* Lite expansions:", dstar_total_expansions)
    print("Replanning count:", dstar_result["replan_count"])
    print("Updated success:", dstar_result["success"])
    print("Updated path length:", dstar_result["path_length"])

    print("\nBFS Results")
    print("Success:", bfs_result["success"])
    print("Path length:", bfs_result["path_length"])
    print("Fresh search expansions:", bfs_expansions)

    # 9. Compare the final paths.
    if dstar_result["success"] == bfs_result["success"]:

        if dstar_result["success"]:
            if dstar_result["path_length"] == bfs_result["path_length"]:
                print("\nResult: Both algorithms found equally short paths.")
            else:
                print("\nResult: Both found paths, but path lengths differ.")

        else:
            print("\nResult: Both algorithms reported no available path.")

    else:
        print("\nResult: The algorithms produced different outcomes.")

    # 10. Compare additional D* Lite work with fresh BFS work.
    print("\nExpansion Comparison")

    if dstar_replan_expansions < bfs_expansions:
        print("D* Lite expanded fewer nodes during replanning.")

    elif dstar_replan_expansions > bfs_expansions:
        print("BFS expanded fewer nodes in this comparison.")

    else:
        print("Both performed the same number of expansions.")

    return {
        "maze": maze_file.stem,
        "obstacle": blocked_cell,
        "initial_dstar_expansions": initial_expansions,
        "dstar_replanning_expansions": dstar_replan_expansions,
        "dstar_total_expansions": dstar_total_expansions,
        "bfs_expansions": bfs_expansions,
        "dstar_success": dstar_result["success"],
        "bfs_success": bfs_result["success"],
        "dstar_path_length": dstar_result["path_length"],
        "bfs_path_length": bfs_result["path_length"]
    }


if __name__ == "__main__":

    maze_files = sorted(Path("data/raw").glob("*.json"))

    print("Total mazes:", len(maze_files))

    results = []

    for maze_file in maze_files:
        result = run_baseline_comparison(maze_file)

        if result is not None:
            results.append(result)

    print("\n========================================")
    print("FINAL SUMMARY")

    print("Mazes tested:", len(results))

    if results:

        average_replanning = sum(
            item["dstar_replanning_expansions"]
            for item in results
        ) / len(results)

        average_bfs = sum(
            item["bfs_expansions"]
            for item in results
        ) / len(results)

        print(
            "Average D* Lite replanning expansions:",
            round(average_replanning, 2)
        )

        print(
            "Average BFS fresh-search expansions:",
            round(average_bfs, 2)
        )

        successful = sum(
            item["dstar_success"] and item["bfs_success"]
            for item in results
        )

        print("Successful comparisons:", successful, "/", len(results))

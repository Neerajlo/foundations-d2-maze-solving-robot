
from src.maze import Maze
from src.dstar_lite import DStarLite
from src.bfs import bfs


def find_recoverable_obstacle(maze, path, target_fraction):
    """
    Select a cell on the current path whose removal
    still allows BFS to find an alternative route.
    """

    if len(path) < 3:
        return None

    target_index = int((len(path) - 1) * target_fraction)

    candidates = sorted(
        path[1:-1],
        key=lambda cell: abs(path.index(cell) - target_index)
    )

    for candidate in candidates:
        test_maze = Maze(
            [row[:] for row in maze.grid],
            start=maze.start,
            goal=maze.goal
        )

        row, col = candidate
        test_maze.grid[row][col] = 1

        if bfs(test_maze)["success"]:
            return candidate

    return None


def run_challenging_test(maze_file):
    actual_maze = Maze.from_json(maze_file)

    dstar_maze = Maze(
        [row[:] for row in actual_maze.grid],
        start=actual_maze.start,
        goal=actual_maze.goal
    )

    bfs_maze = Maze(
        [row[:] for row in actual_maze.grid],
        start=actual_maze.start,
        goal=actual_maze.goal
    )

    planner = DStarLite(dstar_maze)

    initial = planner.plan()

    print("\n====================================")
    print("CHALLENGING D* LITE TEST")
    print("Maze:", maze_file)
    print("Maze size:", actual_maze.rows, "x", actual_maze.cols)

    if not initial["success"]:
        print("Initial path not found.")
        return

    print("Initial path length:", initial["path_length"])

    # Introduce obstacles at different positions
    # along the current path.
    target_fractions = [0.25, 0.50, 0.75]

    for step, fraction in enumerate(target_fractions, start=1):

        current_result = planner.plan()

        if not current_result["success"]:
            print("No route available before obstacle", step)
            break

        obstacle = find_recoverable_obstacle(
            dstar_maze,
            current_result["path"],
            fraction
        )

        if obstacle is None:
            print("No recoverable obstacle found for step", step)
            break

        print("\n---------- Obstacle", step, "----------")
        print("Discovered obstacle:", obstacle)

        # D* Lite updates its existing search.
        dstar_result = planner.update_obstacle(obstacle)

        # BFS starts a fresh search on the same updated maze.
        row, col = obstacle
        bfs_maze.grid[row][col] = 1

        bfs_result = bfs(bfs_maze)

        print("D* Lite success:", dstar_result["success"])
        print("BFS success:", bfs_result["success"])

        print(
            "D* Lite replanning expansions:",
            dstar_result["nodes_expanded_this_call"]
        )

        print(
            "D* Lite total expansions:",
            dstar_result["nodes_expanded"]
        )

        print(
            "BFS fresh-search expansions:",
            bfs_result.get("nodes_expanded", 0)
        )

        print("D* Lite path length:", dstar_result["path_length"])
        print("BFS path length:", bfs_result["path_length"])

        if (
            dstar_result["success"]
            and bfs_result["success"]
            and dstar_result["path_length"] == bfs_result["path_length"]
        ):
            print("Comparison: Both found equally short paths.")

        elif dstar_result["success"] != bfs_result["success"]:
            print("Comparison: Algorithms produced different outcomes.")

        else:
            print("Comparison: Path lengths differ or no route exists.")

    print("\n========== FINAL SUMMARY ==========")
    print("Obstacles discovered:", planner.replan_count)
    print("Total D* Lite expansions:", planner.nodes_expanded)


if __name__ == "__main__":
    run_challenging_test("data/raw/large_42.json")

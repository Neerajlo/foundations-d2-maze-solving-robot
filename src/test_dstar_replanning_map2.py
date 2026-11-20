
import time
import tracemalloc

from src.dstar_lite import DStarLite
from src.external_dataset_loader import load_movingai_map
from src.maze import Maze
from src.bfs import bfs


MAP_FILE = "datasets/maze512-2-0.map"
START = (1, 1)
GOAL = (511, 511)
OBSTACLE = (127, 45)


def validate_path(maze, path, obstacle):
    if not path:
        return False

    if path[0] != maze.start or path[-1] != maze.goal:
        return False

    if obstacle in path:
        return False

    for cell in path:
        if not maze.is_valid(cell):
            return False

    for current, next_cell in zip(path, path[1:]):
        distance = (
            abs(current[0] - next_cell[0])
            + abs(current[1] - next_cell[1])
        )
        if distance != 1:
            return False

    return True


def main():
    print("LARGE MAP - D* LITE DYNAMIC REPLANNING")
    print("--------------------------------------")

    grid = load_movingai_map(MAP_FILE)
    maze = Maze(grid, start=START, goal=GOAL)

    print("Map dimensions:", maze.rows, "x", maze.cols)
    print("Start:", START)
    print("Goal:", GOAL)
    print("New obstacle:", OBSTACLE)

    if not maze.is_valid(START) or not maze.is_valid(GOAL):
        print("Invalid start or goal.")
        return

    if not maze.is_valid(OBSTACLE):
        print("Selected obstacle is not an open cell.")
        return

    # Step 1: Calculate the initial path using D* Lite.
    planner = DStarLite(maze)

    tracemalloc.start()
    start_time = time.perf_counter()

    initial_result = planner.plan()

    initial_runtime = time.perf_counter() - start_time
    _, initial_peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("\nINITIAL D* LITE RESULTS")
    print("Success:", initial_result["success"])
    print("Path length:", initial_result["path_length"])
    print("Nodes expanded:", initial_result["nodes_expanded"])
    print("Runtime:", round(initial_runtime, 6), "seconds")
    print("Peak memory:", round(initial_peak / 1024, 2), "KB")

    if not initial_result["success"]:
        print("Initial planning failed.")
        return

    if OBSTACLE not in initial_result["path"]:
        print("Selected obstacle is not on the D* Lite path.")
        print("Choose another verified obstacle.")
        return

    # Step 2: Independently verify an alternative route with BFS.
    original_grid = [row[:] for row in maze.grid]
    maze.grid[OBSTACLE[0]][OBSTACLE[1]] = 1

    bfs_result = bfs(maze)

    maze.grid = original_grid

    print("\nINDEPENDENT BFS VERIFICATION")
    print("Alternative route exists:", bfs_result["success"])
    print("BFS path length:", bfs_result["path_length"])

    if not bfs_result["success"]:
        print("Obstacle blocks all available routes.")
        return

    # Step 3: Introduce the obstacle and replan with D* Lite.
    tracemalloc.start()
    start_time = time.perf_counter()

    replanned_result = planner.update_obstacle(
        OBSTACLE,
        blocked=True
    )

    replanning_runtime = time.perf_counter() - start_time
    _, replanning_peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("\nD* LITE REPLANNING RESULTS")
    print("Success:", replanned_result["success"])
    print("New path length:", replanned_result["path_length"])
    print("Nodes expanded during replanning:",
          replanned_result["nodes_expanded_this_call"])
    print("Total nodes expanded:", replanned_result["nodes_expanded"])
    print("Replan count:", replanned_result["replan_count"])
    print("Replanning runtime:", round(replanning_runtime, 6), "seconds")
    print("Replanning peak memory:",
          round(replanning_peak / 1024, 2), "KB")

    # Step 4: Validate the new route.
    valid_path = (
        replanned_result["success"]
        and validate_path(maze, replanned_result["path"], OBSTACLE)
    )

    path_changed = (
        initial_result["path"] != replanned_result["path"]
    )

    optimal_match = (
        replanned_result["path_length"] == bfs_result["path_length"]
    )

    print("\nFINAL VALIDATION")
    print("New path is valid:", valid_path)
    print("New path avoids obstacle:", valid_path)
    print("Path changed:", path_changed)
    print("Matches BFS path length:", optimal_match)
    print("Replan count is 1:", replanned_result["replan_count"] == 1)

    if (
        valid_path
        and path_changed
        and optimal_match
        and replanned_result["replan_count"] == 1
    ):
        print("\nLARGE-MAP DYNAMIC REPLANNING TEST PASSED")
    else:
        print("\nLARGE-MAP DYNAMIC REPLANNING TEST NEEDS INVESTIGATION")


if __name__ == "__main__":
    main()


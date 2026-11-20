
from src.maze import Maze
from src.dstar_lite import DStarLite


def main():
    print("D* LITE - DYNAMIC REPLANNING TEST")
    print("--------------------------------")

    # Create a 10x10 maze with no obstacles.
    grid = [[0 for _ in range(10)] for _ in range(10)]

    maze = Maze(
        grid,
        start=(0, 0),
        goal=(9, 9)
    )

    # Step 1: Calculate the initial path.
    planner = DStarLite(maze)
    initial_result = planner.plan()

    print("\nINITIAL PATH")
    print("Success:", initial_result["success"])
    print("Path length:", initial_result["path_length"])
    print("Path:", initial_result["path"])

    if not initial_result["success"]:
        print("Initial pathfinding failed.")
        return

    # Step 2: Select a cell from the middle of the path.
    obstacle = initial_result["path"][len(initial_result["path"]) // 2]

    print("\nNEW OBSTACLE")
    print("Obstacle position:", obstacle)

    # Step 3: Introduce the obstacle and replan.
    replanned_result = planner.update_obstacle(obstacle, blocked=True)

    print("\nREPLANNING RESULTS")
    print("Success:", replanned_result["success"])
    print("New path length:", replanned_result["path_length"])
    print("New path:", replanned_result["path"])
    print("Nodes expanded this call:",
          replanned_result["nodes_expanded_this_call"])
    print("Total nodes expanded:",
          replanned_result["nodes_expanded"])
    print("Replan count:", replanned_result["replan_count"])

    # Step 4: Verify that the new path avoids the obstacle.
    if replanned_result["success"]:
        obstacle_avoided = obstacle not in replanned_result["path"]
        print("\nVALIDATION")
        print("New path avoids obstacle:", obstacle_avoided)
        print("Path changed:",
              initial_result["path"] != replanned_result["path"])

        if obstacle_avoided and initial_result["path"] != replanned_result["path"]:
            print("\nDYNAMIC REPLANNING TEST PASSED")
        else:
            print("\nDYNAMIC REPLANNING TEST NEEDS INVESTIGATION")
    else:
        print("\nDYNAMIC REPLANNING TEST FAILED")


if __name__ == "__main__":
    main()

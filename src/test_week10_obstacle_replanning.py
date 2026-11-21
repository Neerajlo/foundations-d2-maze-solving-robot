from src.maze import Maze
from src.solver import reactive_astar
from src.reactive_astar_experiment import reactive_astar_with_visit_penalty


def main():

    # 0 = free cell, 1 = obstacle
    grid = [
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    start = (0, 0)
    goal = (0, 4)

    print("WEEK 10 CONTROLLED OBSTACLE TEST")
    print("=" * 45)

    maze = Maze(grid, start=start, goal=goal)

    print("Start:", start)
    print("Goal:", goal)

    original = reactive_astar(maze)

    enhanced_maze = Maze(grid, start=start, goal=goal)

    enhanced = reactive_astar_with_visit_penalty(
        enhanced_maze,
        visit_penalty=0.5
    )

    print("\nORIGINAL REACTIVE A*")
    print("Success:", original["success"])
    print("Distance:", original["actual_distance"])
    print("Obstacles discovered:", original["obstacles_discovered"])
    print("Replans:", original["replan_count"])
    print("Final position:", original["final_position"])

    print("\nENHANCED REACTIVE A*")
    print("Success:", enhanced["success"])
    print("Distance:", enhanced["actual_distance"])
    print("Obstacles discovered:", enhanced["obstacles_discovered"])
    print("Replans:", enhanced["replan_count"])
    print("Revisited moves:", enhanced["revisited_moves"])
    print("Final position:", enhanced["final_position"])


if __name__ == "__main__":
    main()
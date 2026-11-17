import csv
import time
import tracemalloc
from pathlib import Path
from src.maze import Maze

from src.robot import Robot
from src.dstar_lite import DStarLite


def run_partial_observation(actual_maze):
    """
    Run a robot simulation in which the robot
    initially knows only its starting cell.

    Unknown cells are assumed open for planning.
    D* Lite replans when the robot discovers an obstacle.
    """
    # Start performance measurements.
    tracemalloc.start()
    start_time = time.perf_counter()

    # Step 1: Initialize the robot.
    robot = Robot(actual_maze)

    # Step 2: Create a separate map using known information.
    planning_maze = robot.get_planning_maze()

    # Step 3: Initialize D* Lite.
    planner = DStarLite(
        planning_maze,
        start=robot.position,
        goal=robot.goal
    )

    moves = 0
    attempts = 0
    max_attempts = actual_maze.rows * actual_maze.cols * 4

    print("\nStarting partial-observation simulation")
    print("Start:", robot.position)
    print("Goal:", robot.goal)

    # Step 4: Navigate until the goal is reached.
    while not robot.reached_goal() and attempts < max_attempts:

        attempts += 1

        # Calculate a route using the currently known map.
        result = planner.plan()

        if not result["success"]:
            print("No route available.")
            break

        if len(result["path"]) < 2:
            break

        # Select the next cell.
        next_cell = result["path"][1]

        # Step 5: Attempt to move.
        if not robot.move(next_cell):

            # An obstacle was discovered.
            print("Obstacle discovered:", next_cell)

            # Update D* Lite's planning map.
            planner.update_obstacle(next_cell)

            print("D* Lite replanned the route.")
            continue

        # Successful movement.
        moves += 1

        # Step 6: Update the planner's current position.
        planner.move_start(robot.position)

    success = robot.reached_goal()

    # Capture performance measurements.
    elapsed_time = time.perf_counter() - start_time
    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Store final results.
    final_result = {
        "success": success,
        "path": robot.path_history,
        "path_length": len(robot.path_history) - 1,
        "nodes_expanded": planner.nodes_expanded,
        "replan_count": planner.replan_count,
        "obstacles_discovered": len(robot.discovered_obstacles),
        "discovered_obstacle_cells": robot.discovered_obstacles,
        "moves": moves,
        "attempts": attempts,
        "runtime_seconds": round(elapsed_time, 8),
        "peak_memory_kb": round(peak_memory / 1024, 2)
    }

    print("\n========== SIMULATION RESULTS ==========")
    print("Navigation successful:", success)
    print("Final position:", robot.position)
    print("Actual distance travelled:", final_result["path_length"])
    print("Nodes expanded:", final_result["nodes_expanded"])
    print("Replanning count:", final_result["replan_count"])
    print("Obstacles discovered:", final_result["obstacles_discovered"])
    print("Runtime:", final_result["runtime_seconds"], "seconds")
    print("Peak memory:", final_result["peak_memory_kb"], "KB")
    print("Robot path:", final_result["path"])

    return final_result
def save_results_to_csv(results, output_file="results/dstar_lite_navigation_results.csv"):
    """Save D* Lite navigation results to CSV."""

    Path(output_file).parent.mkdir(parents=True, exist_ok=True)

    fields = [
        "maze_id",
        "maze_size",
        "success",
        "path_length",
        "nodes_expanded",
        "replan_count",
        "obstacles_discovered",
        "moves",
        "attempts",
        "runtime_seconds",
        "peak_memory_kb"
    ]

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(
            {field: result.get(field, "") for field in fields}
            for result in results
        )

    print(f"\nResults saved to: {output_file}")
if __name__ == "__main__":

    maze_files = sorted(Path("data/raw").glob("*.json"))
    results = []

    print("Total mazes:", len(maze_files))

    for maze_file in maze_files:
        print(f"\nProcessing: {maze_file.stem}")

        maze = Maze.from_json(maze_file)

        result = run_partial_observation(maze)

        result["maze_id"] = maze_file.stem
        result["maze_size"] = f"{maze.rows}x{maze.cols}"

        results.append(result)

    save_results_to_csv(results)

    print("\nAll maze simulations completed!")
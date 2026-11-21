
import heapq
import time
import tracemalloc
import csv

from src.solver import reactive_astar


def reactive_astar_with_visit_penalty(maze, visit_penalty=1):
    """
    Enhanced Reactive A* with visited-cell awareness.

    Unknown cells are temporarily treated as open.
    When an obstacle is discovered, the robot replans.
    Previously visited cells receive an additional cost.
    """

    rows = maze.rows
    cols = maze.cols
    start = maze.start
    goal = maze.goal

    UNKNOWN = -1
    FREE = 0
    WALL = 1

    discovered_map = [
        [UNKNOWN for _ in range(cols)]
        for _ in range(rows)
    ]

    discovered_map[start[0]][start[1]] = FREE

    robot_position = start

    visited_cells = {start}
    path_history = [start]

    replan_count = 0
    plan_count = 0
    nodes_expanded = 0
    obstacles_discovered = 0
    actual_distance = 0
    revisited_moves = 0

    directions = maze.DIRECTIONS

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def plan_path(position):
        nonlocal nodes_expanded

        open_list = []

        g_score = {position: 0}
        came_from = {}

        # Same priority-queue ordering as original Reactive A*.
        heapq.heappush(
            open_list,
            (heuristic(position, goal), 0, position)
        )

        while open_list:
            _, current_cost, current = heapq.heappop(open_list)

            if current_cost != g_score.get(current):
                continue

            nodes_expanded += 1

            if current == goal:
                path = [current]

                while current in came_from:
                    current = came_from[current]
                    path.append(current)

                return path[::-1]

            for dr, dc in directions:
                nr = current[0] + dr
                nc = current[1] + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                if discovered_map[nr][nc] == WALL:
                    continue

                neighbour = (nr, nc)

                movement_cost = 1

                if neighbour in visited_cells:
                    movement_cost += visit_penalty

                new_cost = current_cost + movement_cost

                if new_cost < g_score.get(
                    neighbour, float("inf")
                ):
                    g_score[neighbour] = new_cost
                    came_from[neighbour] = current

                    f_score = (
                        new_cost + heuristic(neighbour, goal)
                    )

                    # Same tuple structure as original Reactive A*.
                    heapq.heappush(
                        open_list,
                        (f_score, new_cost, neighbour)
                    )

        return None

    while robot_position != goal:

        path = plan_path(robot_position)

        if path is None:
            break

        plan_count += 1
        path_blocked = False

        for next_cell in path[1:]:
            r, c = next_cell

            if maze.grid[r][c] == WALL:

                if discovered_map[r][c] != WALL:
                    discovered_map[r][c] = WALL
                    obstacles_discovered += 1

                replan_count += 1
                path_blocked = True
                break

            if next_cell in visited_cells:
                revisited_moves += 1

            discovered_map[r][c] = FREE
            robot_position = next_cell

            actual_distance += 1
            visited_cells.add(next_cell)
            path_history.append(next_cell)

            if robot_position == goal:
                break

        if not path_blocked and robot_position != goal:
            break

    return {
        "success": robot_position == goal,
        "actual_distance": actual_distance,
        "path_length": actual_distance,
        "nodes_expanded": nodes_expanded,
        "replan_count": replan_count,
        "plan_count": plan_count,
        "obstacles_discovered": obstacles_discovered,
        "revisited_moves": revisited_moves,
        "unique_cells_visited": len(visited_cells),
        "path_history": path_history,
        "final_position": robot_position,
    }


def measure_algorithm(algorithm, maze):

    tracemalloc.start()
    start_time = time.perf_counter()

    result = algorithm(maze)

    runtime = time.perf_counter() - start_time

    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return result, runtime, peak_memory / 1024


def main():

    from src.external_dataset_loader import load_movingai_scenario

    MAP_FILE = "datasets/maze512-1-0.map"
    SCENARIO_FILE = "datasets/maze512-1-0.map.scen"

    SCENARIO_INDICES = [100, 101, 102, 103, 104, 105, 106, 107]
    PENALTY_VALUES = [0, 0.1, 0.25, 0.5]

    all_results = []

    print("CORRECTED REACTIVE A* PENALTY EXPERIMENT")
    print("========================================")

    for scenario_index in SCENARIO_INDICES:

        maze, scenario = load_movingai_scenario(
            MAP_FILE,
            SCENARIO_FILE,
            scenario_index
        )

        print("\nScenario:", scenario_index)
        print("Reference optimal length:", scenario["optimal_length"])

        for penalty in PENALTY_VALUES:

            tracemalloc.start()
            start_time = time.perf_counter()

            result = reactive_astar_with_visit_penalty(
                maze,
                visit_penalty=penalty
            )

            runtime = time.perf_counter() - start_time

            current_memory, peak_memory = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            row = {
                "scenario": scenario_index,
                "penalty": penalty,
                "success": result["success"],
                "distance": result["actual_distance"],
                "nodes": result["nodes_expanded"],
                "runtime": runtime,
                "memory": peak_memory / 1024,
                "replans": result["replan_count"],
                "revisited": result["revisited_moves"]
            }

            all_results.append(row)

            print(
                f"Penalty={penalty:<5} "
                f"Success={result['success']!s:<6} "
                f"Distance={result['actual_distance']:<6} "
                f"Nodes={result['nodes_expanded']:<9} "
                f"Runtime={runtime:.6f}s "
                f"Replans={result['replan_count']:<5} "
                f"Revisits={result['revisited_moves']}"
            )

    # Save experiment results to CSV
    output_file = "results/reactive_astar_visit_penalty_results.csv"

    fieldnames = [
        "scenario",
        "penalty",
        "success",
        "distance",
        "nodes",
        "runtime",
        "memory",
        "replans",
        "revisited"
    ]

    with open(output_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_results)

    print(f"\nResults saved to {output_file}")

    # Display overall averages
    print("\n\nOVERALL AVERAGES")
    print("================")

    for penalty in PENALTY_VALUES:

        selected = [
            r for r in all_results
            if r["penalty"] == penalty
        ]

        count = len(selected)

        print(
            f"\nPenalty: {penalty}"
            f"\nSuccess: {sum(r['success'] for r in selected)}/{count}"
            f"\nAverage distance: {sum(r['distance'] for r in selected)/count:.2f}"
            f"\nAverage nodes: {sum(r['nodes'] for r in selected)/count:.2f}"
            f"\nAverage runtime: {sum(r['runtime'] for r in selected)/count:.6f}s"
            f"\nAverage replans: {sum(r['replans'] for r in selected)/count:.2f}"
        )


if __name__ == "__main__":
    main()

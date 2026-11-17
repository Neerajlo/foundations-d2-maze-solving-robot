import heapq


def _search(maze, method):
    start, goal = maze.start, maze.goal
    parent = {start: None}
    visited = []
    costs = {start: 0}

    if method == "BFS":
        from collections import deque
        frontier = deque([start])
        priority_mode = False
    elif method == "DFS":
        frontier = [start]
        priority_mode = False
    else:
        frontier = [(0, start)]
        priority_mode = True

    while frontier:
        if priority_mode:
            _, current = heapq.heappop(frontier)
        elif method == "BFS":
            current = frontier.popleft()
        else:
            current = frontier.pop()

        visited.append(current)

        if current == goal:
            break

        neighbors = maze.get_neighbors(current)
        if method == "DFS":
            neighbors = list(reversed(neighbors))

        for neighbor in neighbors:
            new_cost = costs[current] + 1

            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parent[neighbor] = current

                if priority_mode:
                    heuristic = (
                        abs(neighbor[0] - goal[0])
                        + abs(neighbor[1] - goal[1])
                    )
                    heapq.heappush(
                        frontier, (new_cost + heuristic, neighbor)
                    )
                elif method == "BFS":
                    frontier.append(neighbor)
                else:
                    frontier.append(neighbor)

    path = []
    if goal in parent:
        current = goal
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()

    return {
        "path": path,
        "path_length": max(0, len(path) - 1),
        "nodes_expanded": len(visited),
        "visited_order": visited,
        "success": bool(path),
    }


def dfs(maze):
    return _search(maze, "DFS")


def astar(maze):
    return _search(maze, "A*")
def reactive_astar(maze):
    """
    Reactive A* navigation using partial observation.

    The robot initially knows only its current cell.
    It discovers obstacles when attempting to move into them
    and replans using A*.
    """

    import heapq

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

    replan_count = 0
    plan_count = 0
    nodes_expanded = 0
    obstacles_discovered = 0
    actual_distance = 0

    directions = maze.DIRECTIONS

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def plan_path(position):
        nonlocal nodes_expanded

        open_list = []
        heapq.heappush(
            open_list,
            (heuristic(position, goal), 0, position)
        )

        came_from = {}
        g_score = {position: 0}

        while open_list:
            _, current_g, current = heapq.heappop(open_list)

            if current_g != g_score.get(current):
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
                new_g = current_g + 1

                if new_g < g_score.get(neighbour, float("inf")):
                    g_score[neighbour] = new_g
                    came_from[neighbour] = current

                    f = new_g + heuristic(neighbour, goal)

                    heapq.heappush(
                        open_list,
                        (f, new_g, neighbour)
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

            # Check the actual maze only when attempting to enter.
            if maze.grid[r][c] == WALL:

                if discovered_map[r][c] != WALL:
                    discovered_map[r][c] = WALL
                    obstacles_discovered += 1

                replan_count += 1
                path_blocked = True
                break

            # Successfully move into the cell.
            discovered_map[r][c] = FREE
            robot_position = next_cell
            actual_distance += 1

            if robot_position == goal:
                break

        if not path_blocked and robot_position != goal:
            break


    return {
        "success": robot_position == goal,
        "path_length": actual_distance,
        "actual_distance": actual_distance,
        "nodes_expanded": nodes_expanded,
        "replan_count": replan_count,
        "plan_count": plan_count,
        "obstacles_discovered": obstacles_discovered,
        "final_position": robot_position,
    }
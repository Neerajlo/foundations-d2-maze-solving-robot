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
from collections import deque


def bfs(maze):
    start, goal = maze.start, maze.goal
    queue = deque([start])
    parent = {start: None}
    visited = []

    while queue:
        current = queue.popleft()
        visited.append(current)

        if current == goal:
            break

        for neighbor in maze.get_neighbors(current):
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)

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
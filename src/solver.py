from collections import deque
import heapq


def reconstruct_path(parent, start, goal):
    if goal not in parent:
        return []

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    if path[0] != start:
        return []

    return path


def bfs(maze):
    start = maze.start
    goal = maze.goal

    queue = deque([start])
    parent = {start: None}
    nodes_expanded = 0

    while queue:
        current = queue.popleft()
        nodes_expanded += 1

        if current == goal:
            path = reconstruct_path(parent, start, goal)
            return path, nodes_expanded

        for neighbor in maze.get_neighbors(current):
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)

    return [], nodes_expanded


def dfs(maze):
    start = maze.start
    goal = maze.goal

    stack = [start]
    parent = {start: None}
    nodes_expanded = 0

    while stack:
        current = stack.pop()
        nodes_expanded += 1

        if current == goal:
            path = reconstruct_path(parent, start, goal)
            return path, nodes_expanded

        for neighbor in reversed(maze.get_neighbors(current)):
            if neighbor not in parent:
                parent[neighbor] = current
                stack.append(neighbor)

    return [], nodes_expanded


def heuristic(position, goal):
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])


def astar(maze):
    start = maze.start
    goal = maze.goal

    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    parent = {start: None}
    cost_so_far = {start: 0}
    nodes_expanded = 0

    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        nodes_expanded += 1

        if current == goal:
            path = reconstruct_path(parent, start, goal)
            return path, nodes_expanded

        for neighbor in maze.get_neighbors(current):
            new_cost = cost_so_far[current] + 1

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost

                priority = new_cost + heuristic(neighbor, goal)

                heapq.heappush(
                    priority_queue,
                    (priority, neighbor)
                )

                parent[neighbor] = current

    return [], nodes_expanded
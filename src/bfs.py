from collections import deque


def reconstruct_path(parent, start, goal):
  

    path = []
    current = goal

    while current is not None:
        path.append(current)

        if current == start:
            break

        current = parent.get(current)

    # If start was never reached, there is no path.
    if path[-1] != start:
        return []

    path.reverse()

    return path


def bfs(maze):
  
    start = maze.start
    goal = maze.goal

    # Queue for BFS.
    queue = deque([start])

    # Keep track of visited cells.
    visited = {start}

    # Store how we reached each cell.
    parent = {
        start: None
    }

    # Store the order in which cells were explored.
    visited_order = []

    # BFS search.
    while queue:

        current = queue.popleft()

        # Record this cell as expanded.
        visited_order.append(current)

        # Check whether we reached the goal.
        if current == goal:
            break

        # Explore all reachable neighboring cells.
        for neighbor in maze.get_neighbors(current):

            if neighbor not in visited:

                visited.add(neighbor)

                parent[neighbor] = current

                queue.append(neighbor)

    # Reconstruct the final path.
    path = reconstruct_path(
        parent,
        start,
        goal
    )

    # Determine whether a solution was found.
    success = len(path) > 0

    # Number of movements between cells.
    path_length = len(path) - 1 if success else 0

    return {
        "path": path,
        "path_length": path_length,
        "nodes_expanded": len(visited_order),
        "visited_order": visited_order,
        "success": success
    }
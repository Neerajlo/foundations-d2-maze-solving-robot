from maze_generator import generate_maze
from bfs import bfs


# Generate a 10 x 10 maze.
maze = generate_maze(
    rows=10,
    cols=10,
    seed=42
)


# Run BFS.
result = bfs(maze)


print(" BFS RESULT ")

print("Maze size:", maze.rows, "x", maze.cols)
print("Start:", maze.start)
print("Goal:", maze.goal)

print("Success:", result["success"])
print("Path length:", result["path_length"])
print("Nodes expanded:", result["nodes_expanded"])

print("\nPath:")
print(result["path"])

print("\nVisited cells:")
print(result["visited_order"])
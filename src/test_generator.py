from maze_generator import generate_maze
from maze_visualizer import display_maze


maze = generate_maze(
    rows=10,
    cols=10,
    seed=42
)

print("Maze size:", maze.rows, "x", maze.cols)
print("Start:", maze.start)
print("Goal:", maze.goal)

display_maze(maze)
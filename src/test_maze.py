from maze_generator import generate_maze


maze = generate_maze(
    rows=5,
    cols=5,
    seed=42
)

print("Maze size:", maze.rows, "x", maze.cols)
print("Start:", maze.start)
print("Goal:", maze.goal)

print("\nNeighbors of start:")
print(maze.get_neighbors(maze.start))

print("\nNeighbors of goal:")
print(maze.get_neighbors(maze.goal))

print("\nChecking all cells:")

for row in range(maze.rows):
    for col in range(maze.cols):
        cell = (row, col)
        print(cell, "->", maze.get_neighbors(cell))
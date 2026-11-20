
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from src.maze import Maze
from src.maze_generator import generate_maze
from src.bfs import bfs
from src.solver import dfs, astar


# Generate a reproducible 10x10 maze.
ROWS = 10
COLS = 10
SEED = 42

grid = generate_maze(ROWS, COLS, seed=SEED)

maze = Maze(
    grid,
    start=(0, 0),
    goal=(ROWS - 1, COLS - 1)
)


# Algorithms to compare.
algorithms = [
    ("BFS", bfs),
    ("DFS", dfs),
    ("A*", astar)
]

results = []

for name, algorithm in algorithms:
    result = algorithm(maze)
    results.append((name, result))

    print("\nAlgorithm:", name)
    print("Success:", result["success"])
    print("Path length:", result["path_length"])
    print("Nodes expanded:", result["nodes_expanded"])


# Create three visualizations side by side.
fig, axes = plt.subplots(1, 3, figsize=(17, 6))

for ax, (name, result) in zip(axes, results):

    # Draw the maze cells.
    for row in range(ROWS):
        for col in range(COLS):

            y = ROWS - row - 1

            if grid[row][col] == 1:
                cell_color = "black"
            else:
                cell_color = "white"

            ax.add_patch(
                Rectangle(
                    (col, y),
                    1,
                    1,
                    facecolor=cell_color,
                    edgecolor="lightgray"
                )
            )

    # Draw explored cells.
    for row, col in result["visited_order"]:
        y = ROWS - row - 1

        if (row, col) not in (maze.start, maze.goal):
            ax.add_patch(
                Rectangle(
                    (col, y),
                    1,
                    1,
                    facecolor="lightblue",
                    edgecolor="none",
                    alpha=0.45
                )
            )

    # Draw the final solution path.
    path = result["path"]

    if path:
        x_values = [col + 0.5 for row, col in path]
        y_values = [ROWS - row - 0.5 for row, col in path]

        ax.plot(
            x_values,
            y_values,
            color="red",
            linewidth=2.5,
            marker="o",
            markersize=3,
            label="Solution Path"
        )

    # Mark start and goal.
    ax.scatter(
        0.5,
        ROWS - 0.5,
        color="green",
        s=120,
        marker="o",
        label="Start",
        zorder=5
    )

    ax.scatter(
        COLS - 0.5,
        0.5,
        color="orange",
        s=120,
        marker="s",
        label="Goal",
        zorder=5
    )

    ax.set_xlim(0, COLS)
    ax.set_ylim(0, ROWS)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])

    ax.set_title(
        f"{name}\nPath: {result['path_length']} | "
        f"Expanded: {result['nodes_expanded']}"
    )

    ax.legend(loc="upper right", fontsize=8)


fig.suptitle(
    f"Maze Algorithm Comparison ({ROWS}x{COLS}, Seed={SEED})",
    fontsize=16
)

plt.tight_layout()
plt.show()

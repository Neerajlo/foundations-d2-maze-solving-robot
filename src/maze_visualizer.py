import matplotlib.pyplot as plt


# Colors used for the maze walls.
WALL_COLORS = [
    "red",
    "blue",
    "green",
    "orange",
    "purple",
    "brown",
    "magenta",
    "cyan",
    "gold",
]


def display_maze(maze):
    """
    Display a cell-based maze.

    Light gray lines = cell grid
    Colored lines = actual maze walls
    Blue circle = start
    Orange square = goal
    """

    fig, ax = plt.subplots(figsize=(8, 8))


    for x in range(maze.cols + 1):
        ax.plot(
            [x, x],
            [0, maze.rows],
            color="lightgray",
            linewidth=0.8,
            zorder=1
        )

    for y in range(maze.rows + 1):
        ax.plot(
            [0, maze.cols],
            [y, y],
            color="lightgray",
            linewidth=0.8,
            zorder=1
        )


    wall_index = 0

    for row in range(maze.rows):
        for col in range(maze.cols):

            cell = (row, col)
            cell_walls = maze.walls[cell]

            bottom = maze.rows - row - 1
            top = maze.rows - row

            # Pick a color for this wall.
            wall_color = WALL_COLORS[wall_index % len(WALL_COLORS)]
            wall_index += 1

            # Top wall
            if cell_walls["UP"]:
                ax.plot(
                    [col, col + 1],
                    [top, top],
                    color=wall_color,
                    linewidth=3,
                    solid_capstyle="round",
                    zorder=2
                )

            # Right wall
            if cell_walls["RIGHT"]:
                ax.plot(
                    [col + 1, col + 1],
                    [bottom, top],
                    color=wall_color,
                    linewidth=3,
                    solid_capstyle="round",
                    zorder=2
                )

            # Bottom wall
            if cell_walls["DOWN"]:
                ax.plot(
                    [col, col + 1],
                    [bottom, bottom],
                    color=wall_color,
                    linewidth=3,
                    solid_capstyle="round",
                    zorder=2
                )

            # Left wall
            if cell_walls["LEFT"]:
                ax.plot(
                    [col, col],
                    [bottom, top],
                    color=wall_color,
                    linewidth=3,
                    solid_capstyle="round",
                    zorder=2
                )

    start_row, start_col = maze.start

    ax.scatter(
        start_col + 0.5,
        maze.rows - start_row - 0.5,
        s=300,
        marker="o",
        zorder=4,
        label="Start"
    )

    goal_row, goal_col = maze.goal

    ax.scatter(
        goal_col + 0.5,
        maze.rows - goal_row - 0.5,
        s=300,
        marker="s",
        zorder=4,
        label="Goal"
    )

   

    ax.set_xlim(0, maze.cols)
    ax.set_ylim(0, maze.rows)

    ax.set_aspect("equal")

    ax.set_xticks([])
    ax.set_yticks([])

    ax.set_title(
        "Generated Maze",
        fontsize=18
    )

    ax.legend(
        loc="upper right",
        frameon=True
    )

    plt.tight_layout()
    plt.show()
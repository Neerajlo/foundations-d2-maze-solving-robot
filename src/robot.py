
class Robot:
    """
    Robot that explores a maze without initially
    knowing the complete obstacle layout.
    """

    def __init__(self, actual_maze):
        self.actual_maze = actual_maze

        self.position = actual_maze.start
        self.goal = actual_maze.goal

        # -1 = Unknown, 0 = Open, 1 = Obstacle
        self.known_grid = [
            [-1 for _ in range(actual_maze.cols)]
            for _ in range(actual_maze.rows)
        ]

        # Initially, the robot knows only its starting cell.
        row, col = self.position
        self.known_grid[row][col] = 0

        self.discovered_obstacles = []
        self.path_history = [self.position]

    def observe(self, cell):
        """
        Discover whether the attempted cell is open or blocked.
        Update the robot's known map.
        """

        row, col = cell

        if not (
            0 <= row < self.actual_maze.rows
            and 0 <= col < self.actual_maze.cols
        ):
            return False

        if self.actual_maze.grid[row][col] == 1:
            self.known_grid[row][col] = 1

            if cell not in self.discovered_obstacles:
                self.discovered_obstacles.append(cell)

            return False

        self.known_grid[row][col] = 0
        return True

    def move(self, next_cell):
        """Move one cell if it is open."""

        row, col = next_cell

        distance = (
            abs(row - self.position[0])
            + abs(col - self.position[1])
        )

        if distance != 1:
            raise ValueError(
                "Robot can move only one cell at a time."
            )

        if not self.observe(next_cell):
            return False

        self.position = next_cell
        self.path_history.append(next_cell)

        return True

    def get_planning_maze(self):
        """
        Create a separate planning maze using
        only the robot's known information.

        Unknown cells are temporarily treated as open.
        """

        planning_grid = [
            [
                1 if cell == 1 else 0
                for cell in row
            ]
            for row in self.known_grid
        ]

        from src.maze import Maze

        return Maze(
            planning_grid,
            start=self.position,
            goal=self.goal
        )

    def reached_goal(self):
        return self.position == self.goal

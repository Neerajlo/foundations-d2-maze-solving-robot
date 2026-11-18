

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

def wall_following(maze, hand="left", max_steps=10000):
    """
    Grid-based wall-following algorithm.
    Returns path and performance information.
    """

    start = maze.start
    goal = maze.goal

    # Direction order: Up, Right, Down, Left
    directions = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]

    position = start
    direction = 1  # Initially facing right

    path = [position]
    visited_states = set()
    nodes_expanded = 0

    for _ in range(max_steps):
        if position == goal:
            break

        state = (position, direction)

        if state in visited_states:
            break

        visited_states.add(state)
        nodes_expanded += 1

        # Try left/right hand preference first
        if hand == "left":
            turns = [-1, 0, 1, 2]
        else:
            turns = [1, 0, -1, 2]

        moved = False

        for turn in turns:
            next_direction = (direction + turn) % 4

            dr, dc = directions[next_direction]
            next_position = (
                position[0] + dr,
                position[1] + dc
            )

            if maze.is_valid(next_position):
                position = next_position
                direction = next_direction
                path.append(position)
                moved = True
                break

        if not moved:
            break

    success = position == goal

    return {
        "path": path,
        "path_length": max(0, len(path) - 1),
        "nodes_expanded": nodes_expanded,
        "visited_order": path,
        "success": success
    }
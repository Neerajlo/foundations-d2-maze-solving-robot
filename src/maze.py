class Maze:
    """
    Represents a cell-based maze.

    Each cell has four possible walls:
    top, right, bottom, left.

    False = no wall
    True  = wall
    """

    DIRECTIONS = {
        "UP": (-1, 0),
        "RIGHT": (0, 1),
        "DOWN": (1, 0),
        "LEFT": (0, -1)
    }

    def __init__(self, rows, cols, start, goal, walls):
        self.rows = rows
        self.cols = cols
        self.start = start
        self.goal = goal
        self.walls = walls

    def is_valid(self, position):
        """Check whether a cell is inside the maze."""
        row, col = position

        return (
            0 <= row < self.rows
            and 0 <= col < self.cols
        )

    def get_neighbors(self, position):

        row, col = position
        neighbors = []

        direction_names = ["UP", "RIGHT", "DOWN", "LEFT"]

        for direction in direction_names:

            dr, dc = self.DIRECTIONS[direction]

            neighbor = (row + dr, col + dc)

            if not self.is_valid(neighbor):
                continue

            if not self.walls[position][direction]:
                neighbors.append(neighbor)

        return neighbors
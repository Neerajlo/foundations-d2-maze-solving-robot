import json


class Maze:
    def __init__(self, grid, start=(0, 0), goal=None):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        self.start = start

        if goal is None:
            self.goal = (self.rows - 1, self.cols - 1)
        else:
            self.goal = goal

    @classmethod
    def from_json(cls, file_path):
        with open(file_path, "r") as f:
            grid = json.load(f)

        return cls(grid)

    def is_valid(self, position):
        row, col = position

        return (
            0 <= row < self.rows
            and 0 <= col < self.cols
            and self.grid[row][col] == 0
        )

    def get_neighbors(self, position):
        row, col = position

        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1),   # Right
        ]

        neighbors = []

        for dr, dc in directions:
            next_position = (row + dr, col + dc)

            if self.is_valid(next_position):
                neighbors.append(next_position)

        return neighbors

    def is_goal(self, position):
        return position == self.goal

    def display(self):
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))
import json
from pathlib import Path


class Maze:
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def __init__(self, grid, start=(0, 0), goal=None):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        self.start = tuple(start)
        self.goal = tuple(goal) if goal is not None else (
            self.rows - 1, self.cols - 1
        )

    @classmethod
    def from_json(cls, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return cls(data)

        return cls(
            data["grid"],
            data.get("start", (0, 0)),
            data.get("goal")
        )

    def is_valid(self, position):
        row, col = position
        return (
            0 <= row < self.rows
            and 0 <= col < self.cols
            and self.grid[row][col] == 0
        )

    def get_neighbors(self, position):
        row, col = position
        neighbors = []

        for dr, dc in self.DIRECTIONS:
            next_position = (row + dr, col + dc)

            if self.is_valid(next_position):
                neighbors.append(next_position)

        return neighbors

    def is_goal(self, position):
        return position == self.goal

    def display(self):
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))

import heapq
import itertools
import math


class DStarLite:
    """
    D* Lite pathfinding algorithm.

    Calculates a path from start to goal and reuses previous
    search information when obstacles are discovered.
    """

    def __init__(self, maze, start=None, goal=None):
        self.maze = maze
        self.start = tuple(start if start is not None else maze.start)
        self.goal = tuple(goal if goal is not None else maze.goal)

        self.km = 0
        self.last_start = self.start

        self.g = {}
        self.rhs = {}

        self.open_list = []
        self.entry_versions = {}
        self.counter = itertools.count()

        # Cumulative measurements
        self.nodes_expanded = 0
        self.replan_count = 0

        for row in range(maze.rows):
            for col in range(maze.cols):
                cell = (row, col)
                self.g[cell] = math.inf
                self.rhs[cell] = math.inf

        # The goal is the target of the backward search.
        if self.maze.is_valid(self.goal):
            self.rhs[self.goal] = 0
            self._push(self.goal)

    def heuristic(self, a, b):
        """Manhattan distance for four-direction movement."""
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def _key(self, cell):
        minimum = min(self.g[cell], self.rhs[cell])

        return (
            minimum + self.heuristic(self.start, cell) + self.km,
            minimum
        )

    def _cost(self, a, b):
        """Return movement cost, or infinity if movement is impossible."""
        if not self.maze.is_valid(a) or not self.maze.is_valid(b):
            return math.inf

        return 1

    def _neighbors(self, cell):
        """Return valid four-direction neighbours."""
        row, col = cell
        result = []

        for dr, dc in self.maze.DIRECTIONS:
            neighbor = (row + dr, col + dc)

            if self.maze.is_valid(neighbor):
                result.append(neighbor)

        return result

    def _push(self, cell):
        """Insert a new version of a cell into the priority queue."""
        version = self.entry_versions.get(cell, 0) + 1
        self.entry_versions[cell] = version

        heapq.heappush(
            self.open_list,
            (
                self._key(cell),
                next(self.counter),
                cell,
                version
            )
        )

    def _top_key(self):
        """Return the smallest valid priority."""
        while self.open_list:
            key, _, cell, version = self.open_list[0]

            if self.entry_versions.get(cell) != version:
                heapq.heappop(self.open_list)
                continue

            return key

        return (math.inf, math.inf)

    def _pop(self):
        """Remove and return the smallest valid queue entry."""
        while self.open_list:
            key, _, cell, version = heapq.heappop(self.open_list)

            if self.entry_versions.get(cell) == version:
                return key, cell

        return (math.inf, math.inf), None

    def _update_vertex(self, cell):
        """Update the one-step lookahead value of a cell."""

        if cell == self.goal:
            self.rhs[cell] = (
                0 if self.maze.is_valid(cell) else math.inf
            )

        elif not self.maze.is_valid(cell):
            self.rhs[cell] = math.inf

        else:
            self.rhs[cell] = min(
                (
                    self._cost(cell, neighbor) + self.g[neighbor]
                    for neighbor in self._neighbors(cell)
                ),
                default=math.inf
            )

        # Invalidate old queue entries.
        self.entry_versions[cell] = (
            self.entry_versions.get(cell, 0) + 1
        )

        # Only inconsistent cells belong in the queue.
        if self.g[cell] != self.rhs[cell]:
            self._push(cell)

    def compute_shortest_path(self):
        """Update the search until the start has a consistent path."""

        while (
            self._top_key() < self._key(self.start)
            or self.rhs[self.start] != self.g[self.start]
        ):
            old_key, current = self._pop()

            if current is None:
                break

            new_key = self._key(current)
            self.nodes_expanded += 1

            if old_key < new_key:
                self._push(current)

            elif self.g[current] > self.rhs[current]:
                self.g[current] = self.rhs[current]

                for neighbor in self._neighbors(current):
                    self._update_vertex(neighbor)

            else:
                self.g[current] = math.inf
                self._update_vertex(current)

                for neighbor in self._neighbors(current):
                    self._update_vertex(neighbor)

    def plan(self):
        """Calculate and return the current path."""

        previous_expansions = self.nodes_expanded

        self.compute_shortest_path()

        expansions_this_call = (
            self.nodes_expanded - previous_expansions
        )

        # Handle blocked start or goal.
        if (
            not self.maze.is_valid(self.start)
            or not self.maze.is_valid(self.goal)
            or math.isinf(self.g[self.start])
        ):
            return {
                "path": [],
                "success": False,
                "path_length": 0,
                "nodes_expanded": self.nodes_expanded,
                "nodes_expanded_this_call": expansions_this_call,
                "replan_count": self.replan_count
            }

        path = [self.start]
        current = self.start
        visited = {current}

        while current != self.goal:

            candidates = [
                (
                    self._cost(current, neighbor) + self.g[neighbor],
                    neighbor
                )
                for neighbor in self._neighbors(current)
            ]

            if not candidates:
                break

            best_cost, next_cell = min(candidates)

            if math.isinf(best_cost) or next_cell in visited:
                break

            current = next_cell
            path.append(current)
            visited.add(current)

        success = current == self.goal

        return {
            "path": path if success else [],
            "success": success,
            "path_length": len(path) - 1 if success else 0,
            "nodes_expanded": self.nodes_expanded,
            "nodes_expanded_this_call": expansions_this_call,
            "replan_count": self.replan_count
        }

    def move_start(self, new_start):
        """Move the robot's current position and update the heuristic."""

        new_start = tuple(new_start)

        if not (
            0 <= new_start[0] < self.maze.rows
            and 0 <= new_start[1] < self.maze.cols
        ):
            raise ValueError("New start is outside the maze.")

        self.km += self.heuristic(self.last_start, new_start)
        self.start = new_start
        self.last_start = new_start

    def update_obstacle(self, cell, blocked=True):
        """
        Update the maze after discovering an obstacle.

        Reuses the previous g and rhs values and repairs
        only the affected part of the search.
        """

        cell = tuple(cell)

        if not (
            0 <= cell[0] < self.maze.rows
            and 0 <= cell[1] < self.maze.cols
        ):
            raise ValueError("Obstacle is outside the maze.")

        new_value = 1 if blocked else 0
        old_value = self.maze.grid[cell[0]][cell[1]]

        # Avoid unnecessary replanning if nothing changed.
        if old_value == new_value:
            return self.plan()

        self.maze.grid[cell[0]][cell[1]] = new_value

        self.replan_count += 1

        # The changed cell and its neighbours may be affected.
        affected = [cell] + [
            (cell[0] + dr, cell[1] + dc)
            for dr, dc in self.maze.DIRECTIONS
        ]

        for position in affected:
            if (
                0 <= position[0] < self.maze.rows
                and 0 <= position[1] < self.maze.cols
            ):
                self._update_vertex(position)

        return self.plan()

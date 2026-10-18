from src.maze import Maze
from src.bfs import bfs


def create_test_maze(walls=None):
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    if walls:
        for row, col in walls:
            grid[row][col] = 1

    return Maze(grid, start=(0, 0), goal=(2, 2))


def test_bfs_finds_path():
    maze = create_test_maze()
    result = bfs(maze)

    assert result["success"] is True
    assert result["path"][0] == (0, 0)
    assert result["path"][-1] == (2, 2)


def test_bfs_handles_blocked_goal():
    maze = create_test_maze(walls={(2, 2)})
    result = bfs(maze)

    assert result["success"] is False
    assert result["path"] == []
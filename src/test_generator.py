from src.maze_generator import generate_maze


def test_generate_maze_returns_maze():
    maze = generate_maze(10, 10, seed=42)

    assert isinstance(maze, list)
    assert len(maze) == 10
    assert all(len(row) == 10 for row in maze)


def test_generate_maze_has_valid_start_and_goal():
    maze = generate_maze(10, 10, seed=42)

    assert maze[0][0] == 0
    assert maze[9][9] == 0
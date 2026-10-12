from src.maze import Maze


def create_test_maze():
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    return Maze(grid, start=(0, 0), goal=(2, 2))


def test_maze_initialization():
    maze = create_test_maze()

    assert maze.rows == 3
    assert maze.cols == 3
    assert maze.start == (0, 0)
    assert maze.goal == (2, 2)


def test_valid_position():
    maze = create_test_maze()

    assert maze.is_valid((0, 0))
    assert maze.is_valid((2, 2))


def test_wall_blocks_position():
    maze = create_test_maze()

    assert not maze.is_valid((1, 1))


def test_get_neighbors():
    maze = create_test_maze()
    neighbors = maze.get_neighbors((0, 0))

    assert (0, 1) in neighbors
    assert (1, 0) in neighbors
    assert len(neighbors) == 2


def test_goal_detection():
    maze = create_test_maze()

    assert maze.is_goal((2, 2))
    assert not maze.is_goal((0, 0))
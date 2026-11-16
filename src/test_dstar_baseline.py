
import time
import tracemalloc
from pathlib import Path

from src.maze import Maze
from src.dstar_lite import DStarLite
from src.bfs import bfs


def measure(algorithm):
    tracemalloc.start()
    start_time = time.perf_counter()

    result = algorithm()

    runtime = time.perf_counter() - start_time
    current_memory, peak_memory = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return result, runtime, peak_memory / 1024


for maze_file in sorted(Path("data/raw").glob("*.json")):

    maze = Maze.from_json(maze_file)

    dstar = DStarLite(maze)
    dstar_result, dstar_time, dstar_memory = measure(dstar.plan)

    bfs_result, bfs_time, bfs_memory = measure(lambda: bfs(maze))

    print("\nMaze:", maze_file.stem)

    print(
        f"D* Lite: nodes={dstar_result['nodes_expanded']}, "
        f"path={dstar_result['path_length']}, "
        f"time={dstar_time:.6f}s, "
        f"memory={dstar_memory:.2f} KB"
    )

    print(
        f"BFS: nodes={bfs_result['nodes_expanded']}, "
        f"path={bfs_result['path_length']}, "
        f"time={bfs_time:.6f}s, "
        f"memory={bfs_memory:.2f} KB"
    )

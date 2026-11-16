
from pathlib import Path

from src.maze import Maze
from src.dstar_lite import DStarLite
from src.bfs import bfs


for maze_file in sorted(Path("data/raw").glob("*.json")):

    maze = Maze.from_json(maze_file)

    planner = DStarLite(maze)
    initial = planner.plan()

    if not initial["success"] or len(initial["path"]) <= 2:
        print(maze_file.stem, "Initial path not found")
        continue

    blocked_cell = initial["path"][1]

    dstar_result = planner.update_obstacle(blocked_cell)
    bfs_result = bfs(maze)

    print("\nMaze:", maze_file.stem)
    print("Blocked cell:", blocked_cell)
    print("D* Lite path length:", dstar_result["path_length"])
    print("BFS path length:", bfs_result["path_length"])
    print("D* Lite success:", dstar_result["success"])
    print("BFS success:", bfs_result["success"])
    print("Replan count:", dstar_result["replan_count"])

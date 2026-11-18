# Wall Following Algorithm – Maze-Solving Robot

## 1. Introduction

The Wall Following Algorithm is a maze-navigation technique in which a robot follows a wall while moving through a maze. In this project, the left-hand wall-following strategy is implemented and evaluated against Breadth-First Search (BFS).

The objective is to study the algorithm's ability to navigate different maze sizes and compare its performance with BFS.

## 2. Algorithm Overview

The implemented Wall Following algorithm uses the following navigation strategy:

1. Load the maze and identify the starting and goal positions.
2. Initialize the robot's direction and position.
3. Check available neighbouring cells.
4. Follow the selected wall while navigating through the maze.
5. Continue moving until the goal is reached or no valid movement is possible.
6. Record the resulting path, path length, and nodes explored.

**Note:** The implementation should be understood according to the actual movement and direction-handling logic in `src/robot.py`.

## 3. Implementation

The algorithm is implemented in:

`src/robot.py`

The implementation is tested using the project's existing maze representation and generated maze files.

The comparison script is:

`compare_wall_following.py`

This script executes BFS and Wall Following on the available maze files and compares their results.

## 4. Experimental Methodology

The experiment uses nine generated maze files:

| Maze category | Maze IDs | Count |
|---|---|---:|
| Small | small_42 to small_44 | 3 |
| Medium | medium_42 to medium_44 | 3 |
| Large | large_42 to large_44 | 3 |
| **Total** | | **9** |

Two algorithms are evaluated on each maze:

- Breadth-First Search (BFS)
- Wall Following

The experiment records:
- Algorithm success status
- Path length
- Nodes expanded

A total of 18 algorithm runs are recorded.

## 5. Experimental Results

The comparison produced the following observations:

| Maze | BFS Path | Wall Following Path |
|---|---:|---:|
| large_42 | 58 | 168 |
| large_43 | 58 | 108 |
| large_44 | 58 | 176 |
| medium_42 | 38 | 80 |
| medium_43 | 38 | 74 |
| medium_44 | 38 | 98 |
| small_42 | 18 | 36 |
| small_43 | 18 | 36 |
| small_44 | 18 | 42 |

All 18 algorithm runs reported successful navigation in the tested mazes.

## 6. BFS vs Wall Following

The observed results show that BFS produced shorter paths than Wall Following in all nine tested mazes.

Wall Following successfully reached the goal in these test cases, but its paths were longer.

BFS is a systematic search algorithm that explores the maze level by level. Wall Following uses a local navigation strategy and does not guarantee the shortest path.

These observations apply only to the generated mazes used in this experiment.

## 7. Output File

The comparison results are saved in:

`results/wall_following_comparison.csv`

The CSV contains 18 records covering both algorithms across all nine maze files.

## 8. Limitations

- Results are based on the currently generated maze dataset.
- The experiment does not establish performance on every possible maze structure.
- Runtime and memory comparisons are not included in this particular comparison output.
- Wall Following performance depends on maze structure and the implemented movement strategy.

## 9. Conclusion

The Wall Following Algorithm was successfully implemented and tested on nine generated mazes.

The experiment recorded successful navigation for all tested cases. However, BFS generated shorter paths in each of the nine comparisons.

This comparison demonstrates the difference between local wall-following navigation and systematic graph-search-based pathfinding.

## 10. Reproducibility

Run the comparison from the repository root:

```powershell
python .\compare_wall_following.py
```

The output CSV is generated at:

`results/wall_following_comparison.csv`
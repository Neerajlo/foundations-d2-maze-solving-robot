
# Maze Algorithm Experiment Results

## Overview

This folder contains the output of the maze-solving algorithm experiments. The current experiment compares Breadth-First Search (BFS), Depth-First Search (DFS), and A* on small, medium, and large mazes.

## Output File

`maze_results.csv` contains one record for each algorithm run.

### Column Definitions

| Column | Meaning | Unit or Format |
|---|---|---|
| `maze_id` | Identifier of the input maze | Text |
| `algorithm` | Algorithm used: BFS, DFS, or A* | Text |
| `path_length` | Number of steps in the returned path, as reported by the solver | Steps |
| `nodes_expanded` | Number of nodes expanded by the solver | Nodes |
| `runtime_seconds` | Measured execution time | Seconds |
| `peak_memory_kb` | Peak Python memory traced during the algorithm run using `tracemalloc` | KB (1024 bytes) |
| `replan_count` | Number of replanning events recorded by the program | Count |
| `path_found` | Whether the solver found a path | Boolean (`True`/`False`) |

## How to Reproduce

Run these commands from the repository root in a Python environment with the required dependencies installed:

```powershell
python -m src.main
```

The program reads maze JSON files from `data/raw/`, runs BFS, DFS, and A* on each maze, and writes the results to `results/maze_results.csv`.

The output file is overwritten each time the command runs.

## Experimental Setup

- Input mazes: JSON files stored in `data/raw/`.
- Maze groups: small, medium, and large.
- Seeds represented in the current dataset: 42, 43, and 44.
- Algorithms: BFS, DFS, and A*.
- Metrics: path length, nodes expanded, runtime, and peak traced Python memory.
- Current dataset: 9 maze files and 27 algorithm result records.

## Measurement Assumptions and Limitations

- Runtime is measured using Python's `time.perf_counter()`. It may vary between runs because of machine load and other execution conditions.
- Memory is measured using `tracemalloc`. It represents traced Python memory, not total process memory or total computer RAM.
- `replan_count` is currently recorded as zero by the program; it does not mean replanning behavior has been experimentally evaluated.
- Results describe the current implementation and input mazes. They should not be treated as universal performance guarantees.
- The experiment log in the repository root, `experiments.csv`, records selected experiment runs and their main metrics.

## Week 5 — Sample Output Format

`sample_output.csv` is a dummy file created to demonstrate the agreed output columns. Its values are illustrative only and are not actual experiment results.

Columns:
- `maze_id`: identifier for the maze
- `algorithm`: algorithm used
- `path_length`: number of steps in the path
- `nodes_expanded`: number of nodes explored
- `runtime_seconds`: execution time in seconds
- `peak_memory_kb`: measured peak memory in KB
- `replan_count`: number of replanning events
- `path_found`: whether a path was found

## Week 5 – Member 2 Navigation Output Format

The file `member2_navigation_output.csv` defines the output format for Member 2's Autonomous Navigation and Replanning experiments.

The file currently contains five illustrative dummy records. These values demonstrate the agreed structure and are not actual experimental measurements.

### Output Columns

- `run_id`: Unique experiment run identifier.
- `maze_id`: Identifier of the maze being tested.
- `algorithm`: Navigation algorithm used.
- `start_x`, `start_y`: Starting coordinates of the robot.
- `goal_x`, `goal_y`: Goal coordinates.
- `path_found`: Indicates whether a valid path was found.
- `path_length`: Length of the planned path.
- `nodes_expanded`: Number of nodes explored during path planning.
- `runtime_seconds`: Execution time in seconds.
- `peak_memory_kb`: Peak memory usage in KB.
- `obstacles_discovered`: Number of previously unknown obstacles discovered.
- `replan_count`: Number of replanning operations.
- `actual_distance`: Actual distance travelled by the robot.
- `navigation_success`: Indicates whether the robot successfully reached its goal.

Actual experimental measurements will replace the dummy values when navigation experiments are conducted.
# Maze Algorithm Experiment Results

## Overview

This folder contains the output of the maze-solving algorithm experiments. The current experiment compares Breadth-First Search (BFS), Depth-First Search (DFS), A*, and Reactive A* on small, medium, and large mazes.

## Output File

`maze_results.csv` contains one record for each algorithm run.

### Column Definitions

| Column | Meaning | Unit or Format |
|---|---|---|
| `maze_id` | Identifier of the input maze | Text |
| `algorithm` | Algorithm used: BFS, DFS, A*, or Reactive A* | Text |
| `path_length` | Number of steps in the returned path, as reported by the solver | Steps |
| `nodes_expanded` | Number of nodes expanded by the solver | Nodes |
| `runtime_seconds` | Measured execution time | Seconds |
| `peak_memory_kb` | Peak Python memory traced during the algorithm run using `tracemalloc` | KB (1024 bytes) |
| `replan_count` | Number of replanning events recorded by the program | Count |
| `obstacles_discovered` | Number of previously unknown obstacles discovered by Reactive A* | Count |
| `actual_distance` | Actual distance travelled by the robot | Steps |
| `plan_count` | Total number of path-planning operations performed | Count |
| `path_found` | Whether the solver successfully reached the goal | Boolean (`True`/`False`) |

## How to Reproduce

Run these commands from the repository root in a Python environment with the required dependencies installed:

```powershell
python -m src.main
```

If using the project's virtual environment on Windows:

```powershell
.\.venv\Scripts\python.exe -m src.main
```

The program reads maze JSON files from `data/raw/`, runs BFS, DFS, A*, and Reactive A* on each maze, and writes the results to `results/maze_results.csv`.

The output file is overwritten each time the command runs.

## Experimental Setup

- Input mazes: JSON files stored in `data/raw/`.
- Maze groups: small, medium, and large.
- Seeds represented in the current dataset: 42, 43, and 44.
- Algorithms: BFS, DFS, A*, and Reactive A*.
- Metrics: path length, nodes expanded, runtime, peak traced Python memory, replanning count, obstacles discovered, and actual distance.
- Current dataset: 9 maze files and 36 algorithm result records.

## Measurement Assumptions and Limitations

- Runtime is measured using Python's `time.perf_counter()`. It may vary between runs because of machine load and other execution conditions.
- Memory is measured using `tracemalloc`. It represents traced Python memory, not total process memory or total computer RAM.
- BFS, DFS, and A* use complete maze information and do not perform online replanning.
- Reactive A* initially plans using incomplete maze information and replans when it encounters an unknown obstacle.
- Unknown cells are treated as traversable during initial planning until an obstacle is discovered.
- Results describe the current implementation and input mazes. They should not be treated as universal performance guarantees.
- The experiment log in the repository root, `experiments.csv`, records selected experiment runs and their main metrics.

## Week 5 – Member 3 Algorithm Output Format

The file `member3_algorithm_output.csv` defines the output format for Member 3's Wall Following algorithm experiments.

It contains five illustrative dummy records. These values are examples only, not actual experimental measurements.

The columns record:
- Run and maze identifiers
- Algorithm and start/goal coordinates
- Path found and path length
- Nodes expanded, runtime and peak memory
- Obstacles discovered and replanning count
- Actual distance and navigation success

Actual experimental measurements will replace dummy values after testing.

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

The file contains five illustrative dummy records. These values demonstrate the agreed structure and are not actual experimental measurements.

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

The dummy records remain illustrative. Actual Week 6 navigation measurements are recorded in `maze_results.csv`.

## Week 6 – Member 2 Reactive A* Implementation and Results

Reactive A* was integrated into the main maze-solving program and tested end-to-end on all nine maze files.

Unlike the standard A* algorithm, which has complete maze information, Reactive A* initially plans using partial information. When the robot encounters an unknown obstacle, it records the obstacle and calculates a new path.

### Implementation Features

- Initial path planning using A*.
- Navigation using partially known maze information.
- Discovery of previously unknown obstacles.
- Automatic replanning when an obstacle blocks the planned path.
- Tracking of replanning operations and discovered obstacles.
- Measurement of execution time and peak memory usage.

### Experimental Results

Reactive A* successfully reached the goal in all nine test mazes.

| Maze Group | Number of Mazes | Successful Runs | Reactive A* Actual Distance |
|---|---:|---:|---|
| Small | 3 | 3/3 | 32, 20, 34 |
| Medium | 3 | 3/3 | 44, 54, 72 |
| Large | 3 | 3/3 | 82, 76, 94 |
| **Total** | **9** | **9/9** | **Average: 56.44 steps** |

### Comparison with BFS Baseline

The Week 4 BFS baseline recorded an average of 356.11 expanded nodes across nine mazes.

The Week 6 Reactive A* experiment recorded an average of 2,921.56 expanded nodes across the same nine-maze dataset.

Reactive A* expanded more nodes because it repeatedly performs path planning as new obstacles are discovered. Unlike BFS and standard A*, it operates with incomplete information and must adapt its route during navigation.

### Additional Measurements

- Navigation success rate: 100%.
- Average replanning count: 15.11.
- Average nodes expanded: 2,921.56.
- Average runtime: approximately 0.007978 seconds.
- Average peak memory: approximately 55.11 KB.
- Average actual distance travelled: 56.44 steps.

### Conclusion

The Week 6 experiment demonstrates that Reactive A* can successfully navigate all nine tested mazes while discovering obstacles and replanning routes dynamically.

The results show the trade-off between complete-information path planning and navigation under partial information. Reactive A* successfully adapts to newly discovered obstacles, although its repeated planning increases computational work compared with algorithms that know the complete maze in advance.

The experiment results are saved in `maze_results.csv`, and the selected experiment summary is recorded as Run 005 in `experiments.csv`.
## Member 1 - Multi-Algorithm Experiment Evaluation

### Objective

This experiment evaluates five maze-solving algorithms across three maze sizes using ten different random seeds. The objective is to compare path quality, computational effort, execution time, memory usage, and navigation behaviour.

### Experimental Setup

| Parameter | Configuration |
|---|---|
| Maze sizes | Small (10x10), Medium (20x20), Large (30x30) |
| Random seeds | 42 to 51 |
| Runs per algorithm and maze size | 10 |
| Total experiment records | 150 |
| Fully visible algorithms | BFS, DFS, A* |
| Partial observation algorithms | Reactive A*, D* Lite |

The fully visible scenario provides the complete maze to the search algorithm. The partial observation scenario simulates navigation when the robot initially has incomplete knowledge of the maze.

### Output Files

**1. `experiment_results.csv` - Raw Results**

Contains individual experiment records.

| Column | Meaning | Unit or Format |
|---|---|---|
| `maze_id` | Unique maze identifier | Text |
| `maze_size` | Small, medium, or large | Text |
| `rows` | Number of maze rows | Cells |
| `cols` | Number of maze columns | Cells |
| `seed` | Random seed used for generation | Integer |
| `scenario` | Fully visible or partial observation | Text |
| `algorithm` | Algorithm tested | Text |
| `success` | Whether the algorithm reached the goal | Boolean |
| `path_length` | Length of the returned or travelled path | Steps |
| `nodes_expanded` | Number of nodes expanded | Nodes |
| `runtime_seconds` | Measured execution time | Seconds |
| `peak_memory_kb` | Peak traced Python memory measured using tracemalloc | KB (1024 bytes) |
| `replan_count` | Number of recorded replanning operations | Count |
| `obstacles_discovered` | Number of previously unknown obstacles discovered | Count |
| `error` | Error information, if a run fails | Text |

**2. `experiment_summary.csv` - Statistical Summary**

Contains aggregated metrics for each scenario, maze size, and algorithm.

| Column | Meaning |
|---|---|
| `scenario` | Experiment scenario |
| `maze_size` | Maze size |
| `algorithm` | Algorithm evaluated |
| `metric` | Metric being summarized |
| `runs` | Number of observations |
| `mean` | Average metric value |
| `std_dev` | Sample standard deviation |
| `minimum` | Minimum observed value |
| `maximum` | Maximum observed value |

The summary includes success rate, path length, nodes expanded, runtime, peak memory, replanning count, and discovered obstacles.

**3. `experiment_failures.csv` - Failure Analysis**

Stores unsuccessful experiment records and their associated error information. The current experiment produced zero failure records.

### How to Reproduce

Run the following command from the repository root:

```powershell
python run_experiments.py
```

The script generates the raw results, statistical summary, and failure report in the `results/` folder. Running it again overwrites these three output files.

### Measurement Methodology

- Ten random seeds (42-51) are used for each maze size.
- Each seed is used to generate a maze for the corresponding size.
- BFS, DFS, and A* are evaluated in the fully visible scenario.
- Reactive A* and D* Lite are evaluated in the partial observation scenario.
- Execution time is measured in seconds.
- Peak Python memory is measured using `tracemalloc`.
- Mean, standard deviation, minimum, and maximum are calculated across the ten observations for each algorithm, scenario, and maze size.
- Success rate is expressed as a percentage.

### Experimental Results Overview

- Total experiment records: 150.
- Successful runs: 150.
- Unsuccessful runs: 0.
- Overall success rate: 100%.

All five algorithms successfully completed their assigned test runs across the three maze sizes.

### Measurement Assumptions and Limitations

- Runtime can vary with computer load and execution conditions.
- Each maze-seed combination has one timed run per algorithm. The standard deviation therefore describes variation across different generated mazes, not repeated timing measurements on an identical maze.
- Memory values represent traced Python allocations, not total process memory or system RAM.
- Reactive A* and D* Lite may follow different navigation paths and discover obstacles in different sequences. Their results should therefore be interpreted as observations from separate partial-observation runs, not as a perfectly controlled comparison using identical obstacle-discovery sequences.
- Results describe the current implementation and tested maze configurations; they are not universal performance guarantees.
- The experiment log in the repository root, `experiments.csv`, records this evaluation as Run 006.


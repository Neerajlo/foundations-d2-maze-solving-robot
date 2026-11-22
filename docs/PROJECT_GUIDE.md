
# Maze Solving Robot — Project Guide

## 1. Introduction

The Foundations D2 Maze Solving Robot project implements and evaluates different pathfinding and navigation algorithms using Python.

The project represents a maze as a two-dimensional grid containing free cells and obstacles. A simulated robot navigates from a starting position to a destination while avoiding obstacles.

The project explores both:

- Fully visible navigation, where the complete maze is known.
- Partial-observation navigation, where the robot initially has incomplete knowledge of the maze.

The algorithms are evaluated using performance measurements such as path length, nodes expanded, execution time, memory consumption and replanning activity.

## 2. Project Architecture

The project is organized into separate modules for maze representation, navigation, algorithms, experiments, datasets and documentation.

### Main source modules

| File | Responsibility |
|---|---|
| `src/maze.py` | Represents the maze and provides movement and validation functions. |
| `src/robot.py` | Simulates robot movement, observation and obstacle discovery. |
| `src/bfs.py` | Implements Breadth-First Search. |
| `src/solver.py` | Contains DFS, A* and Reactive A*. |
| `src/dstar_lite.py` | Implements the D* Lite algorithm. |
| `src/partial_observation.py` | Integrates the robot simulation with D* Lite navigation. |
| `src/maze_generator.py` | Generates reproducible maze datasets. |
| `src/maze_visualizer.py` | Provides maze visualization functionality. |
| `src/data_loader.py` | Supports loading project data. |
| `src/external_dataset_loader.py` | Supports external maze dataset loading. |
| `src/experiment_measurement.py` | Contains an experiment measurement workflow. |
| `src/main.py` | Runs the main maze simulation and records results. |
| `run_experiments.py` | Runs the main multi-seed algorithm evaluation. |

## 3. Maze Representation

The maze is represented as a two-dimensional matrix.

Example:

```text
0 0 1 0 0
1 0 1 0 1
0 0 0 0 0
0 1 1 1 0
0 0 0 0 0
```

Cell representation:

| Value | Meaning |
|---|---|
| 0 | Free cell |
| 1 | Obstacle or wall |
| -1 | Unknown cell in the robot's internal map |

The default starting position is `(0, 0)`.

The default goal position is the bottom-right cell.

The project uses four-direction movement:

- Up
- Down
- Left
- Right

Each movement has a cost of 1.

Manhattan distance is used as the heuristic for A* and D* Lite:

`h(n) = |row1 - row2| + |col1 - col2|`

## 4. Algorithms Implemented

### 4.1 Breadth-First Search (BFS)

BFS explores the maze level by level using a queue.

It examines neighbouring cells before moving to cells farther away.

For an unweighted grid, BFS can find a shortest path when a path exists.

### 4.2 Depth-First Search (DFS)

DFS explores one direction deeply before backtracking.

It uses a stack to manage unexplored positions.

DFS can find a valid route, but it does not guarantee the shortest path.

### 4.3 A* Search

A* uses a priority queue to select promising cells.

Its evaluation function is:

`f(n) = g(n) + h(n)`

Where:

- `g(n)` is the cost from the starting position.
- `h(n)` is the estimated cost to the goal.
- `f(n)` is the combined estimated cost.

The project uses Manhattan distance as its heuristic.

### 4.4 Reactive A*

Reactive A* works under partial observation.

The robot does not initially know the complete obstacle layout.

It:

1. Maintains a map of discovered cells.
2. Plans a route using A*.
3. Attempts to move along the route.
4. Discovers an obstacle if the next cell is blocked.
5. Updates its internal map.
6. Calculates another route.

The implementation uses unknown, free and wall states.

The enhanced Reactive A* experiment also investigates visit penalties to study their effect on navigation.

### 4.5 D* Lite

D* Lite is an incremental pathfinding algorithm.

Instead of calculating an entirely new route from scratch after every environmental change, it reuses previous search information.

Important concepts include:

- `g` values: current path-cost estimates.
- `rhs` values: one-step lookahead estimates.
- Priority queue: manages inconsistent cells that need processing.
- `km`: adjusts heuristic keys as the robot's start position moves.

When a newly discovered obstacle changes movement costs, D* Lite updates affected cells and repairs the route.

### 4.6 Wall Following

The project also contains a wall-following algorithm.

The robot follows either a left-hand or right-hand wall preference while navigating.

It tracks position and direction to detect repeated states and avoid endless movement.

This is an additional navigation technique and is separate from the five-algorithm Week 12 statistical evaluation.

## 5. Partial-Observation Navigation Workflow

The partial-observation simulation combines the Robot class and D* Lite planner.

The process is:

1. Initialize the robot at the starting cell.
2. Create its internal map using currently known information.
3. Initialize the D* Lite planner.
4. Calculate a route.
5. Select the next cell.
6. Attempt to move into that cell.
7. If an obstacle is discovered, update the planning map.
8. Replan using D* Lite.
9. Continue until the goal is reached or no route is available.

The robot records its movement history and discovered obstacles.

## 6. Dataset Generation

The project includes a procedural maze generator.

It generates three maze sizes:

| Category | Dimensions |
|---|---|
| Small | 10 × 10 |
| Medium | 20 × 20 |
| Large | 30 × 30 |

The generator uses fixed random seeds to make maze generation reproducible.

The generator initially creates a route from the starting cell to the goal. It then places obstacles in cells outside that guaranteed route.

The main experiment runner uses seeds 42 through 51.

## 7. Experimental Methodology

The main experimental evaluation is performed using:

`run_experiments.py`

### Experimental configuration

| Parameter | Value |
|---|---|
| Random seeds | 42–51 |
| Number of seeds | 10 |
| Maze sizes | Small, Medium, Large |
| Fully visible algorithms | BFS, DFS, A* |
| Partial-observation algorithms | Reactive A*, D* Lite |
| Total experiments | 150 |

### Observation scenarios

**Fully visible scenario**

The algorithms operate with access to the complete maze.

Algorithms:

- BFS
- DFS
- A*

**Partial-observation scenario**

The navigation algorithms operate with incomplete initial knowledge.

Algorithms:

- Reactive A*
- D* Lite

Each algorithm receives a fresh maze copy for an experiment.

This prevents one algorithm's maze modifications from affecting another algorithm's run.

## 8. Performance Evaluation Metrics

The project records several performance measurements.

| Metric | Explanation |
|---|---|
| Success rate | Percentage of runs that reach the goal. |
| Path length | Number of movements in the resulting path. |
| Nodes expanded | Number of search nodes processed. |
| Runtime | Time required to execute the algorithm. |
| Peak memory | Maximum traced memory usage during execution. |
| Replan count | Number of replanning operations. |
| Obstacles discovered | Number of previously unknown obstacles identified. |

The experiment runner calculates:

- Mean
- Standard deviation
- Minimum
- Maximum

Path-length statistics are calculated using successful runs. Other metrics are summarized across the recorded runs.

Runtime and memory measurements can vary depending on the execution environment.

## 9. Experimental Output

The main experiment runner generates three CSV files.

| File | Purpose |
|---|---|
| `results/experiment_results.csv` | Individual experiment results. |
| `results/experiment_summary.csv` | Statistical summaries. |
| `results/experiment_failures.csv` | Unsuccessful experiment records. |

The Week 12 chart generator reads the statistical summary and creates four figures:

```text
results/week12_graphs/
├── nodes_expanded.png
├── path_length.png
├── runtime_seconds.png
└── peak_memory_kb.png
```

Each figure contains separate panels for fully visible and partial-observation scenarios.

The plots show mean values with standard-deviation error bars.

## 10. Automated Testing

The project includes automated tests for important components.

Run the test suite using:

```bash
python -m pytest src/ -v
```

The verified Week 12 test run collected 14 tests, all of which passed.

Additional standalone scripts in `src/` support algorithm experiments, external dataset comparisons and robustness evaluation. They should not all be treated as automated pytest tests.

## 11. Limitations

The project is a software-based maze and robot simulation. It does not control a physical robot.

Other limitations include:

- The environment is represented as a discrete grid.
- Movement is restricted to four directions.
- Each movement has a uniform cost.
- Runtime and memory measurements depend on the computer and execution environment.
- Partial-observation performance depends on the obstacle discovery and replanning process.
- Invalid or malformed maze inputs are not comprehensively validated by every module.

Further details are available in:

- `docs/LIMITATIONS.md`
- `docs/WEEK11_ROBUSTNESS_TESTING.md`

## 12. Future Scope

Possible future improvements include:

- Integrating the navigation algorithms with a physical robot.
- Introducing dynamic and moving obstacles.
- Supporting different movement costs.
- Exploring additional heuristic and search techniques.
- Improving input validation and error handling.
- Expanding experiments with larger and more diverse datasets.
- Developing a more advanced real-time visualization system.

## 13. Conclusion

The project demonstrates how classical search and incremental pathfinding techniques can be applied to grid-based robot navigation.

By evaluating fully visible and partial-observation scenarios, it investigates both initial path planning and navigation under newly discovered obstacles.

The experimental pipeline, statistical summaries, robustness tests and saved visualizations provide a foundation for evaluating and reproducing the implemented algorithms.

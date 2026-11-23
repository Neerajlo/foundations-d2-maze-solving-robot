# Project Integration Documentation

## 1. Project Overview

The Maze Solving Robot project implements and evaluates search and path-replanning algorithms in a grid-based simulated environment.

The system represents a maze as a two-dimensional grid containing free cells and obstacles. A robot navigates from a predefined starting position to a goal position using different pathfinding algorithms.

The project evaluates five algorithms:

1. Breadth-First Search (BFS)
2. Depth-First Search (DFS)
3. A* Search
4. Reactive A*
5. D* Lite

The implementation supports both fully observable and partially observable maze environments.

## 2. System Architecture

The project is organised into the following components:

### 2.1 Maze Representation

File: `src/maze.py`

The Maze class represents the environment using a two-dimensional grid.

- 0 represents a free cell.
- 1 represents an obstacle.
- The starting and goal positions define the navigation task.
- Four-directional movement is supported.
- Neighbour cells are checked before movement.

### 2.2 Maze Generation

File: `src/maze_generator.py`

The maze generator creates reproducible maze layouts using a random seed.

A guaranteed route is generated from the starting cell to the goal before additional obstacles are placed.

The configured maze dimensions are:

- Small: 10 x 10
- Medium: 20 x 20
- Large: 30 x 30

### 2.3 Search Algorithms

Files:

- `src/bfs.py`
- `src/solver.py`

The project implements:

- BFS using a FIFO queue.
- DFS using a LIFO stack.
- A* using path cost and Manhattan-distance heuristic.
- Reactive A* using repeated planning with an incrementally discovered map.

### 2.4 Robot Simulation

File: `src/robot.py`

The Robot class simulates movement through the maze.

It maintains a separate representation of the environment containing:

- Unknown cells.
- Known free cells.
- Discovered obstacles.

The robot updates its knowledge when it attempts to enter a cell.

### 2.5 D* Lite Implementation

File: `src/dstar_lite.py`

D* Lite supports incremental path planning.

The implementation maintains:

- g-values.
- rhs-values.
- A priority queue.
- Manhattan-distance heuristic.
- Start-position updates.
- Obstacle updates.
- Cumulative node-expansion and replanning measurements.

When an obstacle is discovered, the planner updates affected cells and reuses previously calculated search information.

### 2.6 Partial-Observation Navigation

File: `src/partial_observation.py`

This module integrates the robot simulation with D* Lite.

The process is:

1. Initialise the robot with knowledge of its starting cell.
2. Create a planning map from known information.
3. Treat unknown cells as open for planning.
4. Calculate a route using D* Lite.
5. Attempt to move the robot.
6. Detect obstacles when movement is blocked.
7. Update the planning map.
8. Replan using D* Lite.
9. Continue until the goal is reached or navigation fails.

## 3. Experimental Integration

Main experiment runner: `run_experiments.py`

The main experiment pipeline evaluates five pathfinding algorithms under two observation conditions using two independent experimental datasets.

### Fully Observable Scenario

Algorithms:

- BFS
- DFS
- A*

The complete maze layout is available to the search algorithms before navigation begins.

### Partially Observable Scenario

Algorithms:

- Reactive A*
- D* Lite

The algorithms initially operate with incomplete obstacle information and discover previously unknown obstacles during navigation.

### Experimental Configuration

Both datasets use the same experimental configuration:

- Small maze: 10 × 10
- Medium maze: 20 × 20
- Large maze: 30 × 30
- Five algorithms
- Ten random seeds per dataset

**Dataset A — Primary Evaluation**

- Random seeds: 42–51
- Maze sizes: Small, medium, and large
- Total runs: 150

**Dataset B — Additional Statistical Evaluation**

- Random seeds: 100–109
- Maze sizes: Small, medium, and large
- Total runs: 150

**Overall Experimental Evaluation**

The two independent datasets contain 300 experimental runs in total.

Each dataset is analysed separately. Their statistical summaries are not combined, preserving the independence of the two evaluations.

A separate maze instance is created for each algorithm to maintain experimental independence.

## 4. Performance Measurement

The experiments evaluate the following metrics:

| Metric | Description |
|---|---|
| Success rate | Percentage of runs reaching the goal |
| Path length | Number of successful movement steps |
| Nodes expanded | Number of search nodes processed |
| Runtime | Execution time in seconds |
| Peak memory | Maximum traced memory usage in KB |
| Replanning count | Number of route updates |
| Obstacles discovered | Number of previously unknown obstacles detected |

Runtime is measured using Python's high-resolution performance counter.

Peak memory is measured using Python's tracemalloc module.

## 5. Result Storage

The experimental results are stored in the `results` directory. The primary evaluation and additional statistical evaluation are maintained separately.

### Dataset A — Primary Evaluation

Location: `results/`

Important files:

- `experiment_results.csv`: Individual experimental records.
- `experiment_summary.csv`: Aggregated statistical results.
- `experiment_failures.csv`: Records of unsuccessful runs.

### Dataset B — Additional Statistical Evaluation

Location: `results/experiment_runs/`

Important files:

- `experiment_results.csv`: Individual experimental records.
- `experiment_summary.csv`: Aggregated statistical results.
- `experiment_failures.csv`: Records of unsuccessful runs.

### Additional Experiment Results

The repository also contains supplementary experiment outputs, including D* Lite navigation results, external dataset comparisons, stress tests, and individual team-member experiment records.

These supplementary results are maintained separately from the two primary experimental datasets.

## 6. Result Visualisation

The project includes graphical visualisations to support the comparison of the five pathfinding algorithms.

The final research-paper figures are stored in:

`results/paper_figures/`

Eight figures are included:

### Dataset A

1. `dataset_A_nodes_expanded.png` — Mean nodes expanded.
2. `dataset_A_path_length.png` — Mean path length.
3. `dataset_A_runtime_seconds.png` — Mean execution time.
4. `dataset_A_peak_memory_kb.png` — Mean peak memory usage.

### Dataset B

5. `dataset_B_nodes_expanded.png` — Mean nodes expanded.
6. `dataset_B_path_length.png` — Mean path length.
7. `dataset_B_runtime_seconds.png` — Mean execution time.
8. `dataset_B_peak_memory_kb.png` — Mean peak memory usage.

The figures display the mean values with standard-deviation error bars. Dataset A and Dataset B are visualised separately to preserve the independence of their experimental results.

The Python script `generate_paper_figures.py` is included in the repository to support figure generation.

## 7. Earlier Experiment Runner

File: `src/main.py`

The project also contains an earlier experiment runner that evaluates BFS, DFS, A*, and Reactive A* on JSON maze files.

It saves its output to:

`results/maze_results.csv`

This runner is separate from the primary five-algorithm experiment pipeline.

## 8. Additional Navigation Experiments

The repository includes supplementary experiments, such as:

- Multi-obstacle D* Lite navigation.
- Challenging obstacle configurations.
- Reactive A* visit-penalty experiments.
- Wall-following comparisons.
- External maze dataset evaluations.

These experiments provide additional analysis and should not be merged into the primary 150-run comparison without a separately defined methodology.

## 9. Team Integration

The project was developed collaboratively by three team members. Each member contributed to a specific part of the maze-solving system, and their individual work was integrated into a common codebase to develop a complete navigation and experimental evaluation framework.

### Member 1 – Riya (Team Lead and Search Algorithm Developer)

Riya was responsible for the development of the core search algorithms and research coordination.

Key contributions:

- Implemented Breadth-First Search (BFS) for systematic maze exploration and shortest-path search.
- Implemented Depth-First Search (DFS) for depth-oriented maze exploration.
- Developed the core D* Lite algorithm for incremental path planning.
- Contributed to algorithm evaluation and research coordination.
- Supported the integration of search algorithms into the overall maze-solving framework.

### Member 2 – Jasmeet (Autonomous Navigation and Replanning Developer)

Jasmeet was responsible for the robot navigation system and its operation in partially observable environments.

Key contributions:

- Developed autonomous navigation functionality for the simulated robot.
- Worked on partial-observation handling and the robot's knowledge of the environment.
- Implemented obstacle discovery during navigation.
- Developed navigation and replanning workflows when previously unknown obstacles were encountered.
- Integrated navigation functionality with the path-planning components.

### Member 3 – Neeraj (AI/ML and Algorithm Development)

Neeraj was responsible for AI/ML-related algorithm development and supporting the experimental evaluation of the project.

Key contributions:

- Contributed to AI/ML-related algorithm development within the project.
- Supported the implementation and integration of algorithm components.
- Contributed to experimental execution and performance evaluation.
- Supported the analysis and comparison of algorithm results.
- Contributed to the overall development of the maze-solving framework.

### Overall Team Integration

The three members' contributions were combined to create a unified maze-solving system. Search algorithms provide pathfinding capabilities, autonomous navigation handles robot movement and obstacle discovery, and algorithm development and experimentation support the evaluation of system performance.

The integrated project supports five principal algorithms: BFS, DFS, A*, Reactive A*, and D* Lite. Their performance is evaluated across fully observable and partially observable scenarios using two independent experimental datasets.

## 10. Limitations

The project evaluates algorithms in a software simulation rather than on a physical robot.

Partial observability is modelled through obstacle discovery during attempted movement.

Performance measurements depend on the implementation and execution environment. Node-expansion and memory measurements should therefore be interpreted within the stated experimental setup.

The two experimental datasets are maintained separately to preserve their independent evaluation conditions.

## 11. Conclusion

The integrated system combines classical search algorithms, heuristic pathfinding, robot simulation, partial-observation navigation, and incremental replanning.

The experimental pipeline provides a common framework for evaluating the five principal algorithms across different maze sizes and observation conditions.

The resulting CSV files and visualisations support the comparative analysis presented in the research paper.

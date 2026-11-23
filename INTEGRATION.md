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

The main experiment pipeline compares five algorithms under two observation conditions.

### Fully Observable Scenario

Algorithms:

- BFS
- DFS
- A*

The complete maze layout is available to the search algorithms.

### Partially Observable Scenario

Algorithms:

- Reactive A*
- D* Lite

The algorithms initially operate with incomplete obstacle information and discover obstacles during navigation.

### Experiment Configuration

- Random seeds: 42 to 51
- Small maze: 10 x 10
- Medium maze: 20 x 20
- Large maze: 30 x 30
- Five algorithms per maze configuration

The experiment configuration produces 150 runs:

10 seeds x 3 maze sizes x 5 algorithms.

A separate maze object is created for each algorithm to maintain experimental independence.

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

The primary experiment results are stored in the `results` directory.

Important files include:

- `experiment_results.csv`: Individual experimental records.
- `experiment_summary.csv`: Aggregated statistical results.
- `experiment_failures.csv`: Records of unsuccessful runs.
- `dstar_lite_navigation_results.csv`: Partial-observation navigation results.

The repository also contains supplementary experiment outputs and external-dataset results. These are maintained separately from the primary experiment records.

## 6. Result Visualisation

The project contains graphs for the following performance metrics:

- Path length.
- Nodes expanded.
- Runtime.
- Peak memory usage.

Existing figures are stored in:

- `results/experiment_graphs/`
- `results/week12_graphs/`

These figures support the comparison and interpretation of algorithm performance.

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

The project was developed collaboratively by three team members, with each member contributing to a specific area of the system.

### Member 1 – Riya (Team Lead)

Responsible for the implementation and development of classical search algorithms, including Breadth-First Search (BFS) and Depth-First Search (DFS), along with the core D* Lite algorithm. Also contributed to research coordination and algorithm evaluation.

### Member 2 – Jasmeet (Autonomous Navigation and Replanning)

Responsible for autonomous robot navigation, partial-observation handling, obstacle discovery, and replanning when the robot encounters previously unknown obstacles.

### Member 3 – Neeraj (AI/ML and Algorithm Development)

Responsible for AI/ML-related algorithm development and supporting the implementation, experimentation, and evaluation of the maze-solving system.

The individual contributions are integrated into a common repository to provide a unified maze-navigation and experimental evaluation framework.

## 10. Limitations

The project evaluates algorithms in a software simulation rather than on a physical robot.

Partial observability is modelled through obstacle discovery during attempted movement.

Performance measurements depend on the implementation and execution environment. Node-expansion and memory measurements should therefore be interpreted within the stated experimental setup.

The two experimental datasets are maintained separately to preserve their independent evaluation conditions.

## 11. Conclusion

The integrated system combines classical search algorithms, heuristic pathfinding, robot simulation, partial-observation navigation, and incremental replanning.

The experimental pipeline provides a common framework for evaluating the five principal algorithms across different maze sizes and observation conditions.

The resulting CSV files and visualisations support the comparative analysis presented in the research paper.

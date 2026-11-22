# A Comparative Study of Search and Replanning Algorithms for a Maze-Solving Robot

## 1. Abstract

Maze-solving is an important problem in artificial intelligence and autonomous navigation. Different search algorithms provide different levels of efficiency depending on maze size, obstacle distribution, and environmental observability. This project develops and evaluates a grid-based maze-solving robot using five algorithms: Breadth-First Search (BFS), Depth-First Search (DFS), A* Search, Reactive A*, and D* Lite.

The experimental environment consists of small (10×10), medium (20×20), and large (30×30) mazes. Ten random seeds (42–51) are used with an obstacle probability of 25%, and generated benchmark mazes contain a guaranteed path. A total of 150 experiments are conducted across the five algorithms and three maze sizes.

Performance is evaluated using success rate, path length, nodes expanded, execution time, peak memory usage, and replanning count. The recorded benchmark results show a 100% success rate for all five algorithms. The findings demonstrate differences between fully observable search algorithms and approaches designed for partial observation and replanning. This study provides a comparative evaluation of classical and replanning-based approaches in a controlled grid-maze environment.

## 2. Introduction

### 2.1 Background

Autonomous navigation is an important application of artificial intelligence and robotics. A maze-solving robot must identify a route from a starting position to a goal while avoiding obstacles. The task becomes more challenging when the robot has incomplete information about its surroundings or discovers obstacles during navigation.

Search algorithms provide a systematic way to explore possible routes. Breadth-First Search (BFS), Depth-First Search (DFS), and A* are widely used for pathfinding in known environments. In partially observable or changing environments, reactive navigation and incremental replanning methods can help the robot update its route as new information becomes available.

### 2.2 Problem Statement

The main problem addressed in this project is how different search and replanning algorithms perform when navigating grid-based mazes of different sizes. The study considers both fully observable environments, where the maze map is available, and partially observable environments, where the robot discovers information during navigation.

### 2.3 Aim

To develop a grid-based maze-solving robot simulation and comparatively evaluate classical search algorithms and replanning-based navigation algorithms.

### 2.4 Objectives

1. Develop a grid-based maze environment for robot navigation.
2. Implement BFS, DFS, and A* for fully observable pathfinding.
3. Implement Reactive A* and D* Lite for navigation under partial observability.
4. Evaluate the algorithms across different maze sizes and random seeds.
5. Compare their path length, nodes expanded, execution time, memory usage, and replanning behaviour.
6. Document the experimental results, limitations, and reproducibility procedures.

### 2.5 Scope

The project focuses on a software-based grid-maze simulation. It uses four-directional movement and evaluates algorithm performance under controlled experimental conditions. It does not claim to represent every aspect of physical robot navigation, such as real-world sensor noise, continuous motion, or hardware limitations.

## 3. Literature Review

### 3.1 Overview

A maze-solving robot is an autonomous system designed to navigate through a maze from a starting position to a specified goal. The robot may operate using a complete map of the environment or by observing only the cells that it has already explored.

These conditions represent two important problems in artificial intelligence: offline pathfinding and online navigation under partial observability.

Offline pathfinding algorithms such as Breadth-First Search (BFS), Depth-First Search (DFS), and A* search are used to find paths in a known maze. Online navigation approaches such as reactive path planning and incremental replanning help robots respond when new obstacles or unknown areas are discovered.

### 3.2 Review of Previous Studies

| No. | Paper (Author, Year) | Main Contribution | Relevance to This Project |
|---|---|---|---|
| 1 | Hart, Nilsson and Raphael (1968) | Introduced the A* search algorithm and established its theoretical properties. | Supports the use of heuristic search and Manhattan distance. |
| 2 | Korf (1985) | Introduced Iterative Deepening A* for memory-efficient heuristic search. | Highlights memory usage as an important performance measure. |
| 3 | Lumelsky and Stepanov (1987) | Studied Bug1 and Bug2 strategies for robot navigation around unknown obstacles. | Provides background for reactive navigation and wall-following approaches. |
| 4 | Stentz (1994) | Presented an efficient path-planning approach for partially known environments. | Establishes the importance of replanning when obstacles are discovered. |
| 5 | Yamauchi (1997) | Introduced frontier-based exploration for autonomous mobile robots. | Provides a foundation for systematic exploration of unknown regions. |
| 6 | Koenig and Likhachev (2002) | Presented D* Lite, an incremental heuristic search algorithm. | Directly relates to incremental replanning in this project. |
| 7 | Koenig, Likhachev and Furcy (2004) | Developed Lifelong Planning A* for repeated path-planning tasks. | Explains how previous search information can be reused. |
| 8 | Cui and Shi (2011) | Reviewed A*-based pathfinding techniques used in computer games. | Supports the use of A* as a pathfinding baseline. |
| 9 | Agcaoili et al. (2023) | Examined hybrid A* and hierarchical pathfinding approaches. | Provides context for possible future pathfinding improvements. |

### 3.3 Key Findings

The reviewed studies highlight several important findings:

1. BFS can find shortest paths in unweighted grid mazes, although it may explore many nodes.
2. DFS explores depth-first but does not guarantee the shortest path.
3. A* uses heuristic information to guide search towards the goal.
4. Reactive navigation allows a robot to respond to information discovered during movement.
5. D* and D* Lite support route replanning when environmental information changes.
6. Incremental search methods can reuse previous search information instead of restarting the entire search.

### 3.4 Research Gap and Project Contribution

Although several pathfinding algorithms have been studied extensively, their performance can vary depending on maze size, obstacle distribution, and environmental observability.

This project addresses the comparison of classical search algorithms and replanning-based algorithms within a common grid-maze simulation. It implements and evaluates BFS, DFS, A*, Reactive A*, and D* Lite. The evaluation considers both navigation performance and computational measures, including path length, nodes expanded, execution time, peak memory usage, and replanning count.

The project therefore extends beyond a comparison of fully observable search algorithms by also examining navigation under partial observability.

### 3.5 Datasets and Domains

The project-generated maze environments are the primary experimental dataset. External resources such as Moving AI Lab pathfinding benchmarks and Gymnasium FrozenLake may be considered for additional validation where their formats and experimental conditions are suitable.

## 4. Methodology

### 4.1 System Overview

The project uses a grid-based simulation in which a robot navigates from a start cell to a goal cell. The environment contains free cells and obstacle cells. In partially observable navigation, unknown cells are represented in the robot's internal map until they are discovered.

### 4.2 Maze Representation

The maze is represented as a two-dimensional grid:

- 0: Free cell
- 1: Obstacle cell
- -1: Unknown cell in the robot's internal map

The robot starts at the top-left position and attempts to reach the bottom-right position. Movement is allowed in four directions: up, down, left, and right. Each movement has a uniform cost of one.

### 4.3 Algorithms Implemented

**Breadth-First Search (BFS):** Explores the grid level by level and finds a shortest path in an unweighted maze when a path exists.

**Depth-First Search (DFS):** Explores one branch deeply before backtracking. It can find a valid route but does not guarantee the shortest route.

**A* Search:** Uses the cost already travelled and a heuristic estimate of the remaining distance to guide the search. Manhattan distance is suitable for the four-directional grid used in this project.

**Reactive A*:** Supports navigation under partial observability. The robot uses the information available in its internal map and updates its navigation as new obstacles or cells are discovered.

**D* Lite:** Uses incremental search and replanning to update navigation when new environmental information becomes available.

### 4.4 Experimental Procedure

The experiments follow a consistent procedure:

1. Generate or load a maze using the specified size and random seed.
2. Set the robot's starting position and goal.
3. Execute the selected algorithm under its corresponding observation condition.
4. Record whether the goal is reached.
5. Measure path length, nodes expanded, execution time, and peak memory usage.
6. Record replanning information for algorithms that support replanning.
7. Store the results in CSV files for analysis.

### 4.5 Performance Metrics

| Metric | Description |
|---|---|
| Success rate | Percentage of runs in which the goal is reached. |
| Path length | Number of movements in the resulting route. |
| Nodes expanded | Number of nodes explored during search. |
| Execution time | Time taken by the algorithm, measured in seconds. |
| Peak memory usage | Peak traced memory recorded during execution. |
| Replanning count | Number of route updates during navigation. |

### 4.6 Data Analysis

The recorded experimental data are stored in CSV files. Results are grouped by algorithm and maze size. Average values and success rates are used to compare algorithm performance. Graphs are generated for selected performance metrics to support visual comparison.

## 5. Experimental Setup

### 5.1 Software and Environment

The project is implemented as a Python-based grid-maze simulation and developed in a Windows environment. Git and GitHub are used for source-code management and project documentation.

### 5.2 Maze Configurations

Three maze configurations are used:

| Maze Category | Grid Size |
|---|---|
| Small | 10 × 10 |
| Medium | 20 × 20 |
| Large | 30 × 30 |

The benchmark uses ten random seeds, from 42 to 51, and an obstacle probability of 25%. Generated benchmark mazes contain a guaranteed path.

### 5.3 Algorithm and Observation Conditions

| Algorithm | Observation Condition |
|---|---|
| BFS | Fully observable |
| DFS | Fully observable |
| A* | Fully observable |
| Reactive A* | Partially observable |
| D* Lite | Partially observable |

### 5.4 Number of Experiments

The main benchmark contains:

10 random seeds × 3 maze sizes × 5 algorithms = **150 experiments**.

Each algorithm is evaluated across all three maze sizes using the same set of random seeds.

### 5.5 Recorded Outputs

The experimental outputs include:

- `results/experiment_results.csv`
- `results/experiment_summary.csv`
- `results/experiment_failures.csv`
- `results/week12_graphs/`

The graph directory contains visual comparisons for nodes expanded, path length, runtime, and peak memory usage.

### 5.6 Verification and Reproducibility

The project includes automated tests and a verification procedure for comparing summary results with raw experimental records. The Week 12 verification reported 60 summary rows matched and zero mismatches under the checks performed.

The project test suite reported 14 passing tests. A team-member fresh-clone reproduction also reported successful execution of all 150 benchmark experiments. This is team-level reproduction and should not be described as independent external verification.

### 5.7 Experimental Limitations

The study is based on a software simulation rather than a physical robot. The grid uses four-directional movement and uniform movement costs. Runtime and memory measurements may vary with hardware and software conditions. The benchmark also uses generated mazes with a guaranteed path, so its results should not be generalized to every possible maze configuration.

## 6. References

1. Hart PE, Nilsson NJ, Raphael B. A formal basis for the heuristic determination of minimum cost paths. IEEE Transactions on Systems Science and Cybernetics. 1968;4(2):100–107. doi:10.1109/TSSC.1968.300136.

2. Korf RE. Depth-first iterative-deepening: An optimal admissible tree search. Artificial Intelligence. 1985;27(1):97–109.

3. Lumelsky VJ, Stepanov AA. Path-planning strategies for a point mobile automaton moving amidst unknown obstacles of arbitrary shape. Algorithmica. 1987;2:403–430.

4. Stentz A. Optimal and efficient path planning for partially-known environments. Proceedings of the IEEE International Conference on Robotics and Automation. 1994:3310–3317.

5. Yamauchi B. A frontier-based approach for autonomous exploration. Proceedings of the IEEE International Symposium on Computational Intelligence in Robotics and Automation. 1997:146–151.

6. Koenig S, Likhachev M. D* Lite. Proceedings of the AAAI Conference on Artificial Intelligence. 2002:476–483.

7. Koenig S, Likhachev M, Furcy A. Lifelong Planning A*. Artificial Intelligence. 2004;155(1–2):93–146.

8. Cui X, Shi H. A*-based pathfinding in modern computer games. International Journal of Computer Science and Network Security. 2011;11(1):125–130.

9. Agcaoili CJ, Bernabe XY, Agustin VA. Hybridization of A* Pathfinding and Hierarchical Pathfinding A* Algorithm for Pathfinding in Grid Based Games. United International Journal for Research & Technology. 2023;4(8):14–22.

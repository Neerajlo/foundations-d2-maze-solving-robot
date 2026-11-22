1. Abstract
Path planning is an important problem in mobile robotics, where an agent must identify a suitable route from a starting position to a specified destination while avoiding obstacles. This study presents a simulation-based maze-solving framework developed to examine five search algorithms under fully observable and partially observable environments. The implemented algorithms are Breadth-First Search (BFS), Depth-First Search (DFS), A*, Reactive A*, and D* Lite. The environment uses four-directional movement in a grid-based maze, with Manhattan distance as the heuristic for heuristic-based path planning.

The evaluation consists of two independent experimental datasets. The primary evaluation uses ten random seeds (42–51) across three maze sizes and five algorithms, producing 150 runs. An additional statistical evaluation uses a separate set of ten seeds (100–109), also producing 150 runs. Together, these evaluations contain 300 runs, with results analysed separately for each dataset rather than combining their statistical summaries. BFS, DFS, and A* are evaluated with complete maze information, while Reactive A* and D* Lite operate under partial observation and discover obstacles during navigation. All 150 runs in each evaluation completed successfully.

Performance is examined using success rate, path length, nodes expanded, execution time, peak memory usage, replanning activity, and obstacles discovered. The results illustrate differences in search effort, path length, and computational requirements across algorithms and maze sizes. The study provides a comparative simulation framework for understanding classical search and replanning-based navigation while recognising the limitations of comparing algorithms operating under different observation conditions.

Keywords: Maze Solving, Path Planning, Breadth-First Search, Depth-First Search, A*, Reactive A*, D* Lite, Mobile Robotics, Partial Observability.
2. Introduction
2.1 Background
Path planning is one of the fundamental tasks in mobile robotics and artificial intelligence. A mobile robot operating in an environment must determine a route from its current position to a target location while avoiding obstacles. The quality of the selected route can affect navigation efficiency, movement cost, and the robot's ability to reach its destination.

Maze environments provide a useful way to study path-planning techniques because they represent navigation problems using a structured arrangement of free cells and obstacles. A maze can be represented as a two-dimensional grid in which each cell represents either a traversable position or an obstacle. The robot moves through the available cells to reach the goal.

Search algorithms are commonly used to solve these navigation problems. Breadth-First Search (BFS) explores neighbouring positions level by level, while Depth-First Search (DFS) explores one direction deeply before considering alternatives. A* uses a heuristic function to guide the search towards the destination. These algorithms can be evaluated when the complete maze is available to the agent.

However, real navigation situations may not provide complete information about the environment. A robot may initially know only part of the map and discover obstacles while moving. In such situations, a previously planned route may become unavailable, requiring the robot to calculate an alternative path. Reactive A* and D* Lite provide approaches for handling changing knowledge of the environment and replanning navigation routes.

This project develops a grid-based maze-solving simulation to study these search techniques under different observation conditions. It focuses on understanding their behaviour, comparing their performance, and examining how replanning can support navigation when obstacles are discovered during movement.
2.2 Problem Statement
Traditional path-planning algorithms are often evaluated when the complete environment is known in advance. However, this assumption does not always represent navigation situations in which obstacles are discovered during movement.

When a robot encounters an unknown obstacle, its existing route may no longer be valid. It must update its knowledge of the environment and identify another route to the destination. Recalculating a complete path after every change may also involve additional computational effort.

Therefore, the main problem addressed in this study is to examine how different search algorithms perform in fully observable and partially observable maze environments. The study focuses on comparing classical search methods with replanning-based approaches and evaluating their behaviour using measurable performance indicators.
2.3 Research Objectives
The main objectives of this study are:
1. To develop a grid-based maze-solving simulation using Python.
2. To implement BFS, DFS, A*, Reactive A*, and D* Lite for maze navigation.
3. To evaluate BFS, DFS, and A* when the complete maze is known.
4. To examine Reactive A* and D* Lite in partially observable environments where obstacles can be discovered during navigation.
5. To measure algorithm performance using path length, nodes expanded, execution time, peak memory usage, replanning activity, and obstacles discovered.
6. To evaluate the algorithms across different maze sizes and random seeds.
7. To understand the advantages and limitations of different search approaches in maze-based navigation.
2.4 Scope of the Study
This study is limited to a software-based maze-solving simulation developed in Python. The environment is represented as a two-dimensional grid containing free cells and blocked cells. Movement is restricted to four directions: up, down, left, and right.

The study considers two observation conditions. In the fully observable environment, the complete maze is available to the search algorithm before path planning begins. In the partially observable environment, the agent has incomplete information and discovers obstacles during navigation.

Five algorithms are included: BFS, DFS, A*, Reactive A*, and D* Lite. The Manhattan distance heuristic is used for heuristic-based path planning in the four-directional grid environment.

The study includes two independent experimental evaluations across three maze sizes and ten random seeds each, producing 150 runs per dataset and 300 runs in total. The datasets are analysed separately. The study focuses on simulation results and algorithmic performance. It does not include physical robot construction, real-world sensor integration, or testing in an actual outdoor or indoor robotic environment.
3. Literature Review
Path planning is a fundamental problem in mobile robotics and artificial intelligence. Researchers have developed several search and navigation techniques to help autonomous agents find routes, avoid obstacles, and respond to changes in their environments. The existing literature covers classical graph-search algorithms, heuristic-based pathfinding, reactive navigation, and incremental replanning. These studies provide the theoretical foundation for the algorithms implemented in this maze-solving project.
3.1 Classical Search and Heuristic-Based Pathfinding
Hart, Nilsson, and Raphael (1968) introduced the A* search algorithm and established its theoretical properties. A* uses both the cost of the path already travelled and a heuristic estimate of the remaining distance to the goal. The study established that an admissible heuristic can help A* find an optimal path. This work provides the foundation for using A* in the present project, where Manhattan distance is used as the heuristic for four-directional grid movement [1].

Korf (1985) examined Depth-First Iterative-Deepening (DFID), a search approach that combines depth-limited exploration with repeated iterations. DFID is distinct from the ordinary Depth-First Search (DFS) implemented in this project. However, the work provides useful background on the relationship between search strategies and memory requirements. This is relevant to the present study because memory consumption is included among the performance measures [2].

Cui and Shi (2011) discussed A*-based pathfinding techniques used in modern computer games. Their work highlights the importance of A* and its optimizations in pathfinding applications. This provides additional support for selecting A* as one of the algorithms evaluated in the grid-based maze environment [8].

Agcaoili et al. (2023) examined the combination of A* pathfinding with Hierarchical Pathfinding A*. Their work considered how hierarchical approaches can reduce search effort in suitable grid-based environments. This study provides a possible direction for extending the current project through hierarchical path planning [9].
3.2 Reactive Navigation and Partially Known Environments
Lumelsky and Stepanov (1987) presented the Bug1 and Bug2 strategies for mobile robot navigation in environments containing unknown obstacles. Both strategies use obstacle-boundary following to help a robot navigate when a complete map is not available. Their work demonstrates how local environmental information can support navigation in unknown environments. Although these Bug strategies are not implemented in the present project, they provide relevant background for understanding reactive obstacle avoidance and navigation [3].

Stentz (1994) presented the D* path-planning approach for environments that are only partially known. The research focused on updating a route when new obstacles or environmental changes are discovered. This is closely related to the problem addressed in the project, where a previously planned route may become blocked during navigation and the agent must identify an alternative route [4].

Yamauchi (1997) introduced frontier-based exploration for autonomous mobile robots. This approach uses the boundaries between explored and unexplored regions to guide further exploration. The study demonstrates the importance of systematically exploring unknown environments. Although frontier-based exploration is not the primary focus of the current implementation, it provides a possible direction for future development of the maze-solving system [5].
3.3 Incremental Search and Replanning
Koenig and Likhachev (2002) introduced D* Lite, an incremental heuristic search algorithm designed for path planning in changing or partially known environments. Unlike approaches that calculate a completely new route after every environmental change, D* Lite can reuse previous search information to update the path. This makes the algorithm particularly relevant to navigation scenarios in which obstacles are discovered during movement. D* Lite is implemented and evaluated in the present project as one of the approaches for partial-observation navigation [6].

Koenig, Likhachev, and Furcy (2004) developed Lifelong Planning A* (LPA*), an incremental search algorithm for repeated path-planning tasks. LPA* reuses information from previous searches when only part of the environment changes. Their work provides a broader understanding of incremental search and explains the value of retaining previous search information instead of repeatedly solving the entire problem from the beginning [7].
3.4 Summary of Literature and Research Gap
The reviewed studies establish the foundations of several approaches to path planning, including classical search, heuristic search, reactive navigation, and incremental replanning. However, these approaches address different search strategies and environmental conditions. Their reported behaviour therefore cannot automatically be treated as directly comparable across different experimental settings.

The present study focuses on implementing and evaluating five pathfinding algorithms within a common grid-based maze simulation. BFS, DFS, and A* are evaluated in fully observable environments, while Reactive A* and D* Lite are evaluated in partially observable environments. Since these groups operate with different levels of environmental information, performance comparisons are made primarily within their respective scenarios rather than as a direct ranking of all five algorithms.

The evaluation considers path length, nodes expanded, execution time, peak memory usage, replanning count, and obstacles discovered. It uses three maze sizes and two independent experimental datasets with separate sets of fixed random seeds. The results of these datasets are reported separately, allowing the behaviour of the algorithms to be examined across two independent evaluations without combining their measurements.

The contribution of this project is an implementation-level experimental evaluation of classical search and replanning-based approaches within a shared maze-solving simulation. Rather than proposing a new search algorithm, the study examines how the implemented approaches behave under different observation conditions and maze sizes, using a consistent set of recorded performance measures.
4. Methodology
4.1 Research Design
This study uses a simulation-based experimental approach to evaluate five pathfinding algorithms in grid-based maze environments. The algorithms are Breadth-First Search (BFS), Depth-First Search (DFS), A*, Reactive A*, and D* Lite.

The experiments are divided into two scenarios: fully observable and partially observable environments. In the fully observable scenario, the algorithms BFS, DFS, and A* operate with complete knowledge of the maze. In the partially observable scenario, Reactive A* and D* Lite operate with incomplete knowledge and discover obstacles during navigation.

The performance of the algorithms is evaluated using success rate, path length, number of nodes expanded, execution time, peak memory usage, replanning count, and number of discovered obstacles. Since the algorithms are evaluated under different observation conditions, comparisons are made primarily within their respective scenarios rather than as a direct ranking of all five algorithms under identical conditions.
4.2 Maze Environment and Generation
The environment is represented as a two-dimensional grid. Each cell represents a possible robot position. A value of 0 represents a free cell, while a value of 1 represents an obstacle.

The robot starts at the top-left position, (0, 0), and the goal is located at the bottom-right position. Movement is restricted to four directions: up, down, left, and right. Each valid movement has a cost of one.

Random mazes are generated using a custom Python maze-generation function. The generator first initializes an empty grid and constructs a guaranteed route from the starting position to the goal. Starting at (0, 0), the route is created by randomly selecting either a downward or rightward movement whenever both directions are available. When only one direction remains possible, the generator follows that direction until the goal is reached. After constructing the route, the generator independently places obstacles in cells outside the route, using a probability of 25% for each eligible cell.

Fixed random seeds are used to make maze generation reproducible. The experiments use three maze dimensions: 10 × 10, 20 × 20, and 30 × 30. Dataset A uses ten seeds, from 42 to 51, while Dataset B uses a separate set of ten seeds, from 100 to 109, for each maze size.
4.3 Pathfinding Algorithms
Five algorithms are evaluated in this study.
4.3.1 Breadth-First Search (BFS)
BFS explores the maze level by level using a First-In, First-Out (FIFO) queue. It visits the neighboring cells of the current position before exploring cells at the next depth level.

A parent dictionary records how each cell was reached, allowing the final path to be reconstructed after reaching the goal. Since every movement has an equal cost, BFS can find a shortest path in terms of the number of moves.
4.3.2 Depth-First Search (DFS)
DFS explores one possible route as deeply as possible before backtracking. It uses a stack to manage the positions that remain to be explored.

The implementation records visited positions and their parent relationships to reconstruct a path when the goal is reached. DFS provides a comparison with BFS because it follows a different exploration strategy. However, it does not guarantee a shortest path.
4.3.3 A* Search
A* combines the actual cost of reaching a cell with an estimated cost from that cell to the goal. It uses a priority queue to select the next cell for exploration.

The evaluation function is:

f(n) = g(n) + h(n)

Here, g(n) represents the cost from the starting position to the current cell, while h(n) estimates the remaining distance to the goal.

The Manhattan distance is used as the heuristic because movement is restricted to four directions:

h(n) = |x1 - x2| + |y1 - y2|

This helps A* prioritise cells that appear closer to the goal while considering the cost already travelled.
4.3.4 Reactive A*
A reactive replanning strategy based on A* (referred to in this project as Reactive A*) is evaluated in the partially observable scenario. The robot does not initially know the complete obstacle layout.

It maintains a discovered map in which cells are initially marked as unknown, except for the starting position. Unknown cells are temporarily treated as free for planning.

The strategy first plans a route using A*. As the robot follows the route, the simulation checks each attempted cell against the actual maze. If the cell contains an obstacle, the robot records the discovery and runs A* again using the updated known map. This process continues until the robot reaches the goal or no valid route can be found. In this project, Reactive A* therefore refers to this implemented plan–move–observe–replan procedure.
4.3.5 D* Lite
D* Lite is an incremental pathfinding algorithm designed to support navigation when the environment changes or new obstacles are discovered.

The implementation maintains two important values for each cell: g-value and rhs-value. These values help the algorithm identify whether its current path information needs updating.

D* Lite uses a priority queue and the Manhattan distance heuristic to organize its search. When the robot discovers an obstacle, the affected cell and its neighboring cells are updated, and the planner recalculates the route using its existing search information.

After a successful movement, the robot's starting position is updated so that the planner can continue navigation from its new position.
4.4 Partial Observation and Robot Navigation
The partially observable environment is implemented using a simulated robot that maintains its own knowledge of the maze.

Initially, the robot knows its starting position but does not know the locations of all obstacles. Its internal map distinguishes between unknown cells, free cells, and blocked cells.

When the robot attempts to enter a cell, the simulation checks that position against the actual maze. If the cell is free, the robot moves into it and updates its known map. If the cell contains an obstacle, the robot records the discovery and does not enter that cell.

The planning map temporarily treats unknown cells as free. This allows the algorithms to generate an initial route without having complete information about the environment.

Reactive A* and D* Lite use this partial-observation setting to evaluate how path planning responds to newly discovered obstacles.
4.5 Experimental Procedure
The study consists of two independent experimental evaluations conducted using the same five pathfinding algorithms, three maze sizes, and two observation scenarios.

For every generated maze, five algorithms are evaluated:
- BFS, DFS, and A* in the fully observable scenario.
- Reactive A* and D* Lite in the partially observable scenario.

A fresh copy of the generated maze is provided to each algorithm. This ensures that changes made during one algorithm's execution do not affect the maze used by another algorithm.

The two evaluations use separate sets of ten fixed random seeds:

| Evaluation | Random Seeds | Maze Sizes | Algorithms | Total Runs |
|---|---|---|---|---|
| Primary evaluation (Dataset A) | 42–51 | 10 × 10, 20 × 20, 30 × 30 | 5 | 150 |
| Additional statistical evaluation (Dataset B) | 100–109 | 10 × 10, 20 × 20, 30 × 30 | 5 | 150 |

For each evaluation, the number of experiments is calculated as:

For each dataset, total experiments = 10 seeds × 3 maze sizes × 5 algorithms = 150 runs.

Across both independent evaluations, 300 experiment runs were conducted. The datasets retain separate seed ranges and are analysed independently rather than being combined into a single statistical dataset.

The experiment runners collect the output from each run and store the results for further analysis. They also record unsuccessful runs and any errors encountered during execution.
4.6 Performance Evaluation Metrics
The algorithms are evaluated using the following metrics:
1. Success Rate: The percentage of runs in which an algorithm successfully reaches the goal.
2. Path Length: The number of movements required to reach the goal. Path length is calculated for successful runs.
3. Nodes Expanded: The number of positions explored by the algorithm during its search.
4. Execution Time: The time required to execute the algorithm, measured in seconds.
5. Peak Memory Usage: The maximum memory used during execution, measured in kilobytes.
6. Replanning Count: The number of times a new route is calculated following changes or newly discovered obstacles.
7. Obstacles Discovered: The number of previously unknown obstacles identified during navigation.
Python's time measurement and memory-tracking facilities are used to record execution time and peak memory usage. The results are stored in CSV files for analysis.
4.7 Statistical Analysis
The experiment results are grouped according to the observation scenario, maze size, and algorithm.

For each group, the mean, standard deviation, minimum, and maximum values are calculated for the measured performance metrics. Success rate is also calculated as a percentage.

Path-length statistics are calculated using successful runs only because an unsuccessful run does not provide a completed route. The other recorded metrics are summarised using all runs in the corresponding group.

Statistical analysis is performed independently for the two experimental datasets. Dataset A uses seeds 42–51 and Dataset B uses seeds 100–109. Their means, standard deviations, and other statistical summaries are not pooled. This preserves the distinction between the primary evaluation and the additional statistical evaluation.

The primary evaluation results are stored in the results directory, while the additional evaluation results are stored in the results/experiment_runs directory. Each evaluation maintains its own individual run results, statistical summary, and failure records.

These results provide the basis for comparing the behaviour and performance of the five pathfinding algorithms under the two observation scenarios.
4.8 Experimental Limitations
The experiments are conducted in a software simulation using generated grid mazes. The results therefore describe algorithm behaviour in this controlled environment and should not be treated as direct evidence of performance on a physical robot.

The algorithms are also evaluated under two different information conditions: BFS, DFS, and A* receive the complete maze, while Reactive A* and D* Lite discover obstacles during navigation. Consequently, comparisons between algorithms are interpreted in the context of their respective scenarios.

The maze generator creates a guaranteed free route from the start to the goal and places obstacles outside that route. This supports repeatable solvable test cases, but it does not represent every possible maze structure or real-world obstacle distribution. These constraints should be considered when interpreting the results.
5. Experimental Setup
5.1 Hardware Configuration
The hardware configuration documented for the primary evaluation (Dataset A) is listed below. The experiments were conducted on a personal computer running Windows 10 Home Single Language (64-bit).

| Component | Specification |
|---|---|
| Processor | 13th Gen Intel Core i5-1335U |
| Number of CPU cores | 10 |
| Logical processors | 12 |
| Installed RAM | Approximately 16 GB |
| Operating System | Windows 10 Home Single Language |
| System Architecture | 64-bit |

The experiments were executed locally on this computer. No physical robot or external hardware was used because the study focuses on simulation-based maze navigation.

The original documentation available for the additional statistical evaluation (Dataset B) does not specify its hardware configuration. Therefore, the hardware specifications above are not attributed to Dataset B.
5.2 Software Configuration
The software configuration documented for the primary evaluation (Dataset A) used Python version 3.14.3 in a system-wide Python environment.

The following package versions are recorded for this evaluation:

| Package | Version | Purpose |
|---|---|---|
| Python | 3.14.3 | Main programming language |
| Matplotlib | 3.11.2 | Generating charts and visualisations |
| Pandas | 3.1.1 | Data handling and tabular analysis |
| Pytest | 9.2.0 | Automated testing |
| python-docx | 1.2.0 | Working with Word documents |

The project dependencies are listed in the requirements.txt file. The primary evaluation was executed using the system-wide Python installation rather than a separate project-specific virtual environment.

The available original documentation for Dataset B does not establish its exact Python interpreter or package versions. These versions are therefore reported only for Dataset A and are not assumed to apply to Dataset B.
5.3 Experimental Configuration
Both evaluations use three maze dimensions: 10 × 10, 20 × 20, and 30 × 30. They use separate sets of ten fixed random seeds to generate reproducible maze layouts.

The five algorithms are divided according to the observation scenario. BFS, DFS, and A* are tested in fully observable environments, while Reactive A* and D* Lite are tested in partially observable environments.

For each generated maze, a separate copy is provided to every algorithm. This prevents modifications made during one algorithm's execution from affecting the other experiments.

The configurations are:

| Configuration | Primary Evaluation (Dataset A) | Additional Evaluation (Dataset B) |
|---|---|---|
| Random seeds | 42–51 | 100–109 |
| Maze dimensions | 10 × 10, 20 × 20, 30 × 30 | 10 × 10, 20 × 20, 30 × 30 |
| Algorithms | 5 | 5 |
| Runs per evaluation | 150 | 150 |

Each evaluation consists of 10 seeds × 3 maze sizes × 5 algorithms = 150 runs. The two evaluations are maintained as separate experimental datasets.
5.4 Experiment Execution
The two evaluations were executed using separate experiment runners.

Dataset A uses the main experiment script, run_experiments.py. Dataset B uses the additional evaluation script, run_week7_experiments.py.

Each runner generates mazes using its specified dimensions and random seeds. It then executes the five algorithms under their corresponding observation scenarios. Each experiment is recorded separately with its maze identifier, dimensions, seed, scenario, and algorithm name.

The experiment runners record unsuccessful runs and associated error information rather than silently ignoring failed executions. Both evaluations completed 150 runs successfully, with no failed runs.
5.5 Performance Measurement Tools
Python's built-in measurement facilities are used to collect performance information. The time.perf_counter() function measures execution time in seconds, while the tracemalloc module tracks Python memory allocations and records peak traced memory during execution. This value represents Python-tracked allocations rather than the complete memory consumption of the operating system or every native library.

The recorded performance information includes:
1. Success or failure of the algorithm.
2. Path length.
3. Number of nodes expanded.
4. Execution time in seconds.
5. Peak traced memory usage in kilobytes.
6. Number of replanning operations.
7. Number of obstacles discovered.

D* Lite uses its own runtime and peak-memory measurement function in the partial-observation navigation implementation. In the additional evaluation (Dataset B), this measurement approach differs from the external measurement wrapper used for the other algorithms. Consequently, execution-time and memory comparisons involving D* Lite should be interpreted cautiously.

The number of nodes expanded is also an algorithm-specific measure based on the counters maintained by each implementation. It represents search effort within the implemented algorithms and should not be interpreted as an identical internal operation across all five methods.
5.6 Result Storage and Organization
The experimental results are stored in CSV format in separate directories for the two evaluations.

Dataset A stores its results in the results directory:

| File | Description |
|---|---|
| results/experiment_results.csv | Individual results of the primary evaluation. |
| results/experiment_summary.csv | Statistical summaries of the primary evaluation. |
| results/experiment_failures.csv | Unsuccessful experiment cases and associated error information. |

Dataset B stores its results in the results/experiment_runs directory:

| File | Description |
|---|---|
| results/experiment_runs/experiment_results.csv | Individual results of the additional statistical evaluation. |
| results/experiment_runs/experiment_summary.csv | Statistical summaries of the additional evaluation. |
| results/experiment_runs/experiment_failures.csv | Unsuccessful experiment cases and associated error information. |

The statistical summaries include the mean, standard deviation, minimum, and maximum values for the recorded metrics. Success rate is represented as a percentage. Path-length statistics are calculated using successful runs, while other performance metrics are summarised using all runs in the corresponding group.

The two result directories preserve the independence of the experimental evaluations and prevent their statistical summaries from being unintentionally combined.
6. Experimental Results

6.1 Overview of Experimental Outcomes

The study consists of two independent evaluations, each containing 150 experiment runs. Dataset A uses random seeds 42–51, while Dataset B uses seeds 100–109. Both evaluations cover three maze sizes and five pathfinding algorithms.

All 150 runs in Dataset A and all 150 runs in Dataset B completed successfully. Therefore, both evaluations achieved a success rate of 100%, with no failed runs.

The following tables present the mean and sample standard deviation for the measured performance metrics. Results are reported separately for each dataset. Path length, nodes expanded, execution time, and peak memory are included. Replanning count is reported for the partially observable algorithms.

6.2 Primary Evaluation Results (Dataset A: Seeds 42–51)

Dataset A contains 150 runs across ten random seeds, three maze sizes, and five algorithms.

| Maze Size | Algorithm | Path Length | Nodes Expanded | Runtime (s) | Peak Memory (KB) | Replanning Count |
|---|---|---:|---:|---:|---:|---:|
| Small | BFS | 18.00 ± 0.00 | 77.50 ± 8.34 | 0.000214 ± 0.000107 | 5.116 ± 1.675 | — |
| Small | DFS | 32.80 ± 6.75 | 49.20 ± 10.84 | 0.000425 ± 0.000185 | 7.029 ± 2.218 | — |
| Small | A* | 18.00 ± 0.00 | 61.40 ± 13.34 | 0.000224 ± 0.000079 | 6.148 ± 2.250 | — |
| Small | Reactive A* | 23.00 ± 5.75 | 289.70 ± 106.97 | 0.000900 ± 0.000171 | 13.646 ± 0.357 | 5.60 ± 3.20 |
| Small | D* Lite | 23.00 ± 5.75 | 114.40 ± 13.44 | 0.005038 ± 0.001145 | 21.790 ± 3.734 | 5.70 ± 3.43 |
| Medium | BFS | 38.00 ± 0.00 | 306.80 ± 8.60 | 0.000925 ± 0.000240 | 16.153 ± 0.059 | — |
| Medium | DFS | 101.80 ± 16.31 | 312.10 ± 184.23 | 0.002148 ± 0.001672 | 25.764 ± 0.424 | — |
| Medium | A* | 38.00 ± 0.00 | 210.60 ± 42.39 | 0.000975 ± 0.000318 | 22.846 ± 3.847 | — |
| Medium | Reactive A* | 51.00 ± 9.10 | 1800.50 ± 786.67 | 0.009571 ± 0.005964 | 50.440 ± 0.730 | 11.80 ± 4.85 |
| Medium | D* Lite | 51.00 ± 9.10 | 437.20 ± 23.88 | 0.032709 ± 0.008284 | 74.961 ± 8.506 | 11.80 ± 4.85 |
| Large | BFS | 58.00 ± 0.00 | 683.60 ± 11.83 | 0.001626 ± 0.000509 | 49.191 ± 15.589 | — |
| Large | DFS | 190.20 ± 36.10 | 858.40 ± 1152.21 | 0.006628 ± 0.009487 | 71.102 ± 66.134 | — |
| Large | A* | 58.00 ± 0.00 | 414.70 ± 73.63 | 0.001525 ± 0.000512 | 47.970 ± 0.063 | — |
| Large | Reactive A* | 85.60 ± 18.20 | 6333.50 ± 1979.68 | 0.023876 ± 0.015672 | 99.797 ± 0.722 | 22.80 ± 10.11 |
| Large | D* Lite | 85.60 ± 18.20 | 1003.50 ± 75.45 | 0.061565 ± 0.017386 | 149.551 ± 16.697 | 22.70 ± 9.91 |

6.3 Additional Statistical Evaluation Results (Dataset B: Seeds 100–109)

Dataset B contains 150 separate runs using random seeds 100–109. It provides an additional evaluation of the same five algorithms across the same three maze sizes.

| Maze Size | Algorithm | Path Length | Nodes Expanded | Runtime (s) | Peak Memory (KB) | Replanning Count |
|---|---|---:|---:|---:|---:|---:|
| Small | BFS | 18.00 ± 0.00 | 78.80 ± 5.29 | 0.000152 ± 0.000022 | 4.313 ± 0.000 | — |
| Small | DFS | 32.80 ± 6.20 | 56.00 ± 11.67 | 0.000327 ± 0.000147 | 6.705 ± 0.252 | — |
| Small | A* | 18.00 ± 0.00 | 63.70 ± 10.86 | 0.000177 ± 0.000032 | 5.797 ± 0.027 | — |
| Small | Reactive A* | 22.20 ± 5.20 | 256.20 ± 59.73 | 0.000627 ± 0.000166 | 13.636 ± 0.544 | 4.00 ± 1.89 |
| Small | D* Lite | 22.20 ± 5.20 | 112.20 ± 13.95 | 0.004633 ± 0.000800 | 21.379 ± 3.059 | 4.00 ± 1.89 |
| Medium | BFS | 38.00 ± 0.00 | 296.40 ± 18.20 | 0.000439 ± 0.000035 | 16.172 ± 0.000 | — |
| Medium | DFS | 90.60 ± 16.81 | 305.90 ± 88.86 | 0.001168 ± 0.000289 | 25.608 ± 0.302 | — |
| Medium | A* | 38.00 ± 0.00 | 207.00 ± 53.50 | 0.000500 ± 0.000149 | 22.830 ± 3.831 | — |
| Medium | Reactive A* | 57.00 ± 12.01 | 1986.40 ± 763.22 | 0.005213 ± 0.003217 | 50.709 ± 1.967 | 15.40 ± 4.60 |
| Medium | D* Lite | 57.00 ± 12.01 | 456.90 ± 33.91 | 0.020073 ± 0.004095 | 75.175 ± 9.302 | 15.40 ± 4.60 |
| Large | BFS | 58.00 ± 0.00 | 676.60 ± 13.83 | 0.001034 ± 0.000140 | 43.153 ± 15.589 | — |
| Large | DFS | 210.60 ± 36.01 | 944.30 ± 706.19 | 0.003510 ± 0.002596 | 57.813 ± 15.787 | — |
| Large | A* | 58.00 ± 0.00 | 458.20 ± 68.39 | 0.001048 ± 0.000137 | 47.892 ± 0.060 | — |
| Large | Reactive A* | 82.60 ± 18.60 | 5484.10 ± 1781.49 | 0.014322 ± 0.004686 | 99.323 ± 0.923 | 21.10 ± 7.52 |
| Large | D* Lite | 82.80 ± 19.14 | 979.40 ± 61.51 | 0.043721 ± 0.007529 | 147.605 ± 10.592 | 21.30 ± 7.94 |

6.4 Summary of Observed Results

The experimental results show several consistent patterns across both independent evaluations.

In the fully observable scenario, BFS and A* produced identical mean path lengths for all three maze sizes. A* generally expanded fewer nodes than BFS, particularly in medium and large mazes. DFS expanded fewer nodes than the other fully observable algorithms in some cases, but it produced considerably longer paths and showed higher variability in several measurements.

In the partially observable scenario, Reactive A* and D* Lite produced similar mean path lengths. However, D* Lite expanded substantially fewer nodes than Reactive A* across all maze sizes in both evaluations. For example, in the large mazes of Dataset A, D* Lite expanded an average of 1003.50 nodes, compared with 6333.50 for Reactive A*.

The mean path length and computational requirements increased as maze size increased. This pattern was particularly noticeable for the partially observable algorithms, which needed to discover obstacles and update their navigation plans during movement.

The recorded replanning counts and obstacles-discovered counts are identical within each algorithm and maze-size group in both datasets. These measures therefore describe the same recorded count in the present experimental results and should not be interpreted as independent evidence.

Runtime and peak-memory measurements show higher values for D* Lite than Reactive A* in these experiments. However, the measurement implementations differ, and these figures should be interpreted with the methodological limitations described in Section 5.5.

All 300 runs across the two independent evaluations were successful. The results support a comparison of algorithm behaviour within the implemented simulation, while comparisons between fully observable and partially observable algorithms must account for their different information conditions.
7. Discussion

7.1 Fully Observable Pathfinding Algorithms

The results show that BFS and A* consistently produced the same mean path lengths across all three maze sizes in both evaluations. This is consistent with their shortest-path behaviour in the four-directional grid environment when movement costs are equal.

A* generally expanded fewer nodes than BFS, particularly in medium and large mazes. This indicates that the Manhattan distance heuristic helped guide the search towards the goal and reduced the number of explored positions in several test cases.

DFS demonstrated a different behaviour. Although it sometimes expanded fewer nodes than BFS and A*, it generally produced longer paths. Its path length also showed considerable variation across random seeds, particularly in large mazes. These results illustrate the trade-off between exploration strategy and route quality.

7.2 Partially Observable Pathfinding Algorithms

Reactive A* and D* Lite were evaluated in environments where the robot initially had incomplete knowledge of the maze and discovered obstacles during navigation.

Both algorithms produced similar mean path lengths within each evaluation. However, D* Lite consistently expanded fewer nodes than Reactive A* across all maze sizes in both datasets. This indicates that the incremental search information maintained by the implemented D* Lite approach reduced its recorded search effort compared with repeatedly applying A* to the updated known map.

Despite expanding fewer nodes, D* Lite recorded higher execution-time and peak-memory values than Reactive A* in these experiments. These results should not be interpreted as evidence that D* Lite is inherently slower or less memory-efficient. The measurement implementations differ, as explained in Section 5.5, and the recorded values include implementation-specific overhead.

7.3 Effect of Maze Size

Increasing maze size generally increased the number of nodes expanded, execution time, and peak memory usage. This pattern was particularly noticeable in the partially observable algorithms, which had to discover more obstacles and perform additional planning work in larger environments.

DFS also showed considerable variability in large mazes. Its search behaviour depends on the order in which neighbouring cells are explored, which can affect the route found and the number of positions visited.

The results demonstrate that maze size is an important factor when evaluating pathfinding algorithms. Performance observed in small mazes should not automatically be assumed to represent behaviour in larger environments.

7.4 Comparison Across Independent Evaluations

The two evaluations used separate random seed ranges and were analysed independently. Several broad patterns appeared in both datasets: BFS and A* produced identical mean path lengths, DFS generally produced longer routes, and D* Lite expanded fewer nodes than Reactive A* in the partially observable scenario.

The results also show variation between the datasets. For example, the mean path lengths and computational measurements for some algorithms differed between the two seed sets. This reinforces the importance of evaluating algorithms across multiple maze configurations rather than relying on a single set of generated environments.

The datasets are not pooled because they represent separate experimental evaluations. Their results provide additional evidence of recurring patterns but do not replace the need for further controlled experiments.

7.5 Interpretation and Practical Implications

No single algorithm was best across every performance measure in the implemented experiments.

For fully observable environments, BFS and A* consistently found shortest paths, while A* generally reduced search effort compared with BFS. DFS may require fewer explored nodes in some cases, but its longer routes make it less suitable when shortest-path quality is important.

For partially observable environments, D* Lite expanded fewer nodes than Reactive A*, while Reactive A* recorded lower runtime and peak-memory values in the available measurements. The measurement differences must be considered when interpreting this trade-off.

The choice of pathfinding algorithm therefore depends on the available environmental information and the performance requirements of the navigation task. Path length, search effort, execution time, memory usage, and replanning behaviour should be considered together.
8. Conclusion and Future Work

8.1 Conclusion

This study implemented and evaluated five pathfinding algorithms for maze-solving robot navigation: Breadth-First Search (BFS), Depth-First Search (DFS), A*, Reactive A*, and D* Lite. The evaluation considered both fully observable and partially observable navigation scenarios across small, medium, and large maze configurations.

Two independent experimental evaluations were conducted, each containing 150 runs across ten random seeds, three maze sizes, and five algorithms. All 150 runs in each dataset completed successfully. The results were analyzed separately to preserve the independence of the two evaluations.

The experimental findings show that BFS and A* consistently produced the shortest recorded paths in the fully observable scenarios. A* generally expanded fewer nodes than BFS, demonstrating the benefit of heuristic-guided search. DFS found valid routes but often produced longer paths and greater variation in performance.

In partially observable scenarios, Reactive A* and D* Lite successfully navigated the tested environments. D* Lite generally expanded fewer nodes than Reactive A*, while its recorded execution time and memory usage were higher in the reported experiments. These measurements must be interpreted with the differences in measurement implementation in mind.

The results also demonstrate that maze size affects search effort, execution time, and memory requirements. No single algorithm was best across every measured metric. Algorithm selection therefore depends on the navigation environment, available computational resources, and whether the environment is fully or partially observable.

Overall, the project demonstrates the implementation and experimental comparison of classical and incremental pathfinding approaches for autonomous maze navigation. The two independent evaluations provide evidence of successful operation across the tested configurations, while also highlighting the importance of consistent measurement methods when comparing algorithm performance.

8.2 Contributions

The main contributions of this work are:

1. Implementation of five pathfinding algorithms: BFS, DFS, A*, Reactive A*, and D* Lite.
2. Development of a maze-solving simulation environment supporting fully observable and partially observable navigation.
3. Evaluation across three maze sizes using two independent datasets, each containing 150 experimental runs.
4. Collection and analysis of performance metrics, including path length, nodes expanded, execution time, memory usage, and replanning counts where applicable.
5. Comparison of the observed strengths and limitations of the implemented algorithms under the tested conditions.

8.3 Limitations

The findings should be considered in light of the following limitations:

1. The experiments were conducted in a software simulation rather than on a physical robot.
2. The evaluation covered only three maze sizes and ten random seeds per dataset.
3. The generated maze configurations and obstacle-placement rules may not represent every real-world navigation environment.
4. Both datasets recorded successful completion in all runs; consequently, the experiments do not provide evidence about performance in scenarios where no valid route exists.
5. The hardware and software environment for the additional statistical evaluation dataset was not documented sufficiently for a direct environment-controlled comparison with the primary dataset.
6. The D* Lite measurement implementation differed from the external measurement approach used for other algorithms in the additional evaluation. Runtime and memory comparisons should therefore be interpreted cautiously.
7. Node-expansion counters are implementation-specific and may not represent identical units of computational work across algorithms.

8.4 Future Work

Several improvements can extend this research:

1. **Physical robot implementation:** Deploy the algorithms on a mobile robot equipped with appropriate sensors to evaluate real-world navigation performance.
2. **Larger and more diverse environments:** Test additional maze dimensions, obstacle densities, layouts, and obstacle distributions.
3. **Expanded statistical evaluation:** Increase the number of random seeds and experimental repetitions to obtain more robust statistical estimates.
4. **Standardized benchmarking:** Use a common measurement framework for execution time and memory consumption across all algorithms and datasets.
5. **Consistent performance definitions:** Establish standardized definitions for node expansion, replanning, and obstacle discovery to improve cross-algorithm comparisons.
6. **Additional statistical analysis:** Include confidence intervals and suitable statistical significance tests when comparing algorithm performance.
7. **Additional algorithms:** Extend the comparison to other search and replanning approaches, such as Dijkstra's algorithm, Lifelong Planning A* (LPA*), and other incremental pathfinding methods.
8. **Dynamic environments:** Investigate environments with moving obstacles and changing navigation conditions.

8.5 Final Remarks

The study provides a comparative foundation for understanding how different pathfinding strategies behave in simulated maze-navigation tasks. The results emphasize that shortest-path quality, search effort, execution time, memory consumption, and replanning capability should be considered together when selecting a navigation algorithm. Further work involving standardized experiments and physical robot testing can help establish how these findings translate to practical autonomous navigation systems.

References
[1] Hart, P. E., Nilsson, N. J., and Raphael, B. (1968). A formal basis for the heuristic determination of minimum cost paths. IEEE Transactions on Systems Science and Cybernetics, 4(2), 100–107. https://doi.org/10.1109/TSSC.1968.300136.

[2] Korf, R. E. (1985). Depth-first iterative-deepening: An optimal admissible tree search. Artificial Intelligence, 27(1), 97–109.

[3] Lumelsky, V. J., and Stepanov, A. A. (1987). Path-planning strategies for a point mobile automaton moving amidst unknown obstacles of arbitrary shape. Algorithmica, 2, 403–430.

[4] Stentz, A. (1994). Optimal and efficient path planning for partially-known environments. In Proceedings of the IEEE International Conference on Robotics and Automation (ICRA), 3310–3317.

[5] Yamauchi, B. (1997). A frontier-based approach for autonomous exploration. In Proceedings of the IEEE International Symposium on Computational Intelligence in Robotics and Automation, 146–151.

[6] Koenig, S., and Likhachev, M. (2002). D* Lite. In Proceedings of the AAAI Conference on Artificial Intelligence, 476–483.

[7] Koenig, S., Likhachev, M., and Furcy, D. (2004). Lifelong Planning A*. Artificial Intelligence, 155(1–2), 93–146.

[8] Cui, X., and Shi, H. (2011). A*-based pathfinding in modern computer games. International Journal of Computer Science and Network Security, 11(1), 125–130.

[9] Agcaoili, C. J., Bernabe, X. Y., and Agustin, V. A. (2023). Hybridization of A* Pathfinding and Hierarchical Pathfinding A* Algorithm for Pathfinding in Grid Based Games. UIJRT, 4(8), 14–22.

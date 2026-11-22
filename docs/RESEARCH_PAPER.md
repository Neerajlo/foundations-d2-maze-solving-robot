Week 13 — Research Paper Draft
Weekly Plan
| Day | Task | Status |

|---|---|---|

| Monday | Abstract and Introduction | Drafted |

| Tuesday | Literature Review | Drafted |

| Wednesday | Methodology | Drafted |

| Thursday | Experimental Setup | Drafted |

| Friday | Read aloud and revise | Pending |

Week 13 Goal: Draft Sections 1–5.
1. Abstract
Path planning is an important problem in mobile robotics, where an agent must identify a safe and suitable route from a starting position to a specified destination while avoiding obstacles. This study presents a simulation-based maze-solving framework developed to examine and compare different search algorithms under fully observable and partially observable environments. The framework implements Breadth-First Search (BFS), Depth-First Search (DFS), A*, Reactive A*, and D* Lite using four-directional movement in a grid-based maze environment. The Manhattan distance heuristic is used for heuristic-based path planning.

In fully observable environments, BFS, DFS, and A* are evaluated using complete maze information. In partially observable environments, Reactive A* and D* Lite are examined in situations where the agent discovers obstacles during navigation and may need to replan its route. The experimental evaluation uses three maze sizes and ten random seeds. BFS, DFS, and A* are evaluated in fully observable environments, while Reactive A* and D* Lite are evaluated in partially observable environments, resulting in 150 experiment runs. Performance is examined using metrics including path length, nodes expanded, execution time, peak memory usage, replanning activity, and obstacles discovered. All 150 experiment runs completed successfully.

The study provides a comparative simulation framework for understanding the behaviour of classical and replanning-based search algorithms in different maze-observation conditions. It also highlights the importance of evaluating path-planning approaches using multiple performance measures rather than relying on a single metric.

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

The experimental evaluation covers three maze sizes and ten random seeds, producing 150 experiment runs. The study focuses on simulation results and algorithmic performance. It does not include physical robot construction, real-world sensor integration, or testing in an actual outdoor or indoor robotic environment.
3. Literature Review
Path planning is a fundamental problem in mobile robotics and artificial intelligence. Researchers have developed several search and navigation techniques to help autonomous agents find routes, avoid obstacles, and respond to changes in their environments. The existing literature covers classical graph-search algorithms, heuristic-based pathfinding, reactive navigation, and incremental replanning. These studies provide the theoretical foundation for the algorithms implemented in this maze-solving project.
3.1 Classical Search and Heuristic-Based Pathfinding
Hart, Nilsson, and Raphael (1968) introduced the A* search algorithm and established its theoretical properties. A* uses both the cost of the path already travelled and a heuristic estimate of the remaining distance to the goal. The study established that an admissible heuristic can help A* find an optimal path. This work provides the foundation for using A* in the present project, where Manhattan distance is used as the heuristic for four-directional grid movement [1].

Korf (1985) introduced Depth-First Iterative-Deepening (DFID), a search approach that combines the memory advantages of depth-first search with repeated depth-limited exploration. The study highlights the importance of memory efficiency in search problems. This is relevant to the project because memory consumption is included as one of the performance measures when evaluating maze-solving algorithms [2].

Cui and Shi (2011) discussed A*-based pathfinding techniques used in modern computer games. Their work highlights the importance of A* and its optimizations in pathfinding applications. This provides additional support for selecting A* as one of the algorithms evaluated in the grid-based maze environment [8].

Agcaoili et al. (2023) examined the combination of A* pathfinding with Hierarchical Pathfinding A*. Their work considered how hierarchical approaches can reduce search effort in suitable grid-based environments. This study provides a possible direction for extending the current project through hierarchical path planning [9].
3.2 Reactive Navigation and Partially Known Environments
Lumelsky and Stepanov (1987) studied the Bug1 and Bug2 strategies for mobile robot navigation in environments containing unknown obstacles. These strategies demonstrate how a robot can navigate using local environmental information without requiring a complete map in advance. Their work is relevant to the partially observable part of this project, where the robot discovers obstacles while navigating. It also provides a theoretical basis for considering wall-following as a simple reactive navigation approach [3].

Stentz (1994) presented the D* path-planning approach for environments that are only partially known. The research focused on updating a route when new obstacles or environmental changes are discovered. This is closely related to the problem addressed in the project, where a previously planned route may become blocked during navigation and the agent must identify an alternative route [4].

Yamauchi (1997) introduced frontier-based exploration for autonomous mobile robots. This approach uses the boundaries between explored and unexplored regions to guide further exploration. The study demonstrates the importance of systematically exploring unknown environments. Although frontier-based exploration is not the primary focus of the current implementation, it provides a possible direction for future development of the maze-solving system [5].
3.3 Incremental Search and Replanning
Koenig and Likhachev (2002) introduced D* Lite, an incremental heuristic search algorithm designed for path planning in changing or partially known environments. Unlike approaches that calculate a completely new route after every environmental change, D* Lite can reuse previous search information to update the path. This makes the algorithm particularly relevant to navigation scenarios in which obstacles are discovered during movement. D* Lite is implemented and evaluated in the present project as one of the approaches for partial-observation navigation [6].

Koenig, Likhachev, and Furcy (2004) developed Lifelong Planning A* (LPA*), an incremental search algorithm for repeated path-planning tasks. LPA* reuses information from previous searches when only part of the environment changes. Their work provides a broader understanding of incremental search and explains the value of retaining previous search information instead of repeatedly solving the entire problem from the beginning [7].
3.4 Summary of Literature and Research Gap
The reviewed studies establish the importance of different approaches to path planning. BFS and other classical search techniques provide systematic ways to explore known environments. DFS offers a different exploration strategy, while A* uses heuristic information to guide the search towards the goal. Research on Bug algorithms and partially known environments highlights the need for navigation techniques that can respond to locally discovered obstacles. Studies on D* and D* Lite demonstrate how replanning can support navigation when environmental information changes.

However, the performance of these algorithms depends on factors such as maze size, obstacle arrangement, available environmental information, and the need for replanning. Therefore, this project develops a common grid-based simulation framework to examine different algorithms under fully observable and partially observable conditions.

The project implements and evaluates BFS, DFS, and A* in fully observable environments, along with Reactive A* and D* Lite in partially observable environments. Their performance is examined using measures such as path length, nodes expanded, execution time, peak memory usage, replanning activity, and obstacles discovered. Experiments across multiple maze sizes and random seeds provide a consistent basis for comparing their behaviour.

The main contribution of this study is the implementation and experimental comparison of classical search and replanning-based approaches within a common maze-solving simulation. The study focuses not only on finding a route but also on understanding how the algorithms behave when the agent has incomplete knowledge of its environment.
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
4. Methodology
4.1 Research Design
This study uses a simulation-based experimental approach to evaluate five pathfinding algorithms in grid-based maze environments. The algorithms are Breadth-First Search (BFS), Depth-First Search (DFS), A*, Reactive A*, and D* Lite.

The experiments are divided into two scenarios: fully observable and partially observable environments. In the fully observable scenario, the algorithms BFS, DFS, and A* operate with complete knowledge of the maze. In the partially observable scenario, Reactive A* and D* Lite operate with incomplete knowledge and discover obstacles during navigation.

The performance of the algorithms is evaluated using success rate, path length, number of nodes expanded, execution time, peak memory usage, replanning count, and number of discovered obstacles. Since the algorithms are evaluated under different observation conditions, comparisons are made primarily within their respective scenarios rather than as a direct ranking of all five algorithms under identical conditions.
4.2 Maze Environment and Generation
The environment is represented as a two-dimensional grid. Each cell represents a possible robot position. A value of 0 represents a free cell, while a value of 1 represents an obstacle.

The robot starts at the top-left position, (0, 0), and the goal is located at the bottom-right position. Movement is restricted to four directions: up, down, left, and right. Each valid movement has a cost of one.

Random mazes are generated using a custom Python maze-generation function. The generator first creates a free grid and constructs a continuous route between the starting position and the goal. It then places obstacles randomly in cells outside this route, using a probability of 25%.

Fixed random seeds are used to make maze generation reproducible. The experiments use three maze dimensions: 10 × 10, 20 × 20, and 30 × 30. Ten seeds, from 42 to 51, are used for each maze size.
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

h(n) = |x₁ − x₂| + |y₁ − y₂|

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
The experiments are conducted using Python. Three maze sizes and ten fixed random seeds are used to create the test environments.

For every generated maze, five algorithms are evaluated:
- BFS, DFS, and A* in the fully observable scenario.
- Reactive A* and D* Lite in the partially observable scenario.
A fresh copy of the generated maze is provided to each algorithm. This ensures that changes made during one algorithm's execution do not affect the maze used by another algorithm.

The total number of experiments is calculated as:

Total experiments = 10 seeds × 3 maze sizes × 5 algorithms = 150 runs.

The experiment runner collects the output from each run and stores the results for further analysis. It also records unsuccessful runs and any errors encountered during execution.
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

The experimental results are saved in three files: experiment_results.csv for individual run results, experiment_summary.csv for statistical summaries, and experiment_failures.csv for unsuccessful runs.

These results provide the basis for comparing the behaviour and performance of the five pathfinding algorithms under the two observation scenarios.
4.8 Experimental Limitations
The experiments are conducted in a software simulation using generated grid mazes. The results therefore describe algorithm behaviour in this controlled environment and should not be treated as direct evidence of performance on a physical robot.

The algorithms are also evaluated under two different information conditions: BFS, DFS, and A* receive the complete maze, while Reactive A* and D* Lite discover obstacles during navigation. Consequently, comparisons between algorithms are interpreted in the context of their respective scenarios.

The maze generator creates a guaranteed free route from the start to the goal and places obstacles outside that route. This supports repeatable solvable test cases, but it does not represent every possible maze structure or real-world obstacle distribution. These constraints should be considered when interpreting the results.
5. Experimental Setup
5.1 Hardware Configuration
All experiments were conducted on a personal computer running Windows 10 Home Single Language (64-bit). The system configuration used for the experiments is listed below.

| Component | Specification |

|---|---|

| Processor | 13th Gen Intel Core i5-1335U |

| Number of CPU cores | 10 |

| Logical processors | 12 |

| Installed RAM | Approximately 16 GB |

| Operating System | Windows 10 Home Single Language |

| System Architecture | 64-bit |

The experiments were executed locally on this computer. No physical robot or external hardware was used because the study focuses on simulation-based maze navigation.
5.2 Software Configuration
The project was implemented and executed using Python. The Python interpreter installed on the system was version 3.14.3.

The following Python packages were installed and available in the system-wide Python environment. They support experiment analysis, visualisation, automated testing, and document preparation:

| Package | Version | Purpose |

|---|---|---|

| Python | 3.14.3 | Main programming language |

| Matplotlib | 3.11.2 | Generating charts and visualisations |

| Pandas | 3.1.1 | Data handling and tabular analysis |

| Pytest | 9.2.0 | Automated testing |

| python-docx | 1.2.0 | Working with Word documents |

The project dependencies are listed in the requirements.txt file. The experiments were executed using the system-wide Python installation rather than a separate project-specific virtual environment.
5.3 Experimental Configuration
The experimental setup uses three maze dimensions: 10 × 10, 20 × 20, and 30 × 30. Ten fixed random seeds, ranging from 42 to 51, are used for generating reproducible maze layouts.

The five algorithms are divided according to the observation scenario. BFS, DFS, and A* are tested in fully observable environments, while Reactive A* and D* Lite are tested in partially observable environments.

For each generated maze, a separate copy is provided to every algorithm. This prevents modifications made during one algorithm's execution from affecting the other experiments.

The complete experiment configuration consists of:
- 3 maze dimensions
- 10 random seeds for each dimension
- 3 algorithms in the fully observable scenario
- 2 algorithms in the partially observable scenario
- 150 total experiment runs
5.4 Experiment Execution
The experiments are executed through the main Python script, run_experiments.py.

The script generates mazes using the specified dimensions and random seeds. It then executes the selected algorithms under their corresponding observation scenarios. Each experiment is recorded separately with its maze identifier, dimensions, seed, scenario, and algorithm name.

The script also handles unsuccessful runs and records error information when an exception occurs. This helps maintain a record of experiment outcomes instead of silently ignoring failed executions.
5.5 Performance Measurement Tools
Python's built-in measurement facilities are used to collect performance information.

The time.perf_counter() function measures algorithm execution time in seconds. The tracemalloc module tracks Python memory allocations and records peak traced memory during execution. This value represents Python-tracked allocations rather than the complete memory consumption of the operating system or every native library.

The experiment runner records the following performance information:
1. Success or failure of the algorithm.
2. Path length.
3. Number of nodes expanded.
4. Execution time in seconds.
5. Peak traced memory usage in kilobytes.
6. Number of replanning operations.
7. Number of obstacles discovered.
For D* Lite, the partial-observation navigation function performs its own runtime and peak-memory measurements. The resulting measurements are included in the experiment records.
5.6 Result Storage and Organization
The experimental results are saved in CSV format inside the results directory. Three output files are generated:

| File | Description |

|---|---|

| experiment_results.csv | Stores the individual results of all experiment runs. |

| experiment_summary.csv | Stores statistical summaries grouped by scenario, maze size, and algorithm. |

| experiment_failures.csv | Stores unsuccessful experiment cases and their associated error information. |

The statistical summary includes the mean, standard deviation, minimum, and maximum values for the recorded metrics. Success rate is represented as a percentage. Path-length statistics are calculated using successful runs, while other performance metrics are summarised using all runs in the corresponding group.

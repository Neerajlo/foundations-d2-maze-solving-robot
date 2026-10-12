# Literature Review
## D2: Maze-Solving Robot
Track D · Foundations of AI

## 1. Why This Literature Matters

Our module asks a simulated robot to reach a goal in a grid maze, first with a complete map and then with only what it has actually seen. This involves two related problems: offline shortest-path search using BFS, DFS and A*, and online replanning under partial observability using reactive navigation and D* Lite.

The following literature covers both problems. It includes foundational research that introduced important algorithms and comparative studies that help us understand their behaviour. These papers will guide our own experiments and help us justify our algorithm choices.

## 2. Literature Table

| # | Paper (Author, Year) | What They Did | Data / Domain | Key Result | What We Can Borrow |
|---|---|---|---|---|---|
| 1 | Hart, Nilsson & Raphael, "A Formal Basis for the Heuristic Determination of Minimum Cost Paths" (1968) | Introduced A* and established its theoretical properties for heuristic search. | Graph-search theory, motivated by robot route planning. | A* can find an optimal path when its heuristic satisfies the required conditions. | Use Manhattan distance as the heuristic for four-direction grid movement and compare A* with BFS. |
| 2 | Korf, "Depth-First Iterative-Deepening: An Optimal Admissible Tree Search" (1985) | Introduced IDA*, combining depth-first exploration with a cost bound. | Sliding-tile puzzles and other search-tree problems. | IDA* reduces memory requirements by using depth-first search, but may revisit nodes across iterations. | Discuss memory-efficient search as a possible alternative when memory becomes a limitation. |
| 3 | Putra et al., "Comparison of Breadth-First Search (BFS) and Depth-First Search (DFS) Algorithms for Shortest Search in Campus Maze" (2025) | Compared BFS and DFS using a campus-maze simulation and evaluated performance. | Campus layout represented as an unweighted graph, with 20 room/location nodes. | The paper reports differences in execution speed, memory use and shortest-path behaviour between BFS and DFS. | Compare BFS and DFS using path length, nodes expanded, runtime and memory on our generated mazes. |
| 4 | Stentz, "Optimal and Efficient Path Planning for Partially-Known Environments" (1994) | Introduced D*, which repairs a path when new obstacles are discovered rather than always planning from scratch. | Outdoor mobile-robot navigation with a partially known terrain map. | D* supports path planning in partially known environments and updates plans as new information becomes available. | Explain why replanning is important when our robot discovers previously unknown walls. |
| 5 | Yamauchi, "A Frontier-Based Approach for Autonomous Exploration" (1997) | Introduced frontier-based exploration, using boundaries between explored and unexplored areas to guide a robot. | Mobile-robot mapping in cluttered office environments using sonar. | Frontier-based exploration supports mapping without requiring a complete map in advance. | Represent known and unknown cells and explain how the robot can discover the maze incrementally. |
| 6 | Koenig & Likhachev, "D* Lite" (2002) | Presented D* Lite, an incremental heuristic-search method based on Lifelong Planning A*. | Simulated and real navigation and mapping in unknown terrain. | The authors demonstrated the benefits of incremental heuristic search for replanning. | Use D* Lite as the planned method for updating routes after discovering new obstacles. |
| 7 | Koenig, Likhachev & Furcy, "Lifelong Planning A*" (2004) | Developed LPA*, which reuses information from previous searches when a graph changes. | Theoretical analysis and path-planning experiments. | Reusing previous search information can reduce repeated search effort when changes are limited. | Compare incremental replanning with repeatedly running A* from scratch. |
| 8 | Elkari et al., "Exploring Maze Navigation: A Comparative Study of DFS, BFS, and A* Search Algorithms" (2024) | Compared DFS, BFS and A* for maze path planning using Python and the Pmaze library. | Generated maze configurations containing dead ends, loops and multiple possible paths. | The study examines trade-offs in path cost and algorithmic complexity across the three methods. | Follow a direct comparison structure and report path length, nodes expanded, runtime and performance across maze sizes. |
| 9 | Beamer, Asanović & Patterson, "Direction-Optimizing Breadth-First Search" (2013) | Introduced a BFS optimisation that switches between top-down and bottom-up traversal. | Large synthetic graphs and real social-network graphs on multicore systems. | The paper reports speedups over a baseline BFS on the evaluated large-graph workloads. | Use this paper as background on BFS optimisation, while noting that its large-graph setting differs from our grid mazes. |

## 3. What This Literature Tells Us

Two important lessons emerge from these papers.

First, improved algorithms should be compared with a clearly defined baseline. Our project can use BFS and DFS as uninformed-search baselines, A* as heuristic search, and D* Lite for incremental replanning.

Second, algorithm performance depends on the problem and the metric being measured. BFS can find shortest paths in unweighted graphs, DFS does not guarantee the shortest path, A* uses a heuristic to guide search, and incremental algorithms can reuse previous search information.

Therefore, our experiments should consider path length, nodes expanded, execution time, memory usage and performance across different maze sizes. We should report limitations as well as successful results.

## 4. Backup Datasets / Domains

### Dataset 1: Moving AI Lab Pathfinding Benchmarks

Source:https://www.movingai.com/benchmarks/grids.html

The Moving AI Lab provides public grid maps and benchmark scenarios for evaluating pathfinding algorithms. For our project, we downloaded the `maze512-1-0.map` map file and its corresponding `maze512-1-0.map-scen` scenario file.

The map is a 512 × 512 grid. This dataset can be used to test our pathfinding algorithms on an external benchmark instead of relying only on randomly generated mazes. Before running experiments, we must verify the map format, movement rules, and start and goal positions specified by the scenario.
The first scenario entry in `maze512-1-0.map-scen` specifies a start position of (477, 130), a goal position of (476, 131), and a reference path length of 2.0. These values must be interpreted using the benchmark's coordinate convention before running the experiment.

### Dataset 2: Gymnasium Environments

Source: https://gymnasium.farama.org/environments/toy_text/frozen_lake/

Gymnasium provides public reinforcement-learning environments, including FrozenLake-v1. FrozenLake is a grid-world environment in which an agent moves from a starting state toward a goal while avoiding holes. Its slippery version can cause movement to differ from the intended action. It can therefore serve as a secondary grid-navigation environment for exploratory testing. However, it is not a conventional maze-map benchmark like Moving AI, and its transition rules differ from our project's four-direction maze movement. We will treat it as a separate environment rather than directly combining its results with our maze experiments.


## 5. Selected Methods and Reasons

| Method | Purpose in Our Project | Reason for Selection |
|---|---|---|
| BFS | Baseline search on a fully known maze | Finds a shortest path in an unweighted maze and provides a reference for comparisons. |
| DFS | Alternative uninformed search | Allows us to compare exploration behaviour, path length and memory usage with BFS. |
| A* | Heuristic pathfinding | Uses Manhattan distance to guide search toward the goal in four-direction movement. |
| Reactive navigation / repeated A* | Navigation with partial observation | Allows the robot to update its knowledge and replan when it discovers a wall. |
| D* Lite | Incremental replanning | Reuses previous search information to handle changes in the discovered map. |

We will compare the selected methods using consistent maze configurations and clearly recorded metrics. Our existing BFS implementation from Week 2 provides the starting baseline. Further algorithms and partial-observation behaviour will be evaluated as the project progresses.

## 6. References

1. Hart, P. E., Nilsson, N. J., & Raphael, B. (1968). A formal basis for the heuristic determination of minimum cost paths. *IEEE Transactions on Systems Science and Cybernetics*, 4(2), 100–107.

2. Korf, R. E. (1985). Depth-first iterative-deepening: An optimal admissible tree search. *Artificial Intelligence*, 27(1), 97–109.

3. Putra, A. A. D., Maulana, A. N., Febrianti, S. B., Camelia, N., Hutagalung, S. K., & Khudori, A. N. (2025). Comparison of Breadth-First Search (BFS) and Depth-First Search (DFS) Algorithms for Shortest Search in Campus Maze. *JESICA: Journal of Enhanced Studies in Informatics and Computer Applications*, 2(2), 43–51.

4. Stentz, A. (1994). Optimal and efficient path planning for partially-known environments. *Proceedings of the 1994 IEEE International Conference on Robotics and Automation*, 3310–3317.

5. Yamauchi, B. (1997). A frontier-based approach for autonomous exploration. *Proceedings of the 1997 IEEE International Symposium on Computational Intelligence in Robotics and Automation*, 146–151.

6. Koenig, S., & Likhachev, M. (2002). D* Lite. *Proceedings of the 18th National Conference on Artificial Intelligence (AAAI-02)*, 476–483.

7. Koenig, S., Likhachev, M., & Furcy, D. (2004). Lifelong Planning A*. *Artificial Intelligence*, 155(1–2), 93–146.

8. Elkari, B., Ourabah, L., Sekkat, H., Hsaine, A., Essaiouad, C., Bouargane, Y., & El Moutaouakil, K. (2024). Exploring Maze Navigation: A Comparative Study of DFS, BFS, and A* Search Algorithms. *Statistics, Optimization & Information Computing*, 12, 761–781. https://doi.org/10.19139/soic-2310-5070-1939

9. Beamer, S., Asanović, K., & Patterson, D. (2013). Direction-optimizing breadth-first search. *Scientific Programming*, 21, 137–148. https://doi.org/10.3233/SPR-130370
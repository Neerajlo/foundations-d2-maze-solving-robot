# Literature Review
## D2: Maze-Solving Robot
### Track D – Foundations of AI

## 1. Why This Literature Matters

A maze-solving robot is an autonomous system designed to navigate through a maze from a starting position to a specified goal. The robot may operate using a complete map of the environment or by observing only the cells that it has already explored.

These conditions represent two important problems in artificial intelligence: offline pathfinding and online navigation under partial observability.

Offline pathfinding algorithms such as Breadth-First Search (BFS), Depth-First Search (DFS), and A* search are used to find paths in a known maze. Online navigation approaches such as reactive path planning and incremental replanning help robots respond when new obstacles or unknown areas are discovered.

This literature review examines foundational research and comparative studies related to maze-solving, heuristic search, autonomous exploration, and dynamic path planning. The findings provide a theoretical foundation for implementing and evaluating algorithms in our project.

## 2. Literature Review Table

| No. | Paper (Author, Year) | What They Did | Data / Domain | Key Result | What We Can Borrow |
|---|---|---|---|---|---|
| 1 | Hart, Nilsson and Raphael (1968) | Introduced the A* search algorithm and established its theoretical properties. | Graph search and path planning | A* can find an optimal path when an admissible heuristic is used. | Use Manhattan distance as a heuristic for grid-based maze navigation. |
| 2 | Korf (1985) | Introduced Iterative Deepening A* (IDA*) for memory-efficient heuristic search. | Tree-search problems | IDA* combines depth-first search with heuristic cost limits to reduce memory requirements. | Consider memory usage when comparing algorithms on larger mazes. |
| 3 | Lumelsky and Stepanov (1987) | Studied Bug1 and Bug2 strategies for robot navigation around unknown obstacles. | Mobile robot navigation | Reactive strategies allow robots to navigate using local sensing without a complete map. | Use wall-following as a baseline for partially observable navigation. |
| 4 | Stentz (1994) | Presented an efficient path-planning approach for partially known environments. | Mobile robot navigation | D* supports replanning when new obstacles or environmental changes are discovered. | Study how a robot can update its route when the maze changes. |
| 5 | Yamauchi (1997) | Introduced frontier-based exploration for autonomous mobile robots. | Unknown environment exploration | Frontier-based exploration helps robots systematically explore unknown regions. | Consider exploration of unexplored maze cells as a future extension. |
| 6 | Koenig and Likhachev (2002) | Presented D* Lite, an incremental heuristic search algorithm. | Dynamic path planning | D* Lite reuses previous search information to efficiently update paths after changes. | Use incremental replanning as a future improvement over repeated A* searches. |
| 7 | Koenig, Likhachev and Furcy (2004) | Developed Lifelong Planning A* (LPA*) for repeated path-planning tasks. | Dynamic graph search | LPA* reuses previous search results when only part of the environment changes. | Understand the benefits of incremental search and compare replanning strategies. |
| 8 | Cui and Shi (2011) | Reviewed A*-based pathfinding techniques used in modern computer games. | Game environments and pathfinding | A* remains an important foundation for efficient pathfinding and its optimizations. | Use A* as a baseline for evaluating pathfinding performance. |
| 9 | Hybridization of A* Pathfinding and Hierarchical Pathfinding A* (2023) | Examined combining heuristic and hierarchical pathfinding approaches. | Grid-based pathfinding | Hierarchical approaches can reduce search effort in suitable environments. | Consider hierarchical pathfinding as a possible future extension. |

## 3. Key Findings from the Literature

The reviewed studies highlight several important findings:

1. BFS is useful for finding shortest paths in unweighted grid mazes, although it may explore many nodes.
2. DFS can explore a maze with relatively low memory requirements but does not guarantee the shortest path.
3. A* uses heuristic information to guide the search towards the goal and can reduce unnecessary exploration.
4. Wall-following provides a simple reactive navigation baseline but may not always find a route in every maze configuration.
5. D* and D* Lite support replanning when the environment changes or new obstacles are discovered.
6. Incremental search methods can reuse previous search information instead of starting the entire search again.

These findings help establish the algorithms and performance measures that should be considered in our experiments.

## 4. Research Gap and Planned Contribution

Although several pathfinding algorithms have been studied extensively, their performance can vary depending on maze size, obstacle density, maze structure, and environmental conditions.

Our project will implement and compare BFS, DFS, and A* in grid-based maze environments using the following performance measures:

- Path length
- Number of nodes expanded
- Execution time
- Peak memory usage
- Whether the goal is successfully reached

The project will also examine navigation under partial observability and consider how reactive navigation and replanning approaches can improve performance when the robot discovers new obstacles.

The experimental results will be used to identify the strengths and limitations of the implemented algorithms. Advanced incremental replanning methods such as D* Lite will be treated as future work unless they are implemented and experimentally evaluated.

## 5. Backup Datasets and Domains

If the generated maze environments are insufficient for additional validation, the following external resources may be considered:

1. Moving AI Lab – Pathfinding Benchmarks: Provides grid-based maps and benchmark scenarios for evaluating pathfinding algorithms.
2. OpenAI Gymnasium – FrozenLake: Provides a grid-based environment that can be used to study navigation under different environmental conditions.
3. Maze environments generated within our project: These will remain the primary experimental datasets to ensure consistency across algorithm comparisons.

External datasets will only be used when their format and experimental conditions are suitable for the project.

## 6. References

1. Hart PE, Nilsson NJ, Raphael B. A formal basis for the heuristic determination of minimum cost paths. IEEE Transactions on Systems Science and Cybernetics. 1968;4(2):100–107. doi:10.1109/TSSC.1968.300136.

2. Korf RE. Depth-first iterative-deepening: An optimal admissible tree search. Artificial Intelligence. 1985;27(1):97–109.

3. Lumelsky VJ, Stepanov AA. Path-planning strategies for a point mobile automaton moving amidst unknown obstacles of arbitrary shape. Algorithmica. 1987;2:403–430.

4. Stentz A. Optimal and efficient path planning for partially-known environments. Proceedings of the IEEE International Conference on Robotics and Automation. 1994:3310–3317.

5. Yamauchi B. A frontier-based approach for autonomous exploration. Proceedings of the IEEE International Symposium on Computational Intelligence in Robotics and Automation. 1997:146–151.

6. Koenig S, Likhachev M. D* Lite. Proceedings of the AAAI Conference on Artificial Intelligence. 2002:476–483.

7. Koenig S, Likhachev M, Furcy D. Lifelong Planning A*. Artificial Intelligence. 2004;155(1–2):93–146.

8. Cui X, Shi H. A*-based pathfinding in modern computer games. International Journal of Computer Science and Network Security. 2011;11(1):125–130.

9. Hybridization of A* pathfinding and hierarchical pathfinding A*. 2023. [Bibliographic details require verification before final submission.]
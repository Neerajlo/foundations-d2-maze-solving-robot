Literature Review
D2: Maze-Solving Robot
Track D · Foundations of AI 
1. Why this literature matters
Our module asks a simulated robot to reach a goal in a grid maze, first with a complete map and then with only what it has actually seen. That is really two problems glued together: offline shortest-path search (BFS, DFS, A*) and online replanning under partial observability (reactive A*, D* Lite). The literature below was chosen to cover both halves, from the foundational papers that defined the algorithms we are implementing to more recent comparative studies that show how they behave in practice — which is the part our own experiments (Section 5, Rule 4) need to speak to honestly.
2. Literature table
#	Paper (Author, Year)	What they did	Data / Domain	Key result	What we can borrow
1	Hart, Nilsson & Raphael, “A Formal Basis for the Heuristic Determination of Minimum Cost Paths” (1968)	Introduced the A* algorithm and proved it is complete and optimal for an admissible heuristic, and that no other algorithm using the same heuristic expands fewer nodes	Graph search theory; originally motivated by the Shakey robot's route planning	A* with an admissible heuristic guarantees the shortest path while typically expanding far fewer nodes than uninformed search	The Manhattan-distance heuristic and the admissibility argument for why A* should beat BFS on our grid mazes
2	Korf, “Depth-First Iterative-Deepening: An Optimal Admissible Tree Search” (1985)	Introduced IDA*, combining depth-first search with A*'s cost bound to get A*-quality solutions in linear space	Sliding-tile puzzles and other exponential tree-search domains	IDA* is asymptotically optimal in time, space, and solution cost, at the cost of re-visiting nodes across iterations	A concrete answer to “BFS runs out of memory before it finds anything” — worth reporting as a memory-bounded alternative on our largest maze
3	Lumelsky & Stepanov, “Path-Planning Strategies for a Point Mobile Automaton Moving Amidst Unknown Obstacles of Arbitrary Shape” (1987)	Defined the Bug1/Bug2 family: minimal-sensing reactive strategies (move toward goal, follow obstacle boundary on contact) with proven worst-case path-length bounds	A point robot with only local/contact sensing, no map	Guarantees the robot reaches the goal (if reachable) using only local information, with a provable path-length bound	A useful low-end baseline for our partial-observation phase, and a natural “stupidest thing that works” candidate for Week 4
4	Stentz, “Optimal and Efficient Path Planning for Partially-Known Environments” (1994)	Introduced D*, which plans an initial path like A* but repairs it locally when new obstacles are discovered instead of replanning from scratch	Outdoor mobile-robot navigation with a partially known terrain map	D* finds paths in unknown/changing environments while staying optimal and far more efficient than repeated full A* replans	The core justification for why our module builds toward D* Lite instead of just re-running A* after every wall discovery
5	Yamauchi, “A Frontier-Based Approach for Autonomous Exploration” (1997)	Defined “frontiers” — the boundary between explored and unexplored cells — and used them to drive a robot's exploration decisions	Real mobile robot mapping cluttered office environments with sonar	Frontier-based exploration lets a robot extend its map efficiently in both open and cluttered spaces without a prior map	A clean way to frame our robot's “what does it see, what hasn't it seen yet” bookkeeping in the partial-observation phase
6	Koenig & Likhachev, “D* Lite” (2002)	Built D* Lite on top of Lifelong Planning A*, reproducing D*'s behaviour with a simpler, easier-to-analyse incremental algorithm	Simulated and real goal-directed navigation and mapping in unknown terrain	D* Lite matches D*'s efficiency at replanning after new information while being substantially easier to implement and prove correct	This is the algorithm named directly in Roadmap Step 3 — their worked examples are the closest thing to a spec we have
7	Koenig, Likhachev & Furcy, “Lifelong Planning A*” (2004)	Formalised LPA*, which reuses the search tree from a previous A* run instead of rebuilding it after small changes to the graph	Theoretical analysis plus grid-based path-repair experiments	LPA* provably returns the same solution as a fresh A* search after each update, with far fewer node expansions when changes are local	The theoretical backbone for why incremental replanning should beat naive re-running of A* — useful for explaining our own replan-count numbers
8	Cui & Shi, “A*-based Pathfinding in Modern Computer Games” (2011)	Surveyed A* variants and optimisations used in shipped games, and compared their behaviour on grid maps	Grid-based game maps of varying size	Confirms that plain A*'s node-expansion cost grows quickly with grid size, motivating the optimisations it reviews	Grid-size scaling behaviour we should expect to reproduce in our own three-maze-size comparison
9	“Hybridization of A* Pathfinding and Hierarchical Pathfinding A*”, UIJRT (2023)	Combined A* with HPA* clustering and benchmarked path quality and speed against plain A*	Randomly generated and real-game grid maps	Hierarchical A* variants can be substantially faster than plain A* while staying within about 1% of the optimal path length	A concrete precedent for reporting a speed/quality trade-off table, the same shape Rule 1 asks us for
3. What this tells us before we write any code
Two things stand out across these nine papers, and both map directly onto our roadmap:
●	Every “improved” algorithm here is improved relative to a clearly named baseline — Bug algorithms against blind wandering, D* against full-replan-from-scratch, D* Lite against D*, hierarchical A* against plain A*. That is the same discipline Rule 1 asks of us: our A*/D* Lite results only mean something next to BFS/DFS and repeated-A* baselines.
●	Every one of these methods is reported with an explicit account of where it is expensive — IDA* re-visits nodes, Bug algorithms take long boundary-following detours, plain A* runs out of memory or slows down as the grid grows. None of the source papers hide this. Our own warning about testing on only one maze size is really the same lesson: report the scaling, not just the best case.
4. Backup datasets / domains
In case our generated mazes are not enough for Week 3's “two public datasets” requirement:
●	Moving AI Lab pathfinding benchmarks — a standard grid-map benchmark suite used across the pathfinding literature (including several papers above), useful for validating our A* implementation against externally known optimal path lengths.
●	OpenAI Gym / Gymnasium FrozenLake and Maze environments — grid navigation with configurable stochasticity, usable as a secondary domain for the partial-observation phase if we want a second dataset for Week 9's external-data test.
5. References
1. Hart, P. E., Nilsson, N. J., & Raphael, B. (1968). A formal basis for the heuristic determination of minimum cost paths. IEEE Transactions on Systems Science and Cybernetics, 4(2), 100–107.
2. Korf, R. E. (1985). Depth-first iterative-deepening: An optimal admissible tree search. Artificial Intelligence, 27(1), 97–109.
3. Lumelsky, V. J., & Stepanov, A. A. (1987). Path-planning strategies for a point mobile automaton moving amidst unknown obstacles of arbitrary shape. Algorithmica, 2(1–4), 403–430.
4. Stentz, A. (1994). Optimal and efficient path planning for partially-known environments. Proceedings of the 1994 IEEE International Conference on Robotics and Automation, 3310–3317.
5. Yamauchi, B. (1997). A frontier-based approach for autonomous exploration. Proceedings of the 1997 IEEE International Symposium on Computational Intelligence in Robotics and Automation (CIRA'97), 146–151.
6. Koenig, S., & Likhachev, M. (2002). D* Lite. Proceedings of the 18th National Conference on Artificial Intelligence (AAAI-02), 476–483.
7. Koenig, S., Likhachev, M., & Furcy, D. (2004). Lifelong Planning A*. Artificial Intelligence, 155(1–2), 93–146.
8. Cui, X., & Shi, H. (2011). A*-based pathfinding in modern computer games. International Journal of Computer Science and Network Security, 11(1), 125–130.
9. Hybridization of A* pathfinding and hierarchical pathfinding A*. (2023). United International Journal for Research & Technology, 4(8).
<<<<<<< HEAD
## 6. Research Gap

Existing research covers shortest-path algorithms such as BFS and A*, memory-efficient search methods such as IDA*, and replanning approaches such as D* Lite. However, their performance depends on maze structure, obstacle placement, and whether the environment is fully or partially observable.

This project addresses this practical comparison by evaluating BFS, DFS, and A* on generated grid mazes of different sizes. It records path length, nodes expanded, runtime, and path-found status to compare solution quality and search effort.

**Research question:** How do BFS, DFS, and A* compare in path length and search effort as maze size and structure change?

**Scope limitation:** The current experiments use generated, fully observable mazes. They do not yet establish performance in real-world robot navigation or partially observable environments.
=======


## 6. Member 2 — Autonomous Navigation and Replanning

### 6.1 Partial-Observation Navigation

In a partially observed maze, the robot does not initially know the complete layout. It maintains a discovered map containing known free cells, known walls, and unknown cells. As the robot moves, it observes its surroundings and updates this map.

The ground-truth map represents the complete maze, while the discovered map represents only the information currently available to the robot. The navigation algorithm must plan using the discovered map rather than accessing hidden obstacles directly.

This distinction is important because a path that appears valid on the discovered map may become blocked when the robot observes a previously unknown wall.

### 6.2 Obstacle Discovery and Map Updating

When the robot observes a new obstacle, it updates the corresponding cell in its discovered map. It then checks whether the obstacle affects the current planned route.

If the current route is blocked, the robot must calculate an alternative route. If the route remains valid, it may continue following the existing plan.

The navigation cycle is:

1. Plan a route using the discovered map.
2. Move toward the goal.
3. Observe the surrounding cells.
4. Update the discovered map.
5. Check whether new information invalidates the current route.
6. Replan if necessary.
7. Repeat until the goal is reached or no valid route can be found.

### 6.3 Reactive A* and Incremental Replanning

Reactive A* is the initial approach selected for our project. It runs A* on the currently discovered map and performs another search when newly discovered information blocks the planned route.

D* Lite and Lifelong Planning A* are relevant alternatives because they reuse search information when the planning problem changes. These algorithms may reduce repeated computation, but their benefits must be measured rather than assumed.

The initial implementation will use Reactive A* because it is relatively simple to understand and evaluate. An incremental approach may be considered later if the project has sufficient time and a suitable implementation.

### 6.4 Limitations Relevant to Our Project

The literature suggests several issues that should be investigated during implementation and evaluation:

* Repeatedly running A* may perform unnecessary work when the map changes only slightly.
* An incomplete discovered map can make a planned route appear valid until a hidden obstacle is observed.
* Frequent obstacle discoveries may increase the total number of searches and execution time.
* Incremental algorithms require additional implementation complexity.
* Performance on small generated mazes may not generalize to larger or more complex environments.
* Comparisons are meaningful only when algorithms use consistent maze layouts, movement rules, start positions, goal positions, and observation conditions.

These limitations will guide the project's experiments and should not be interpreted as proof that one algorithm is always better than another.

### 6.5 Proposed Navigation Evaluation

The project will evaluate navigation using generated mazes and a simulated observation model.

The following metrics will be recorded:

* **Replanning count:** Number of additional route searches triggered by newly discovered obstacles.
* **Actual distance travelled:** Number of movement steps taken by the robot.
* **Final path length:** Number of movement steps in the completed route.
* **Nodes expanded:** Number of search nodes processed by the planning algorithm.
* **Execution time:** Time required for planning and navigation.
* **Discovered obstacles:** Number of previously unknown obstacles identified during navigation.
* **Navigation success:** Whether the robot reaches the goal.

The initial comparison will focus on Reactive A*. D* Lite may be evaluated as an alternative if implementation time permits.

### 6.6 Connection to the Existing Experiment

The existing Reactive A* experiment in `notebooks/01_exploration.ipynb` demonstrates a robot discovering an obstacle, updating its discovered map, and replanning when its current route is affected.

The experiment provides an initial proof of concept. Further testing on different maze layouts and obstacle locations is required before drawing general conclusions about navigation performance.

The reported measurements should be taken from the actual experiment outputs and should not be generalized beyond the tested conditions.


## 7. Conclusion and Proposed Direction

The reviewed literature covers both offline pathfinding in known mazes and online navigation in partially observed environments. BFS provides a useful baseline for unweighted grids, while A* uses a heuristic to guide the search toward the goal. Bug algorithms provide alternative navigation strategies when only local information about obstacles is available.

For the partial-observation component, the project will initially use Reactive A*. The robot will maintain a discovered map, observe nearby cells, update the map when it discovers previously unknown walls, and replan when new information invalidates its current route. D* Lite and Lifelong Planning A* are potential alternatives for future comparison because they reuse search information when the planning problem changes.

The experiments should compare algorithms using consistent maze layouts, start and goal positions, movement rules, and observation conditions. Evaluation will consider path length, actual distance travelled, nodes expanded, execution time, replanning count, and navigation success.

The team will retain generated mazes as its primary experimental environment and use suitable public benchmark maps as additional test resources. Final algorithm choices will be based on measured results, implementation feasibility, and the limitations identified in the literature.
>>>>>>> origin/main

# Week 3: Literature Review — Maze-Solving Robot

## 2.1 Literature Review

| Study | Method / Problem | Data or Environment | Main Finding | What We Can Borrow |
|---|---|---|---|---|
| Hart, Nilsson and Raphael (1968) | A* heuristic search | Graph search problems | Introduced a best-first search method using path cost and heuristic estimates | Use A* with Manhattan distance |
| Stentz (1994) | D* incremental search | Robot navigation in partially known environments | Supports replanning when the environment changes or new information becomes available | Motivate future replanning experiments |
| Yamauchi (1997) | Frontier-based exploration | Unknown environments for mobile robots | Robots can explore by moving toward boundaries between known and unknown space | Consider exploration under partial observability |
| Koenig and Likhachev (2002) | D* Lite | Simulated navigation with changing edge costs | Reuses previous search information to improve replanning efficiency | Identify D* Lite as a future extension |
| Koenig and Likhachev (2004) | Lifelong Planning A* | Search problems with changing graph costs | Reuses search results across related search tasks | Compare incremental search as future work |
| Sturtevant (2012) | Grid-based pathfinding benchmarks | Standardized maps and pathfinding instances | Provides benchmark maps for reproducible algorithm evaluation | Use public grid maps to test algorithms |
| Korf (1990) | Real-time heuristic search | Search tasks requiring bounded computation | Investigated heuristic search under real-time constraints | Discuss trade-offs between computation and decisions |
| Dijkstra (1959) | Shortest-path algorithm | Weighted graph networks | Established a systematic shortest-path algorithm | Use shortest-path principles as background for BFS on unweighted grids |

*Note: The findings above are concise summaries of the cited methods, not numerical results reproduced from the original experiments. Verify bibliographic details before submission.*

## 2.2 Public Datasets

1. **Moving AI Lab Grid Benchmarks:** https://www.movingai.com/benchmarks/grids.html  
   Use selected grid maps to evaluate path length and search effort. Record the map collection and individual maps used.

2. **Pathfinding Benchmarks — 2D Grid Maps:** https://benchmarks.pathfinding.ai/2d-benchmarks/grid-maps/  
   Use as a second source to inspect available benchmark maps. Check whether the selected maps overlap with Moving AI before treating the sources as independent datasets.

For each selected map, record its source, dimensions, obstacle layout, start and goal positions, and whether a valid path exists.

## 2.3 Methods Selected and Rationale

- **Breadth-First Search (BFS):** Baseline for finding shortest paths in an unweighted grid.
- **Depth-First Search (DFS):** Baseline for comparison; it does not guarantee a shortest path.
- **A* Search:** Uses the Manhattan-distance heuristic for four-directional movement:
  h(n) = |x_n - x_goal| + |y_n - y_goal|
- **Replanning:** Measure replanning behaviour when new obstacles or changed information affect the route. Treat D* Lite as a proposed extension unless it has actually been implemented and tested.

## 2.4 Evaluation Metrics

- Path length
- Nodes expanded
- Runtime in seconds
- Replan count
- Path found (true/false)

Use the same maze instances and start/goal conditions when comparing algorithms. Report averages and clearly describe the test setup.

## 2.5 Research Gap and Planned Contribution

This project compares BFS, DFS and A* on maze environments using path length, nodes expanded and runtime. Replanning behaviour is also relevant for partially observed environments. The current implementation and experiments will determine which conclusions can be supported; incremental replanning methods such as D* Lite remain future work unless implemented and evaluated.

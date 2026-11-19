# Foundations D2 — Maze Solving Robot

## Project Overview

Track: Foundations D — Robotics and Algorithmic Problem Solving  
Module: D2 — Maze Solving Robot  
Type: Path Finding / Robot Simulation  
Difficulty: Foundation

The objective of this project is to develop a computational **Maze Solving Robot** using Python. The system represents a maze as a grid containing accessible cells and obstacles, defines a starting point and destination, and determines a valid path between them.

The project simulates the movement of a robot through the maze and records the path followed by the robot. The solution is also visualised and evaluated using computational performance measures.

The project demonstrates fundamental concepts of:

- Algorithmic problem solving
- Path finding
- Grid-based navigation
- Robotics logic
- Python programming
- Data analysis
- Computational experimentation
- Result visualisation

The final module will produce a solved maze, the path followed by the robot, and performance information describing the solution.

---

## Objectives

The main objectives of this project are:

1. Represent a maze using a computational grid.
2. Define a starting position and destination position.
3. Identify valid and invalid robot movements.
4. Implement a maze-solving/path-finding algorithm.
5. Simulate robot movement through the maze.
6. Determine a valid path from start to destination.
7. Record the sequence of positions visited by the robot.
8. Visualise the solved maze and robot path.
9. Measure the performance of the maze-solving algorithm.
10. Store experimental results in a reproducible format.

---

## Team

This project is developed collaboratively by a four-member project team.

| Member | Role |
|---|---|
| Member 1 (Neeraj) | Maze / Data Preparation |
| Member 2 (Jasmeet) | Algorithm Development |
| Member 3 (Riya) | Testing / Evaluation |
| Member 4 (Pranav) | Documentation / Research |

All team members are expected to contribute to the repository and understand the complete project pipeline.

---

## Problem Definition

The robot is placed at a predefined starting cell inside a maze.

The maze contains:

- Free cells that the robot can enter.
- Obstacle/wall cells that the robot cannot enter.
- A starting position.
- A destination/goal position.

The objective is to determine a valid sequence of movements that allows the robot to reach the destination without moving through obstacles.

A typical movement may include:

```text
        UP
         ↑
         |
LEFT ← ROBOT → RIGHT
         |
         ↓
       DOWN

## Week 2 – Initial Findings

1. The dataset contains 27 experiment records covering 9 mazes and 3 algorithms.

2. The recorded path lengths range from 18 to 240 steps across the experiments.

3. The number of nodes expanded ranges from 38 to 875 across the experiments.

4. BFS and A* returned equal path lengths on all nine tested mazes, while DFS produced longer paths on the tested configurations.

5. The exploration notebook shows differences in average path length and nodes expanded between BFS, DFS, and A*.

## How to Run the Project

### 1. Generate Maze Data

```bash
python -m src.maze_generator
```

### 2. Run Maze-Solving Experiments

```bash
python -m src.main
```

### 3. Run Tests

```bash
python -m pytest src/ -v
```

## Results

The experiment results are saved in `results/maze_results.csv`. The file records the maze ID, algorithm, path length, nodes expanded, runtime, replanning count, and path-found status.

## Algorithms

* **BFS:** Finds a shortest path in an unweighted maze.
* **DFS:** Explores paths deeply and may return a longer path.
* **A* Search:** Uses a heuristic to guide the search toward the goal.

## Testing

The current test suite contains 9 tests covering maze generation, maze validation, neighbor detection, goal detection, and BFS path finding.

## Research Paper Validation

**Reference paper:**

Hart, P. E., Nilsson, N. J., & Raphael, B. (1968).
A Formal Basis for the Heuristic Determination of Minimum Cost Paths.
IEEE Transactions on Systems Science and Cybernetics, 4(2), 100–107.
https://doi.org/10.1109/TSSC.1968.300136

**Objective:** Validate the shortest-path property of A* on our
generated, unweighted grid mazes using BFS as a baseline.

**Method:** Run BFS and A* on the same nine mazes and compare
their path lengths using `results/maze_results.csv`.

**Observed result:** BFS and A* returned equal path lengths on all
nine tested mazes. Small mazes required 18 steps, medium mazes
38 steps, and large mazes 58 steps.

**Conclusion:** These results are consistent with both algorithms
finding shortest paths on the tested mazes. This is a practical
validation inspired by the paper's minimum-cost path principle,
not an exact reproduction of the original experiment.

**Limitation:** The validation covers only the generated mazes
and configurations tested in this project.

## Wall Following Algorithm

The project includes a Wall Following navigation algorithm implemented in `src/robot.py`.

Its performance was compared with BFS across 9 generated mazes (small, medium, and large), producing 18 experimental records.

- [Wall Following Algorithm Documentation](docs/wall_following_algorithm.md)
- [BFS vs Wall Following Results](results/wall_following_comparison.csv)
- [Comparison Script](compare_wall_following.py)

---

## Week 6 – D* Lite Implementation and Experimental Evaluation

### 1. Objective

The objective of Week 6 was to implement D* Lite for incremental path planning and evaluate its ability to update routes when new obstacles are discovered.

### 2. D* Lite Implementation

D* Lite was implemented in `src/dstar_lite.py`.

The implementation uses:

- **g-values:** Store the current estimated cost from a cell to the goal.
- **rhs-values:** Store the one-step lookahead cost.
- **Priority Queue:** Processes cells according to their calculated priority.
- **Incremental Updates:** Reuses previous search information when obstacles are discovered.
- **Start Movement:** Updates the robot's current position while retaining previous search information.

### 3. Partial-Observation Integration

The D* Lite planner was integrated with the robot simulation.

The robot initially knows only its starting cell. Unknown cells are temporarily assumed to be open for planning. When the robot attempts to enter an obstacle, the obstacle is discovered and the planner updates the route.

Relevant files:

- `src/robot.py`
- `src/partial_observation.py`
- `src/dstar_lite.py`

### 4. Experimental Evaluation

D* Lite was compared with Breadth-First Search (BFS).

A challenging experiment was conducted using the 30 × 30 maze `large_42`.

Twenty-four additional obstacle cells were introduced sequentially. D* Lite updated its existing search information after each obstacle discovery, while BFS performed a fresh search on the final updated maze.

### 5. Experimental Results

| Measurement | D* Lite | BFS |
|---|---:|---:|
| Initial path length | 58 | — |
| Final path length | 60 | 60 |
| Total nodes expanded | 737 | 669 |
| Replanning expansions | 348 | — |
| Navigation successful | Yes | Yes |

Both algorithms found a valid shortest path of 60 steps after the obstacles were introduced.

D* Lite successfully processed all 24 obstacle updates. However, its total node expansions were higher than BFS in this experiment.

### 6. Result Files

- `results/challenging_obstacle_results.csv`
- `results/member1_multi_obstacle_test.csv`
### 6.1 Reproducing the Multi-Obstacle Experiment

The 24-obstacle D* Lite experiment can be reproduced by running:

```bash
python -m src.test_dstar_multi_obstacle
```

The script loads `data/raw/large_42.json`, introduces 24 fixed obstacles sequentially, updates D* Lite after each obstacle, and compares the final route with a fresh BFS search.

The regenerated output is saved to:

`results/member1_multi_obstacle_test_reproduced.csv`

### 6.2 CSV Column Definitions and Units

| Column | Description | Unit |
|---|---|---|
| record_type | Obstacle record or final summary | Text |
| maze | Maze identifier | Text |
| size | Maze dimensions | Cells |
| obstacle_number | Sequential obstacle number | Count |
| obstacle_cell | Obstacle position (row, column) | Grid coordinates |
| expansions_this_update | D* Lite expansions for an update | Nodes |
| initial_path_length | Original path length | Steps |
| final_dstar_path_length | Final D* Lite path length | Steps |
| final_bfs_path_length | Final BFS path length | Steps |
| dstar_total_expansions | Total D* Lite expansions | Nodes |
| dstar_replanning_expansions | D* Lite expansions after initial planning | Nodes |
| bfs_expansions | Fresh BFS search expansions | Nodes |
| success | Whether the algorithm found a valid path | Boolean |

### 6.3 Experimental Assumptions

- The experiment uses the generated 30 x 30 `large_42` maze.
- The same 24 fixed obstacle coordinates are used in every run.
- Obstacles are introduced sequentially, one at a time.
- D* Lite retains its previous search information between updates.
- BFS performs a fresh search after all obstacles have been introduced.
- Movement is restricted to four directions.
- Unknown cells and sensor uncertainty are not modelled in this particular experiment.
- Node expansions are counted as search operations; execution time is not measured in this experiment.

### 6.4 Experimental Outcome

Both algorithms successfully found a final path of 60 steps.

D* Lite recorded 737 total expansions, including 348 replanning expansions. BFS recorded 669 expansions in its fresh final search.

These results demonstrate successful incremental replanning, but do not establish that D* Lite is more efficient than BFS in every scenario.

### 7. Testing and Validation

The existing automated test suite was executed using:

bash
python -m pytest -q


Result: 9 tests passed.

### 8. Conclusion

The Week 6 implementation demonstrates that D* Lite can update its search after successive obstacle discoveries while retaining previously calculated search information.

The comparison with BFS confirmed that both algorithms found equally short paths in the challenging experiment.

The results are preliminary and do not establish that D* Lite always performs better than BFS in terms of execution time or total node expansions.
---

## Week 6 – Reactive A* and D* Lite Comparative Evaluation

### 9. Objective

The objective of this experiment was to evaluate autonomous navigation algorithms in partially observable maze environments.

Reactive A* and D* Lite were tested to study their ability to discover obstacles, replan routes, and navigate from the starting position to the goal.

### 9.1 Reactive A* Implementation

Reactive A* was implemented in `src/solver.py`.

The algorithm:
- Initially has limited knowledge of the maze.
- Treats unknown cells as traversable during planning.
- Discovers obstacles when attempting movement.
- Updates its known map.
- Runs A* again when an obstacle is discovered.

The implementation was integrated into `src/main.py`.

### 9.2 D* Lite Partial-Observation Integration

D* Lite was integrated with the robot simulation using:

- `src/dstar_lite.py`
- `src/robot.py`
- `src/partial_observation.py`

The robot initially knows only its starting position. Unknown cells are assumed to be open for planning.

When an obstacle is discovered, D* Lite updates its existing search information and calculates a new route.

### 9.3 Experimental Setup

Both algorithms were evaluated using the same nine generated mazes:

| Maze Category | Dimensions | Number of Mazes |
|---|---|---:|
| Small | 10 × 10 | 3 |
| Medium | 20 × 20 | 3 |
| Large | 30 × 30 | 3 |
| **Total** | | **9** |

The following performance parameters were recorded:

- Navigation success rate
- Actual path length
- Nodes expanded
- Number of replanning operations
- Execution time
- Peak memory usage
- Number of discovered obstacles

### 9.4 Comparative Results

The average measurements obtained from the nine experiments are shown below.

| Algorithm | Success Rate | Avg. Path Length | Avg. Nodes Expanded | Avg. Runtime (s) | Avg. Memory (KB) | Avg. Replans |
|---|---:|---:|---:|---:|---:|---:|
| BFS | 100% | 38.00 | 356.11 | 0.000614 | 28.40 | 0.00 |
| DFS | 100% | 104.22 | 382.56 | 0.001827 | 34.98 | 0.00 |
| A* | 100% | 38.00 | 223.00 | 0.000591 | 24.60 | 0.00 |
| Reactive A* | 100% | 56.44 | 2921.56 | 0.007978 | 55.11 | 15.11 |
| D* Lite | 100% | 56.44 | 525.00 | 0.028559 | 91.41 | 15.22 |

### 9.5 Performance Analysis

**Node Expansions:**

D* Lite expanded an average of 525 nodes, compared with 2921.56 for Reactive A*. This represents approximately 82% fewer node expansions.

**Execution Time:**

Reactive A* recorded a lower average execution time of approximately 0.007978 seconds, compared with 0.028559 seconds for D* Lite.

**Memory Usage:**

Reactive A* used approximately 55.11 KB of peak memory, whereas D* Lite used approximately 91.41 KB.

**Path Length:**

Both algorithms achieved an average actual path length of 56.44 steps across the nine mazes.

**Navigation Success:**

Both algorithms successfully reached the goal in all nine test mazes, achieving a 100% success rate.

### 9.6 Result Files

The experimental results are stored in:

- `results/maze_results.csv` – BFS, DFS, A*, and Reactive A* results.
- `results/dstar_lite_navigation_results.csv` – D* Lite partial-observation results.
- `results/algorithm_comparison.csv` – Comparative average performance of all five algorithms.

### 9.7 Conclusion

The experiments demonstrate that both Reactive A* and D* Lite can successfully navigate partially observable maze environments.

D* Lite performed substantially fewer node expansions than Reactive A*, indicating an advantage in reducing repeated search operations through incremental replanning.

However, Reactive A* recorded lower execution time and memory consumption in the tested implementation.

The results demonstrate different performance trade-offs between the two navigation approaches. Neither algorithm is universally superior across all performance measurements.

The experiments were conducted on nine generated mazes, and the results should be interpreted within the limits of the tested configurations.
## 10. Week 7 – Statistical Evaluation

### 10.1 Objectives

Week 7 focused on evaluating maze navigation algorithms across multiple maze configurations and unseen random seeds.

The evaluation measured:
- Nodes expanded.
- Peak memory consumption.
- Solution quality (actual path length).
- Navigation success rate.
- Execution time.
- Replanning count.

### 10.2 Experimental Setup

A separate dataset was generated using seeds 100–109.

| Maze Size | Dimensions | Test Mazes |
|---|---|---:|
| Small | 10 × 10 | 10 |
| Medium | 20 × 20 | 10 |
| Large | 30 × 30 | 10 |
| Total | | 30 |

Five algorithms were tested: BFS, DFS, A*, Reactive A*, and D* Lite.

This produced 150 experiments. BFS, DFS and A* used full maze visibility, while Reactive A* and D* Lite used partial observation.

### 10.3 Statistical Results

Values represent mean ± standard deviation across 10 runs.

#### Nodes Expanded

| Maze Size | Reactive A* | D* Lite |
|---|---:|---:|
| Small | 256.2 ± 59.73 | 112.2 ± 13.95 |
| Medium | 1,986.4 ± 763.22 | 456.9 ± 33.91 |
| Large | 5,484.1 ± 1,781.49 | 979.4 ± 61.51 |

#### Peak Memory Usage (KB)

| Maze Size | Reactive A* | D* Lite |
|---|---:|---:|
| Small | 13.64 ± 0.54 | 21.38 ± 3.06 |
| Medium | 50.71 ± 1.97 | 75.18 ± 9.30 |
| Large | 99.32 ± 0.92 | 147.61 ± 10.59 |

#### Solution Quality – Path Length

| Maze Size | Reactive A* | D* Lite |
|---|---:|---:|
| Small | 22.2 ± 5.20 | 22.2 ± 5.20 |
| Medium | 57.0 ± 12.01 | 57.0 ± 12.01 |
| Large | 82.6 ± 18.60 | 82.8 ± 19.14 |

### 10.4 Success Rate

Both Reactive A* and D* Lite achieved 100% success across all three maze sizes.

All 150 experiments across the five algorithms completed successfully, with zero recorded failures.

### 10.5 Error-Bar Charts

The following charts were generated using mean values and standard deviations:

- `results/week7/charts/nodes_expanded.png`
- `results/week7/charts/memory_usage.png`
- `results/week7/charts/path_length.png`

### 10.6 Performance Analysis

D* Lite expanded fewer nodes than Reactive A* across all maze sizes.

Reactive A* consumed less peak memory across all three maze sizes.

Both algorithms achieved nearly identical average path lengths, indicating comparable solution quality.

The results demonstrate different performance trade-offs. D* Lite performed better in terms of recorded node expansions, while Reactive A* used less memory.

Node-expansion counts are implementation-specific and should not be interpreted as identical measures of total computational work.

### 10.7 Result Files

All Week 7 outputs are stored separately in `results/week7/`.

- `experiment_results.csv` – Raw results from 150 experiments.
- `experiment_summary.csv` – Statistical summaries.
- `experiment_failures.csv` – Failed experiment records.
- `charts/` – Generated comparison charts.

The experiment scripts are:

- `run_week7_experiments.py`
- `create_week7_charts.py`

### 10.8 Conclusion

The Week 7 evaluation extended the earlier experiments using 10 additional random seeds and three maze sizes.

D* Lite demonstrated fewer node expansions, while Reactive A* required less peak memory. Both algorithms achieved 100% success and nearly identical average path lengths.

These results provide a statistical comparison of the two partial-observation navigation approaches across different maze configurations.

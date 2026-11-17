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
| Member 1 (Neeraj)| Maze / Data Preparation |
| Member 2 (Riya) | Algorithm Development |
| Member 3 (jasmeet)| Testing / Evaluation |
| Member 4 (pranav)| Documentation / Research | (removed)

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
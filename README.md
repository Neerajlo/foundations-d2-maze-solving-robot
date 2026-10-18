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

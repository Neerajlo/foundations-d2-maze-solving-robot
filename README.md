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

## Week 2 — Initial Findings

1. All tested maze sizes (5 × 5, 10 × 10, 20 × 20, and 30 × 30) were successfully solved by BFS.

2. The path length increased significantly as the maze size increased, from 10 moves in the 5 × 5 maze to 436 moves in the 30 × 30 maze.

3. The number of nodes expanded increased from 15 in the 5 × 5 maze to 743 in the 30 × 30 maze.

4. The actual path through the maze can be much longer than the Manhattan distance between the start and goal because the robot must follow the available maze passages.

5. The generated maze structure has dead ends and branching paths. In the 10 × 10 maze, the number of reachable neighbors per cell ranged from 1 to 3, with an average of 1.98.
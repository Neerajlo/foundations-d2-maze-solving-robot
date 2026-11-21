# Week 10 – Navigation and Replanning Validation

## 1. Project Information

**Project:** Foundations D2 – Maze Solving Robot  
**Team Member:** Jasmeet  
**Role:** Member 2 – Navigation and Replanning Validation  
**Week:** 10

## 2. Objective

The objective of this work was to validate the enhanced Reactive A* algorithm implemented by Member 1.

The testing focused on:

1. Verifying obstacle detection.
2. Checking whether the robot replans when its planned path is blocked.
3. Evaluating the effect of visited-cell penalties on navigation.
4. Comparing original and enhanced Reactive A* on selected obstacle-heavy mazes.
5. Checking whether the robot successfully reaches its goal without getting stuck.

## 3. Testing Environment

The project was implemented and tested using:

- Programming Language: Python
- Development Environment: Visual Studio Code
- Python Environment: Project virtual environment (.venv)
- Dataset: Moving AI benchmark
- Map: `maze512-1-0.map`
- Scenario File: `maze512-1-0.map.scen`

The external map dimensions were 512 × 512.

### Algorithms Tested

**Original Reactive A\***

The original algorithm uses partial observation. It discovers obstacles when attempting to enter blocked cells and replans using A*.

**Enhanced Reactive A\***

The enhanced implementation introduces a configurable visit penalty. Previously visited cells receive additional movement cost during path planning.

Penalty values tested:

- 0.0
- 0.1
- 0.25
- 0.5

## 4. Experimental Methodology

Four Moving AI scenarios were selected:

- Scenario 100
- Scenario 102
- Scenario 104
- Scenario 107

For each scenario:

1. The original Reactive A* algorithm was executed.
2. The enhanced algorithm was executed using four different penalty values.
3. Both algorithms used the same map and start/goal coordinates.
4. Navigation success, distance, replanning, obstacle discovery and revisiting behaviour were recorded.
5. The final position was checked against the goal position.

A total of 20 experiments were performed:

- 4 original algorithm experiments.
- 16 enhanced algorithm experiments.

Results were saved in:

`results/week10_navigation_validation.csv`

## 5. Comparative Navigation Results

### 5.1 Actual Travel Distance

| Scenario | Original | Penalty 0.1 | Penalty 0.25 | Penalty 0.5 |
|---|---:|---:|---:|---:|
| 100 | 757 | 1107 | 1021 | 57 |
| 102 | 47 | 47 | 47 | 47 |
| 104 | 43 | 43 | 43 | 43 |
| 107 | 99 | 213 | 213 | 213 |

All experiments successfully reached their respective goals.

### 5.2 Replanning Behaviour

| Scenario | Original Replans | Penalty 0.1 | Penalty 0.25 | Penalty 0.5 |
|---|---:|---:|---:|---:|
| 100 | 371 | 565 | 564 | 35 |
| 102 | 27 | 27 | 27 | 27 |
| 104 | 23 | 23 | 23 | 23 |
| 107 | 47 | 129 | 129 | 129 |

### 5.3 Revisited Moves

| Scenario | Penalty 0.0 | Penalty 0.1 | Penalty 0.25 | Penalty 0.5 |
|---|---:|---:|---:|---:|
| 100 | 393 | 618 | 529 | 7 |
| 102 | 4 | 4 | 4 | 4 |
| 104 | 0 | 0 | 0 | 0 |
| 107 | 31 | 91 | 91 | 91 |

The original algorithm does not return a revisited-moves metric.

## 6. Scenario-wise Observations

### Scenario 100

Penalty 0.5 produced a substantial improvement.

- Original distance: 757
- Enhanced distance: 57
- Original replans: 371
- Enhanced replans: 35
- Enhanced revisited moves: 7

The enhanced algorithm successfully reached the goal while significantly reducing travel distance and replanning.

### Scenario 102

All four penalty values produced the same travel distance of 47.

The enhanced algorithm successfully reached the goal, and replanning remained unchanged at 27.

### Scenario 104

All penalty values produced the same travel distance of 43.

The enhanced algorithm recorded zero revisited moves and successfully reached the goal.

### Scenario 107

The enhanced algorithm showed a performance deterioration with every non-zero penalty.

- Original distance: 99
- Enhanced distance: 213
- Original replans: 47
- Enhanced replans: 129
- Enhanced revisited moves: 91

This indicates that the visit penalty can negatively affect route selection in certain maze configurations.

## 7. Controlled Obstacle Detection and Replanning Test

A separate controlled maze was created to directly verify obstacle discovery and replanning.

The test used a 5 × 5 maze.

Start position: `(0, 0)`

Goal position: `(0, 4)`

The maze contained blocked cells along the initially preferred route, requiring the robot to discover obstacles and find an alternative route.

### Test Results

| Metric | Original Reactive A* | Enhanced Reactive A* |
|---|---:|---:|
| Success | True | True |
| Actual distance | 8 | 8 |
| Obstacles discovered | 2 | 2 |
| Replans | 2 | 2 |
| Revisited moves | Not measured | 0 |
| Final position | (0, 4) | (0, 4) |

### Observations

1. Both algorithms successfully detected two obstacles.
2. Both algorithms replanned twice.
3. Both algorithms found an alternative route.
4. Both algorithms successfully reached the goal.
5. The enhanced algorithm completed the route without revisiting cells.

This test directly validated obstacle detection and replanning behaviour.

## 8. Key Findings

The experiments produced the following findings:

1. The enhanced Reactive A* successfully reached the goal in all 16 selected benchmark runs.
2. Penalty 0.5 significantly improved navigation in Scenario 100.
3. Scenarios 102 and 104 showed no change in travel distance across the tested penalty values.
4. Scenario 107 demonstrated that non-zero penalties can increase travel distance and replanning.
5. The controlled obstacle test confirmed that both algorithms can detect obstacles and replan successfully.
6. The effectiveness of the visit penalty depends on the maze configuration.

## 9. Limitations

The validation was performed on four selected Moving AI scenarios and one controlled maze.

The results therefore do not establish that a particular penalty value is optimal for all maze configurations.

The experiments demonstrate that visit penalties can improve navigation in some environments but may also introduce additional navigation overhead in others.

Further testing on a larger variety of obstacle configurations would help establish more reliable penalty-selection strategies.

## 10. Deliverables

The following files were produced for Week 10:

### Testing Scripts

- `src/test_week10_navigation.py`
- `src/test_week10_obstacle_replanning.py`

### Experimental Results

- `results/week10_navigation_validation.csv`

### Evidence Screenshots

- `docs/evidence/week10_obstacle_replanning.png`
- `docs/evidence/week10_comparative_results.png`

## 11. Conclusion

The Week 10 navigation and replanning validation was completed successfully.

The enhanced Reactive A* algorithm was tested against the original implementation using selected external benchmark scenarios and a controlled obstacle maze.

All 20 benchmark experiments successfully reached their respective goals.

The controlled test further confirmed that both implementations correctly detected obstacles, replanned their routes and reached the destination.

The visit penalty demonstrated significant improvements in certain scenarios, while other scenarios showed no improvement or deterioration.

Overall, the testing confirms that the enhanced algorithm is functional, but its navigation efficiency depends on the maze configuration and selected penalty value.
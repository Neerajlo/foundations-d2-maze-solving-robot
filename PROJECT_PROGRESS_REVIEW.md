
# PROJECT PROGRESS REVIEW

## 1. Project Overview

### Project Title
D2 – Maze Solving Robot Using Search Algorithms

### Introduction
The objective of this project is to develop a simulated robot that can navigate through a grid-based maze and find a path from a starting position to a goal position.

The project uses Artificial Intelligence search algorithms to explore the maze, avoid obstacles, find paths, and replan routes when new obstacles are discovered.

### Project Objectives
- Implement search algorithms for maze navigation.
- Use BFS as the baseline pathfinding algorithm.
- Compare BFS, DFS and A* in a fully visible maze.
- Implement Reactive A* and D* Lite for partial-observation navigation.
- Evaluate algorithms using path length, nodes expanded, execution time and memory usage.
- Test the algorithms on different maze sizes and random seeds.

### Maze Environment
The maze is represented as a two-dimensional grid.

- `0` represents an open cell.
- `1` represents an obstacle or blocked cell.
- The robot starts at the top-left position.
- The goal is at the bottom-right position.
- The robot can move in four directions: up, down, left and right.

### Observation Models
**Fully Visible Maze:** The complete maze is available to the search algorithm before navigation begins.

**Partial Observation:** The robot initially knows only limited information about the maze. It discovers obstacles while moving and updates its route when required.

## 2. Search Algorithms and Implementation

This project uses different search algorithms to find paths through the maze and compare their performance.

### 2.1 Breadth-First Search (BFS)

**Purpose:** BFS is used as the baseline algorithm for maze pathfinding.

**How it works:**
1. It starts from the starting cell.
2. It explores all nearby cells first.
3. It uses a queue (FIFO – First In, First Out).
4. It marks visited cells to avoid exploring them repeatedly.
5. It continues until the goal is reached.

**Why we used BFS:**
- It finds the shortest path in an unweighted maze.
- It provides a reliable baseline for comparing other algorithms.

**Implementation:** `src/bfs.py`

### 2.2 Depth-First Search (DFS)

**Purpose:** DFS is used to compare another search strategy with BFS.

**How it works:**
1. It starts from the starting cell.
2. It explores one direction as deeply as possible.
3. It uses a stack (LIFO – Last In, First Out).
4. When it cannot continue, it backtracks.
5. It continues until it finds the goal or exhausts the available paths.

**Why we used DFS:**
- It provides a comparison with BFS.
- It helps demonstrate how different search strategies affect path length and exploration.

**Limitation:** DFS does not guarantee the shortest path.

**Implementation:** `src/solver.py`

### 2.3 A* Search

**Purpose:** A* is used to find an efficient path by combining the distance already travelled with an estimate of the remaining distance.

**How it works:**
1. It calculates the cost of reaching a cell.
2. It estimates the distance from that cell to the goal.
3. It adds both values to calculate the priority.

The evaluation function is:

f(n) = g(n) + h(n)

Where:
- g(n) = actual cost from the starting cell.
- h(n) = estimated cost from the current cell to the goal.
- f(n) = total estimated cost.

**Heuristic used:** Manhattan Distance.

**Why we used A*:** It helps reduce unnecessary exploration compared with BFS while finding a shortest path when the heuristic is suitable.

**Implementation:** `src/solver.py`

### 2.4 D* Lite

**Purpose:** D* Lite is used for navigation when the robot discovers new obstacles while moving through the maze.

**How it works:**
1. It initially plans a route from the robot's starting position to the goal.
2. It uses two important values, g and rhs, to maintain information about path costs.
3. When a new obstacle is discovered, it updates the affected cells.
4. It reuses previously calculated search information.
5. It calculates an updated route instead of restarting the entire search from the beginning.

**Why we used D* Lite:**
- It supports dynamic environments.
- It can update routes when obstacles are discovered.
- It reuses previous search information during replanning.

**Implementation:** `src/dstar_lite.py`

### 2.5 Reactive A*

Reactive A* is another algorithm used in the project's partial-observation navigation experiments.

It initially plans using the information currently available. When the robot discovers an obstacle, it updates its knowledge and calculates another route.

**Implementation:** `src/solver.py`

**Note:** The main focus of Member 1's search-algorithm work is BFS, DFS and D* Lite.

## 3. Experimental Methodology

The project was evaluated using multiple maze sizes, random seeds and search algorithms.

### 3.1 Experimental Setup

- Maze sizes: 10×10, 20×20 and 30×30.
- Random seeds: 42 to 51.
- Total seeds: 10.
- Algorithms tested: BFS, DFS, A*, Reactive A* and D* Lite.
- Total experimental runs: 150.

### Additional Statistical Evaluation

A separate statistical evaluation was conducted using a new set of 10 random seeds (100–109).

- Maze sizes: 10×10, 20×20 and 30×30.
- Random seeds: 100 to 109.
- Algorithms tested: BFS, DFS, A*, Reactive A* and D* Lite.
- Total experimental runs: 150.
- Successful runs: 150.
- Failed runs: 0.

The results are stored separately in:
- `results/week7/experiment_results.csv`
- `results/week7/experiment_summary.csv`
- `results/week7/experiment_failures.csv`

This dataset is separate from the earlier evaluation using seeds 42–51. The two datasets have not been combined.

The experiments were divided into two scenarios:

**Scenario 1 – Fully Visible Maze**
- BFS
- DFS
- A*

**Scenario 2 – Partial Observation**
- Reactive A*
- D* Lite

### 3.2 Performance Metrics

The following metrics were used:

1. **Path Length:** Number of steps required to reach the goal.
2. **Nodes Expanded:** Number of nodes explored by the algorithm.
3. **Execution Time:** Time taken to perform the search or navigation.
4. **Peak Memory:** Maximum memory used during execution.
5. **Replan Count:** Number of times the route was recalculated after discovering obstacles.
6. **Success Rate:** Percentage of runs in which the robot successfully reached the goal.

## 4. Experimental Results

### 4.1 Overall Results

- Total experimental runs: 150.
- Successful runs: 150.
- Failed runs: 0.
- Overall success rate: 100%.

Each combination of maze size and algorithm was tested using 10 random seeds.

### 4.2 Fully Visible Maze Results

Average results across 10 seeds:

| Maze Size | Algorithm | Path Length | Nodes Expanded |
|---|---|---:|---:|
| 10×10 | BFS | 18 | 77.5 |
| 10×10 | DFS | 32.8 | 49.2 |
| 10×10 | A* | 18 | 61.4 |
| 20×20 | BFS | 38 | 306.8 |
| 20×20 | DFS | 101.8 | 312.1 |
| 20×20 | A* | 38 | 210.6 |
| 30×30 | BFS | 58 | 683.6 |
| 30×30 | DFS | 190.2 | 858.4 |
| 30×30 | A* | 58 | 414.7 |

### 4.3 Partial Observation Results

Average nodes expanded across 10 seeds:

| Maze Size | Reactive A* | D* Lite |
|---|---:|---:|
| 10×10 | 289.7 | 114.4 |
| 20×20 | 1800.5 | 437.2 |
| 30×30 | 6333.5 | 1003.5 |

Average path lengths:

| Maze Size | Reactive A* | D* Lite |
|---|---:|---:|
| 10×10 | 23 | 23 |
| 20×20 | 51 | 51 |
| 30×30 | 85.6 | 85.6 |

### 4.4 Performance Analysis

**BFS vs A*:**
- Both algorithms produced the same average path lengths in the tested mazes.
- A* expanded fewer nodes than BFS across all three maze sizes.
- This demonstrates the benefit of using the Manhattan Distance heuristic to guide the search.

**DFS:**
- DFS successfully found paths.
- However, its average path lengths were longer than BFS and A*.
- DFS does not guarantee the shortest path.

**Reactive A* vs D* Lite:**
- D* Lite expanded fewer nodes than Reactive A* in all three maze sizes.
- Both algorithms achieved the same average path length for each maze size.
- However, D* Lite had higher execution time and peak memory usage in these experiments.
- D* Lite reuses previous search information when updating its route.

### 4.5 Experiment Output Files

The experimental results are stored in:

- `results/experiment_results.csv` – raw results of individual runs.
- `results/experiment_summary.csv` – average, standard deviation, minimum and maximum values.
- `results/experiment_failures.csv` – records failed experiments.
- `experiments.csv` – project experiment log.

The experiments can be reproduced using:

```powershell
python run_experiments.py
```

### 4.6 Important Experimental Limitation

The project currently uses a simulated grid-based maze with four-direction movement. It has not yet been validated using a physical robot.

The partial-observation algorithms were evaluated in simulation. Their obstacle-discovery sequences are not necessarily identical, so the comparison should be interpreted as an experimental performance comparison rather than a perfectly controlled identical-obstacle test.

## 5. Practical Demonstrations

Two demonstration programs were prepared for the project progress review.

### 5.1 Demonstration 1 – Fully Visible Maze

**File:** `demo.py`

This program demonstrates BFS, DFS and A* on a 10×10 maze.

**Working:**
1. A maze is generated using random seed 42.
2. BFS, DFS and A* are executed on the same maze.
3. The algorithms explore the maze and search for the goal.
4. Their explored cells and final paths are displayed visually.
5. Path length and nodes expanded are printed in the terminal.

**Observed Output:**

| Algorithm | Success | Path Length | Nodes Expanded |
|---|---|---:|---:|
| BFS | Yes | 18 | 76 |
| DFS | Yes | 24 | 38 |
| A* | Yes | 18 | 57 |

**Purpose:** To visually demonstrate how different search algorithms explore a maze and find paths.

**Generated chart:** `results/charts/demo.png`

### 5.2 Demonstration 2 – Reactive A* vs D* Lite

**File:** `demo2.py`

This program compares Reactive A* and D* Lite using the existing 9-maze experimental results stored in `results/algorithm_comparison.csv`.

**Comparison Results:**

| Metric | Reactive A* | D* Lite |
|---|---:|---:|
| Success Rate | 100% | 100% |
| Average Path Length | 56.44 | 56.44 |
| Average Nodes Expanded | 2921.56 | 525 |
| Average Runtime | 0.00798 s | 0.02856 s |
| Average Memory | 55.11 KB | 91.41 KB |
| Average Replans | 15.11 | 15.22 |

**Purpose:** To demonstrate the differences in search effort, execution time, memory usage and path length between the two partial-observation approaches.

**Generated chart:** `results/charts/demo2.png`

**Important:** These figures are from the earlier 9-maze experiment. They are separate from the newer 150-run evaluation documented in Section 4.

## 6. Additional D* Lite Multi-Obstacle Experiment

A separate experiment was conducted to examine how D* Lite responds when multiple obstacles are introduced into a maze.

### Experiment Setup

- Maze size: 30×30.
- Maze used: `large_42`.
- Number of newly introduced obstacles: 24.
- Algorithms compared: D* Lite and BFS.
- D* Lite updated its existing search information after obstacle changes.
- BFS was executed again on the final modified maze.

### Results

| Metric | D* Lite | BFS |
|---|---:|---:|
| Final Path Length | 60 | 60 |
| Total Nodes Expanded | 737 | 669 |
| Additional D* Lite Replanning Expansions | 348 | Not applicable |

- Both algorithms successfully found a path.
- Both produced the same final path length of 60.
- D* Lite reused its previous search information during obstacle updates.
- In this particular experiment, D* Lite's total expansions were higher than the fresh BFS search.

### Output File

`results/member1_multi_obstacle_test_reproduced.csv`

**Implementation:** `src/test_dstar_multi_obstacle.py`

**Conclusion:** This experiment demonstrates D* Lite's incremental replanning capability. It does not establish that D* Lite always expands fewer nodes than BFS.

## 7. Member 2 – Jasmeet's Contributions (Algorithm Development)

Jasmeet primarily contributed to the development and experimental evaluation of Reactive A* for autonomous maze navigation under partial observation.

### 7.1 Reactive A* Implementation

- Implemented Reactive A* navigation in `src/solver.py`.
- Developed a partial-observation approach in which the robot initially knows only its starting cell.
- Implemented an internal map to distinguish unknown, free and blocked cells.
- Used A* path planning to calculate an initial route towards the goal.
- Added obstacle detection when the robot attempts to enter a blocked cell.
- Implemented route replanning whenever a previously unknown obstacle is discovered.
- Recorded navigation information, including actual distance travelled, nodes expanded, replanning count and discovered obstacles.

### 7.2 Experimental Evaluation

- Contributed to the experimental evaluation of the maze-solving algorithms.
- Evaluated Reactive A* across small, medium and large maze configurations.
- Worked with a ten-seed experimental evaluation to study performance across different maze configurations.
- Analysed path length, nodes expanded, execution time, peak memory and success rate.
- Examined average performance and standard deviation to understand variations across experiments.
- Helped prepare result tables and error-bar visualizations for performance analysis.

### 7.3 Comparative Analysis

Compared Reactive A* with the team's existing D* Lite implementation under partial-observation conditions.

The evaluation examined:
- Average path length.
- Nodes expanded.
- Execution time.
- Peak memory usage.
- Replanning behaviour.
- Overall navigation success.

The results showed that D* Lite expanded fewer nodes, while Reactive A* required less execution time and peak memory in the measured experiments.

### 7.4 Obstacle Detection and Replanning Tests

Conducted controlled tests to verify Reactive A* behaviour when encountering obstacles.

One controlled test demonstrated:
- Successful navigation to the goal.
- One obstacle discovered.
- One replanning operation.
- Actual distance travelled: 4 steps.
- Nodes expanded: 16.

These tests helped verify obstacle detection and route recovery independently of the larger statistical experiments.

### 7.5 Documentation and Review Preparation

- Updated project documentation relating to Reactive A*.
- Contributed experimental findings and performance comparisons.
- Reviewed generated result charts and tables.
- Prepared material explaining the algorithm's working, experimental findings and current limitations for the project progress review.

### 7.6 Current Challenges and Improvement Areas

- Reactive A* performs a fresh A* search after discovering an obstacle, which can increase the number of nodes expanded.
- Its search efficiency needs improvement for larger mazes.
- Further testing is required with more challenging obstacle configurations.
- The current implementation is evaluated in a simulated grid environment and has not yet been tested on a physical robot.

**Overall Contribution:** Developed and evaluated the Reactive A* partial-observation navigation approach, investigated obstacle discovery and replanning, and contributed to the experimental comparison and documentation of navigation algorithms.

## 8. Current Limitations and Areas for Improvement

The project is currently working in a simulated maze environment. However, some limitations remain.

### 8.1 Current Limitations

1. **Simulation Only:** The project has not yet been tested on a physical robot.
2. **Four-Direction Movement:** The robot can move only up, down, left and right.
3. **Limited Environment:** The maze is grid-based and does not represent every real-world navigation condition.
4. **Execution Time:** D* Lite uses more execution time and memory than Reactive A* in the current 150-run evaluation.
5. **Experimental Conditions:** The obstacle-discovery sequences may differ between the partial-observation algorithms.

### 8.2 Future Improvements

- Test the algorithms in more complex maze environments.
- Improve the efficiency of path planning and replanning.
- Perform additional robustness tests with different obstacle configurations.
- Investigate the possibility of testing the system with a physical robot.

## 9. project progress review and Teacher Feedback

### 9.1 Demonstration Preparation

The following demonstration programs have been prepared:

- `demo.py` – BFS, DFS and A* comparison.
- `demo2.py` – Reactive A* and D* Lite comparison.

The corresponding charts have been generated and saved in `results/charts/`.

### 9.2 Teacher Feedback

Status: Earlier feedback received; demonstration review pending.

Earlier Teacher Feedback:

- Instruction: Ensure that the project is uploaded and updated on the GitHub "main" branch.
- Action: Verify repository synchronization and maintain updated project documentation.
- Verification: Git status previously confirmed that the local "main" branch was up to date with "origin/main". Current local documentation changes still require review and synchronization.

Demonstration Review Status:

- Demonstration programs prepared: Yes.
- Demonstration presented to teacher: No.
- Teacher attended demonstration: No.
- Demonstration-specific feedback: Awaiting presentation.

Pending Actions:

1. Present the Fully Visible Maze demonstration.
2. Present the Reactive A* vs D* Lite demonstration.
3. Record actual teacher comments and suggestions.
4. Update the project plan according to the feedback received.

Feedback received from the teacher will be recorded here after the demonstration.

| No. | Teacher Feedback | Action Required | Status |
|---|---|---|---|
| 1 | To be updated after review | To be decided | Pending |
| 2 | To be updated after review | To be decided | Pending |
| 3 | To be updated after review | To be decided | Pending |

## 10. Project Plan for Weeks 9–12

The following plan is based on the project guidebook and will be updated according to teacher feedback.

### Week 9 – Improve and Test

**Focus:**
- Improve the existing project based on review feedback.
- Test the system with additional scenarios or external data, where applicable.
- Review the performance of the implemented algorithms.

**Member 1 – Riya:**
- Review BFS, DFS and D* Lite implementation.
- Identify possible improvements in search and replanning.
- Validate the results after any changes.

### Week 10 – Required Extension

**Focus:**
- Implement the required project extension.
- Integrate the extension with the existing system.
- Test whether the new functionality works correctly.

**Member 1 – Riya:**
- Contribute to the search-algorithm side of the extension.
- Check compatibility with existing BFS and D* Lite functionality.

### Week 11 – Robustness Testing

**Focus:**
- Test the project under different conditions.
- Identify failures and weaknesses.
- Fix problems and verify the results.

**Member 1 – Riya:**
- Test BFS and D* Lite using different maze configurations.
- Check how D* Lite responds to newly introduced obstacles.
- Document performance and any issues found.

### Week 12 – Final Project Freeze

**Focus:**
- Finalize the implementation.
- Verify the results and documentation.
- Organize the repository.
- Prepare the final project demonstration.

**Member 1 – Riya:**
- Verify the search-algorithm implementation.
- Check experimental results and documentation.
- Prepare to explain the BFS, DFS and D* Lite contributions.

## 11. Project Review Completion Status

| Task | Status |
|---|---|
| Prepare BFS, DFS and A* demonstration | Completed |
| Prepare Reactive A* and D* Lite demonstration | Completed |
| Generate demonstration charts | Completed |
| Document experimental results | Completed |
| Document limitations | Completed |
| Deliver project demonstration | Pending |
| Record teacher feedback | Pending |
| Finalize Weeks 9–12 plan using feedback | Pending |

## 12. Conclusion

During this project, different search algorithms were implemented and evaluated for maze navigation.

BFS was used as the baseline, while DFS and A* were used for comparison in fully visible mazes. Reactive A* and D* Lite were evaluated for partial-observation navigation.

The project completed 150 experimental runs with a 100% success rate. The results demonstrate differences in path length, nodes expanded, execution time and memory usage.

The next phase will focus on improvements, additional testing, robustness and final project preparation.




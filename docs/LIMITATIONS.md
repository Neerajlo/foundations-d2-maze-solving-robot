# Week 11 — Reactive A* Stress Testing and Limitations

## 1. Objective

The objective of Week 11 was to test the limitations of the Reactive A* algorithm with visit penalties. The experiments examined normal navigation, obstacle discovery, unreachable goals, invalid inputs, different visit penalties, runtime, and memory usage.

## 2. Testing Approach

The following tests were performed:

- Normal navigation in a small maze.
- Obstacle discovery and replanning.
- Navigation when the goal is unreachable.
- Negative visit-penalty input.
- Empty maze input.
- Irregular maze input with unequal row lengths.
- Navigation in an obstacle-heavy maze.
- Comparison of different visit-penalty values.
- Runtime and memory measurements.
- Performance testing on larger open mazes.

Reactive A* is a search algorithm and does not use a training dataset. Therefore, the training-data reduction question does not directly apply to this module. Evaluation was performed using manually constructed test mazes instead.

## 3. Experimental Results

| Test | Result | Observation |
|---|---|---|
| Simple 3x3 maze | Success | Reached the goal in 4 moves |
| Obstacle discovery | Success | Discovered one obstacle and replanned once |
| Unreachable goal | Failure reported correctly | Stopped after 3 replans |
| Negative penalty (-1) | Success | Accepted negative input without validation |
| Empty maze | Error | Raised IndexError |
| Irregular maze | Input accepted | Unequal row lengths were not validated |
| Obstacle-heavy 5x5 maze | Success | Discovered two obstacles and replanned twice |
| Penalty comparison | Success | Penalties 0, 0.5 and 1 produced identical results |

## 4. Runtime and Memory Analysis

Runtime and peak traced memory were measured externally using Python's time and tracemalloc modules.

| Maze Size | Success | Runtime (seconds) | Peak Memory (KB) | Nodes Expanded | Distance (moves) |
|---|---|---:|---:|---:|---:|
| 5x5 obstacle-heavy | Yes | 0.001092 | 5.43 | 62 | 8 |
| 50x50 open | Yes | 0.012251 | 327.55 | 2500 | 98 |
| 100x100 open | Yes | 0.106559 | 1300.55 | 10000 | 198 |

The larger open mazes required more nodes to be expanded, more execution time, and more memory.

These measurements were collected on one computer and may vary with hardware and system load. The memory figures represent traced Python allocations, not total process memory.

The maze layouts were not identical across all three sizes, so this comparison is illustrative rather than a controlled scaling experiment.

## 5. Identified Limitations

### 5.1 No validation for negative visit penalties

The function accepted a negative visit penalty without raising an error.

A negative penalty is unsuitable for the intended behaviour because it can reward revisiting previously visited cells rather than discourage revisits.

### 5.2 Empty maze input is not handled safely

Passing an empty maze caused an IndexError because the Maze constructor attempted to access the first row.

The constructor should validate that the maze contains at least one row.

### 5.3 Irregular maze dimensions are not validated

The Maze constructor accepted rows with different lengths.

The algorithm assumes a consistent grid structure, so irregular input may cause unexpected behaviour or indexing errors.

### 5.4 Unreachable goals require additional exploration

When the goal was surrounded by obstacles, the algorithm correctly reported failure. However, it expanded 26 nodes, travelled 6 moves, and replanned 3 times before stopping.

This shows that unsuccessful searches can still require computational work and physical movement.

### 5.5 Replanning increases computational work

In the obstacle-heavy test, the robot discovered two obstacles and replanned twice.

Obstacle discovery is necessary for navigation in partially observed environments, but repeated replanning increases search work.

### 5.6 Visit penalties do not always improve navigation

In the tested 5x5 obstacle-heavy maze, penalty values of 0, 0.5, and 1 all produced the same distance, nodes expanded, and replanning count.

This shows that increasing the visit penalty does not guarantee better results in every environment.

### 5.7 Larger mazes require more resources

The 100x100 open maze required 10,000 expanded nodes and approximately 0.106559 seconds in the measured run.

As the search space grows, the algorithm requires more computational resources.

### 5.8 Limited testing of noisy and complex environments

The tests included invalid penalty values, empty input, irregular maze dimensions, and obstacle-heavy layouts. However, they did not cover every possible malformed input or randomly generated noisy environment.

Further testing is required before making broad claims about robustness.

## 6. Practical Implications

Reactive A* is effective in the tested environments and can discover obstacles, replan, and reach a destination.

However, practical deployment requires additional safeguards:

- Validate maze dimensions and input values.
- Reject negative or non-finite visit penalties.
- Test more complex and randomly generated environments.
- Evaluate performance across more maze sizes and obstacle densities.
- Monitor replanning frequency and computational cost.

## 7. Conclusion

The Week 11 experiments show that Reactive A* can successfully navigate normal and obstacle-heavy test mazes and can correctly report an unreachable goal.

The tests also revealed weaknesses in input validation, handling of malformed mazes, and the computational cost of larger search spaces.

These limitations provide useful directions for future improvements and form the discussion points for the project report.

## 8. Reproduction

Run the Week 10 experiment using:

`python -m src.reactive_astar_experiment`

Week 11 stress-test results are stored in:

`results/stress_test_results.csv`

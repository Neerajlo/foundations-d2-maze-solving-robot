# WEEK 11 — ROBUSTNESS TESTING AND FAILURE ANALYSIS

## 1. Objective

The objective of Week 11 was to evaluate the robustness of the maze-solving algorithms by deliberately testing difficult conditions, malformed inputs, noisy environments, and performance limitations.

The testing focused on:

- Reducing the benchmark evaluation dataset.
- Introducing random obstacles.
- Testing malformed maze inputs.
- Identifying algorithm failure conditions.
- Measuring runtime and memory consumption.
- Comparing Original Reactive A* with Enhanced Reactive A*.

## 2. Reduced Benchmark Evaluation

Since the project uses pathfinding algorithms rather than a machine-learning model, the instruction concerning reduced training data was interpreted as reducing the benchmark scenario set.

The eight Moving AI benchmark scenarios (100–107) were divided into two groups.

| Group | Scenarios |
|---|---|
| Half A | 100, 101, 102, 103 |
| Half B | 104, 105, 106, 107 |

Average results across four visit-penalty settings:

| Metric | Half A | Half B |
|---|---:|---:|
| Average distance | 381.75 | 400.00 |
| Average nodes expanded | 97,808.75 | 106,852.00 |
| Average replans | 195.81 | 189.06 |
| Average revisited moves | 191.06 | 193.12 |

**Observation:** Both subsets showed broadly similar average behaviour, although Half B required approximately 9.2% more node expansions. Scenario-specific differences indicate that averages alone do not fully represent algorithm performance.

## 3. Malformed Input and Edge-Case Testing

Several malformed maze configurations were tested to identify weaknesses in input validation.

| Test case | Observed result | Finding |
|---|---|---|
| Empty grid `[]` | Constructor raises IndexError | Empty grids are not validated |
| Empty row `[[]]` | Algorithms raise IndexError | Missing cells cause indexing failures |
| Unequal row lengths | IndexError during cell validation | Irregular grids are not handled safely |
| Invalid value `2` | Treated as blocked | Invalid values are silently accepted |
| Negative value `-1` | Treated as blocked | Invalid values are silently accepted |
| Floating-point value `0.5` | Treated as blocked | Invalid values are silently accepted |
| Boolean values | False treated as free; True treated as blocked | Python Boolean-integer equality affects validation |
| Start outside grid | Both algorithms unexpectedly succeed in the tested case | Start-position validation is missing |
| Goal outside grid | Both algorithms safely return failure | Invalid goal is not explicitly diagnosed |
| Unreachable goal | Both algorithms terminate and report failure | Correct failure handling |
| Start equals goal | Both algorithms report success with distance zero | Correct edge-case handling |

### Important findings

The `Maze` constructor does not validate grid dimensions or cell values.

The `is_valid()` method also assumes that every row has the same number of columns.

An out-of-bounds starting position was accepted by both algorithms in the tested configuration, demonstrating a weakness in input validation.

No modifications were made to the original algorithms during this testing phase.

### Additional irregular-grid validation

An additional automated test confirmed that the Maze constructor
accepts grids with unequal row lengths.

For the grid:

    [[0, 0],
     [0]]

Accessing the missing cell at position (1,1) raises:

    IndexError: list index out of range

Both algorithms can still succeed when their navigation route avoids
the missing cell. Therefore, the failure is conditional on accessing
the missing position.

## 4. Random Obstacle Stress Testing

Random obstacles were introduced into a 20×20 maze using a fixed random seed of 42.

The starting position `(0,0)` and goal position `(19,19)` were kept free.

### Results

| Obstacle density | Obstacles | Original Reactive A* | Enhanced Reactive A* |
|---|---:|---|---|
| 0% | 0 | Success | Success |
| 10% | 39 | Success | Success |
| 25% | 103 | Success | Success |
| 35% | 150 | Failure | Failure |
| 40% | 163 | Failure | Failure |

### 10% obstacle density

| Metric | Original | Enhanced |
|---|---:|---:|
| Success | True | True |
| Distance | 38 | 38 |
| Nodes expanded | 1,052 | 1,052 |

Both algorithms performed identically.

### 25% obstacle density

| Metric | Original | Enhanced |
|---|---:|---:|
| Success | True | True |
| Distance | 52 | 52 |
| Nodes expanded | 4,428 | 4,325 |

Enhanced Reactive A* expanded 103 fewer nodes, approximately 2.33% fewer than the original algorithm.

### 35% obstacle density

| Metric | Original | Enhanced |
|---|---:|---:|
| Success | False | False |
| Distance | 70 | 67 |
| Nodes expanded | 5,760 | 5,950 |

A BFS connectivity check confirmed that the goal was unreachable. Only 60 cells were reachable from the starting position.

### 40% obstacle density

| Metric | Original | Enhanced |
|---|---:|---:|
| Success | False | False |
| Distance | 78 | 77 |
| Nodes expanded | 5,926 | 6,431 |

A BFS connectivity check confirmed that the goal was unreachable. Only 58 cells were reachable from the starting position.

### Stress-test conclusion

Both algorithms successfully navigated the tested 10% and 25% obstacle configurations.

At 35% and 40%, the generated mazes disconnected the goal from the starting position. Therefore, the failures were caused by unreachable configurations rather than demonstrated algorithm defects.

## 5. Narrow-Corridor Stress Test

A 7×7 maze containing a narrow winding corridor was created to test navigation with limited alternative routes.

### Results

| Metric | Original Reactive A* | Enhanced Reactive A* |
|---|---:|---:|
| Success | True | True |
| Actual distance | 18 | 18 |
| Nodes expanded | 249 | 248 |
| Replans | 10 | 10 |
| Revisited moves | Not reported | 0 |

Both algorithms successfully reached the goal.

Enhanced Reactive A* expanded one fewer node, but the difference was negligible.

The visit penalty did not produce a meaningful performance improvement in this particular configuration.

## 6. Runtime and Memory Analysis

The existing Enhanced Reactive A* benchmark results were analysed using the recorded runtime and peak-memory measurements.

The dataset contained 32 experimental runs covering eight scenarios and four visit-penalty settings.

### Runtime statistics

| Metric | Runtime |
|---|---:|
| Mean | 0.725476 seconds |
| Median | 0.035914 seconds |
| Minimum | 0.011087 seconds |
| Maximum | 3.024271 seconds |

### Memory statistics

| Metric | Peak memory |
|---|---:|
| Mean | 2,281.60 KB |
| Median | 2,143.44 KB |
| Minimum | 2,116.94 KB |
| Maximum | 2,897.45 KB |

### Performance observations

- Scenario 106 produced the highest runtime, reaching approximately 3.02 seconds.
- Scenario 106 also had very high node expansions.
- Scenario 101 consistently showed relatively high runtime and memory consumption.
- Runtime varied considerably depending on the scenario and search workload.

The measurements indicate that difficult navigation scenarios can significantly increase computational effort.

## 7. Identified Weaknesses

The experiments identified the following weaknesses:

1. Empty grids are not validated before accessing the first row.
2. Unequal row lengths can cause indexing errors.
3. Invalid cell values are accepted without explicit validation.
4. Starting positions outside the maze are not properly rejected.
5. Dense random obstacles can create disconnected navigation environments.
6. Enhanced Reactive A* does not consistently reduce computational effort.
7. Runtime increases considerably on difficult benchmark scenarios.

## 8. Limitations

- Random-obstacle experiments used one fixed random seed.
- The 35% and 40% configurations produced unreachable goals.
- Runtime and memory statistics were obtained from the existing benchmark dataset, not exclusively from the newly generated random-obstacle tests.
- The reduced benchmark comparison used averages across four penalty settings.
- The narrow-corridor test covered one configuration.
- No original algorithm implementation was modified during robustness testing.

## 9. Final Conclusion

Week 11 focused on deliberately testing the limitations of Original Reactive A* and Enhanced Reactive A*.

Both algorithms handled several challenging situations successfully, including clean mazes, moderate random obstacles, unreachable goals, start-equals-goal cases, and narrow corridors.

However, the experiments exposed weaknesses in maze input validation, particularly concerning empty grids, irregular row lengths, invalid starting positions, and malformed cell values.

The stress tests also demonstrated that Enhanced Reactive A* does not always reduce node expansions or computational effort compared with the original algorithm.

Overall, the testing provided a clearer understanding of algorithm robustness, failure conditions, and performance limitations.

**Week 11 Outcome:** Robustness testing and failure analysis completed. Input-validation weaknesses and performance limitations identified for future improvement.
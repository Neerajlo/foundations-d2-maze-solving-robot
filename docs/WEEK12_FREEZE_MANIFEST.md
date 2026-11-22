# Week 12 — Experimental Freeze Manifest

## 1. Purpose

This document records the final experimental configuration, results, verification procedures and reproduction instructions for the Foundations D2 Maze Solving Robot project.

Week 12 is the experimental freeze stage.

The objective is to preserve the completed experimental results and ensure that another person can independently clone the repository and reproduce the experiments.

No new algorithms or features are introduced during this stage.

## 2. Frozen Repository Baseline

| Item | Value |
|---|---|
| Repository | https://github.com/Neerajlo/foundations-d2-maze-solving-robot |
| Baseline commit | `84575433d90b8d357c2634e04fb0c3964f7eb4bd` |
| Commit message | Complete experiments, charts and documentation |
| Programming language | Python |
| Tested Python version | 3.14.7 |
| Operating environment | Windows |
| Dependency file | requirements.txt |

The baseline commit identifies the repository state before this freeze manifest was added.

## 3. Experimental Configuration

The final experimental evaluation uses the following configuration:

| Parameter | Configuration |
|---|---|
| Random seeds | 42–51 |
| Number of seeds | 10 |
| Small maze | 10 × 10 |
| Medium maze | 20 × 20 |
| Large maze | 30 × 30 |
| Obstacle probability | 25% |
| Guaranteed path | Start to goal |
| Total experiments | 150 |

The experiment runner generates mazes using fixed random seeds.

The maze generator preserves a guaranteed path from the starting position to the goal position.

### Algorithms evaluated

1. Breadth-First Search (BFS)
2. Depth-First Search (DFS)
3. A* Search
4. Reactive A*
5. D* Lite

### Observation scenarios

- Fully visible: BFS, DFS and A*.
- Partial observation: Reactive A* and D* Lite.

The evaluation consists of:

10 seeds × 3 maze sizes × 5 algorithms = 150 experiments.

## 4. Experimental Results

The primary experimental outputs are:

| File | Description |
|---|---|
| `results/experiment_results.csv` | Raw experimental records |
| `results/experiment_summary.csv` | Aggregated experimental metrics |
| `results/experiment_failures.csv` | Failed experiment records |

The raw results contain 150 experimental records.

The recorded metrics include:

- Success status
- Path length
- Nodes expanded
- Runtime
- Peak memory usage
- Replanning count
- Obstacles discovered

The summary file groups results by observation scenario, maze size and algorithm.

Summary statistics include success rate, mean, standard deviation, minimum and maximum values.

## 5. Final Graphs

The final Week 12 graphs are stored in:

`results/week12_graphs/`

The four generated figures are:

1. `nodes_expanded.png`
2. `path_length.png`
3. `runtime_seconds.png`
4. `peak_memory_kb.png`

The figures display mean values and standard-deviation error bars.

These figures are intended for the final research paper and experimental presentation.

## 6. Result Verification

The verification script is:

`verify_week12.py`

It compares the raw experimental records against the aggregated summary.

It checks:

- Path length
- Nodes expanded
- Runtime
- Peak memory usage
- Number of runs in each group
- Mean-value consistency

The verification tolerance for mean values is 0.000001.

### Previously recorded verification result

| Verification item | Result |
|---|---:|
| Summary rows checked | 60 |
| Matching rows | 60 |
| Mismatches | 0 |
| Status | SUCCESS |

The recorded output was:

`SUCCESS: Summary matches raw experimental data.`

This verification checks run counts and mean values. It does not independently verify every summary statistic.

## 7. Dependencies

Install the dependencies using:

`python -m pip install -r requirements.txt`

Required packages:

| Package | Purpose |
|---|---|
| matplotlib | Graph generation |
| pandas | Experimental data processing |
| pytest | Automated testing |
| python-docx | Word document generation |

Python standard-library modules do not require separate installation.

## 8. Reproduction Instructions

### Step 1 — Clone the repository

`git clone https://github.com/Neerajlo/foundations-d2-maze-solving-robot.git`

### Step 2 — Enter the repository

`cd foundations-d2-maze-solving-robot`

### Step 3 — Check Python

`python --version`

The tested environment used Python 3.14.7.

### Step 4 — Install dependencies

`python -m pip install -r requirements.txt`

### Step 5 — Run the final experimental evaluation

`python run_experiments.py`

IMPORTANT: This command overwrites the existing raw results, summary and failure CSV files. Preserve a backup of the frozen results before running it.

### Step 6 — Generate the graphs

`python create_charts.py`

### Step 7 — Verify the summary

`python verify_week12.py`

### Step 8 — Run automated tests

`python -m pytest src/ -v`

## 9. Important Reproducibility Notes

- Execute commands from the repository root.
- Use the recorded random seeds when reproducing the experiments.
- Keep the dependency list unchanged when testing the frozen environment.
- Preserve the original CSV files before rerunning experiments.
- Runtime and memory measurements may vary across hardware and operating systems.
- Graph appearance and numerical timing measurements may differ slightly between environments.
- The experiment runner should not be executed casually because it overwrites existing result files.

## 10. Freeze Completion Checklist

| Requirement | Status |
|---|---|
| Final experimental configuration identified | Completed |
| Random seeds documented | Completed |
| Raw experimental results preserved | Completed |
| Summary results preserved | Completed |
| Four final graphs generated | Completed |
| Summary verification performed | Completed |
| Dependencies documented | Completed |
| Reproduction instructions documented | Completed |
| Fresh external clone tested | Pending |
| Final Git working tree verified clean | Pending |

## 11. Final Freeze Statement

The project has completed its main experimental evaluation and generated the associated summary tables and figures.

The experimental baseline is identified by commit:

`84575433d90b8d357c2634e04fb0c3964f7eb4bd`

The final reproducibility stage requires an independent fresh clone, environment setup, experiment execution and verification.

The project should be considered fully reproducible only after that independent test succeeds.
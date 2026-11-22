
# Project Setup Guide

## 1. Project Requirements

This project uses Python to simulate maze-solving algorithms and evaluate their performance.

Required software:

- Python
- Git
- Visual Studio Code (recommended)

## 2. Clone the Repository

Open a terminal and execute:

```bash
git clone https://github.com/Neerajlo/foundations-d2-maze-solving-robot.git
```

Navigate into the project directory:

```bash
cd foundations-d2-maze-solving-robot
```

All project commands should be executed from the repository root directory.

## 3. Verify Python Installation

Check the installed Python version:

```bash
python --version
```

## 4. Install Dependencies

Install the required Python packages:

```bash
python -m pip install -r requirements.txt
```

The project dependencies are:

| Package | Purpose |
|---|---|
| matplotlib | Generate experiment graphs and visualizations |
| pandas | Process experimental data |
| pytest | Execute automated tests |
| python-docx | Generate Word documents for paper-related work |

Verify the installed packages:

```bash
python -m pip check
```

## 5. Generate Maze Datasets

Generate the sample maze files:

```bash
python -m src.maze_generator
```

The generator creates:

- Small mazes: 10 × 10
- Medium mazes: 20 × 20
- Large mazes: 30 × 30

It uses seeds 42, 43 and 44.

Generated JSON files are saved in:

```text
data/raw/
```

**Important:** Running the generator again overwrites files with matching names in `data/raw/`. Back up existing data before regenerating it.

## 6. Run the Main Maze Simulation

Execute:

```bash
python -m src.main
```

This program loads maze files from `data/raw/` and evaluates:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- A* Search
- Reactive A*

The output is saved to:

```text
results/maze_results.csv
```

## 7. Run the Partial-Observation Simulation

Execute:

```bash
python -m src.partial_observation
```

This simulation uses the Robot class and D* Lite planner to navigate a maze with incomplete initial knowledge.

It records navigation performance, discovered obstacles and replanning information.

The output is saved to:

```text
results/dstar_lite_navigation_results.csv
```

## 8. Run the Main Experimental Evaluation

Execute:

```bash
python run_experiments.py
```

The experiment runner evaluates five algorithms under two observation scenarios.

Configuration:

- 10 random seeds (42–51)
- Three maze sizes
- Three fully visible algorithms
- Two partial-observation algorithms
- 150 total experiments

Generated files:

```text
results/
├── experiment_results.csv
├── experiment_summary.csv
└── experiment_failures.csv
```

**Important:** This command overwrites these three CSV files. Back up existing results before executing it.

## 9. Generate Week 12 Graphs

After the experiment summary has been generated, execute:

```bash
python create_charts.py
```

The four graphs are saved in:

```text
results/week12_graphs/
```

Generated graphs:

- nodes_expanded.png
- path_length.png
- runtime_seconds.png
- peak_memory_kb.png

The graphs display mean values and standard-deviation error bars.

## 10. Run Automated Tests

Execute:

```bash
python -m pytest src/ -v
```

This runs the automated pytest suite located under `src/`.

## 11. Important Notes

- Run commands from the repository root.
- Install dependencies before running the project.
- Generate maze data before running `src.main`.
- The main experiment runner and maze generator overwrite certain existing output files.
- Back up important experimental results before regenerating them.
- Runtime and memory measurements may vary across machines and execution environments.

# Week 10 - Required Extension

## Extension
Maze Difficulty Classification and Dataset Metadata Generation.

## Implementation
- Read 9 generated maze JSON files.
- Calculated maze dimensions and total cells.
- Counted obstacles and free cells.
- Calculated obstacle density.
- Classified mazes as Easy, Medium, or Hard.
- Exported results to data/processed/maze_metadata.csv.

## Integration
The extension uses the existing maze generator output and does not modify BFS, DFS, A*, or D* Lite implementations.

## Testing
The extension successfully analyzed 9 maze files and generated the metadata CSV. Existing project tests were executed separately.

## Deliverables
- src/maze_extension.py
- data/processed/maze_metadata.csv
- docs/WEEK10_REPORT.md

## Conclusion
The project now includes automated maze dataset analysis and difficulty classification.

import csv

from src.solver import reactive_astar
from src.reactive_astar_experiment import reactive_astar_with_visit_penalty
from src.external_dataset_loader import load_movingai_scenario


MAP_FILE = "datasets/maze512-1-0.map"
SCENARIO_FILE = "datasets/maze512-1-0.map.scen"

SCENARIOS = [100, 102, 104, 107]
PENALTIES = [0.0, 0.1, 0.25, 0.5]

OUTPUT_FILE = "results/week10_navigation_validation.csv"


def run_validation():

    results = []

    print("\nWEEK 10 NAVIGATION VALIDATION")
    print("=" * 60)

    for scenario_index in SCENARIOS:

        print(f"\nTesting Scenario {scenario_index}")

        # Original Reactive A*
        maze, scenario = load_movingai_scenario(
            MAP_FILE,
            SCENARIO_FILE,
            scenario_index
        )

        original = reactive_astar(maze)

        results.append({
            "scenario": scenario_index,
            "algorithm": "Original",
            "penalty": "",
            "success": original["success"],
            "distance": original["actual_distance"],
            "nodes_expanded": original["nodes_expanded"],
            "replans": original["replan_count"],
            "obstacles_discovered": original["obstacles_discovered"],
            "revisited_moves": "",
            "final_position": original["final_position"]
        })

        print("Original distance:", original["actual_distance"])

        # Enhanced Reactive A* with different penalties
        for penalty in PENALTIES:

            maze, scenario = load_movingai_scenario(
                MAP_FILE,
                SCENARIO_FILE,
                scenario_index
            )

            enhanced = reactive_astar_with_visit_penalty(
                maze,
                visit_penalty=penalty
            )

            results.append({
                "scenario": scenario_index,
                "algorithm": "Enhanced",
                "penalty": penalty,
                "success": enhanced["success"],
                "distance": enhanced["actual_distance"],
                "nodes_expanded": enhanced["nodes_expanded"],
                "replans": enhanced["replan_count"],
                "obstacles_discovered": enhanced["obstacles_discovered"],
                "revisited_moves": enhanced["revisited_moves"],
                "final_position": enhanced["final_position"]
            })

            print(
                f"Penalty {penalty}: "
                f"Success={enhanced['success']}, "
                f"Distance={enhanced['actual_distance']}, "
                f"Replans={enhanced['replan_count']}, "
                f"Revisited={enhanced['revisited_moves']}"
            )

            # Navigation validation
            assert enhanced["success"], (
                f"Scenario {scenario_index} failed "
                f"with penalty {penalty}"
            )

            assert enhanced["final_position"] == maze.goal, (
                f"Robot did not reach goal in scenario {scenario_index}"
            )

            assert (
                enhanced["replan_count"]
                == enhanced["obstacles_discovered"]
            ), (
                f"Unexpected obstacle/replanning count "
                f"in scenario {scenario_index}"
            )

        assert original["success"], (
            f"Original algorithm failed in scenario {scenario_index}"
        )

    # Save validation results
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=results[0].keys()
        )

        writer.writeheader()
        writer.writerows(results)

    print("\n" + "=" * 60)
    print("VALIDATION COMPLETED")
    print("Total experiments:", len(results))
    print("Results saved to:", OUTPUT_FILE)


if __name__ == "__main__":
    run_validation()
# Lesson 2 teacher guide — Data structures on the board

Open the fleet checkpoint first and point to the live data panel. Ask students to predict which occupied cells change when x, y or vertical changes. Define a data structure, then connect each structure to that prediction.

The tuple represents a board cell, the dictionary represents a ship and the list contains separate ship dictionaries. Coordinates are zero-based columns and rows. The Scout length is two cells and the Cruiser length is three. Lengths and placement validation use the existing board.py rules.

Use the incremental guide for the two-hour schedule and acceptance checks. Slides 5, 14 and 16 contain actual screenshots captured from the Python checkpoints. The white outline identifies the selected starting cell. Gold outlines identify the selected ship and green outlines identify other ships.

The core demonstration moves a horizontal Scout from `(2, 3)` to `(4, 1)`, then rotates it. Its occupied cells change from `[(2, 3), (3, 3)]` to `[(4, 1), (5, 1)]`, then to `[(4, 1), (4, 2)]`. Have students state each prediction before clicking.

For the fleet task select index 1 and place the Cruiser at `(6, 2)`. It occupies `[(6, 2), (6, 3), (6, 4)]`. Verify the Scout remains at its previous position. Try an overlapping placement and an edge placement. Rejection must leave the saved record unchanged.

The teacher supplies window setup, rendering, mouse conversion and calls to cells/can_place. Students focus on choosing structures, accessing entries and changing records. The optional set exercise stays in the terminal examples.

[Incremental tasks and schedule](../days/day02/increments/README.md)

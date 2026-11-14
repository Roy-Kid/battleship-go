# Lesson 2 — Data structures on the Battleship board

A data structure organizes related values and provides operations to access or update them. This lesson applies tuples, dictionaries and lists to a visible 10×10 game board.

## Run the checkpoints

Activate the course Python environment and enter this directory.

```bash
python data_structures.py
python 00_scalars.py
python 01_position.py
python 02_ship_record.py
python 03_fleet.py
```

Copy this entire directory with its assets, board.py and requirements.txt for independent use. Install the pinned dependency with `python -m pip install -r requirements.txt` if needed.

## The data controls the board

Coordinates are zero-based `(column, row)` pairs. `(2, 3)` identifies column 2 and row 3. A ship's x/y fields store its starting cell. The supplied renderer converts those cells into pixels.

| Checkpoint | Student data | Visible game behavior |
|---|---|---|
| 00 | Separate column and row values | A white outline marks one board cell |
| 01 | `position = (2, 3)` | Clicking another cell replaces the tuple and moves the outline |
| 02 | One ship dictionary | x/y place the ship, its name determines length, vertical controls orientation |
| 03 | A fleet list with two independent records | 1/2 selects a record, clicking moves its ship, R rotates it |

The right-hand panel displays current data and occupied cells. Students can compare a changed value with the exact board change.

## Step 1 — A tuple selects a cell

Run `01_position.py`. Predict where the outline appears for `position = (2, 3)`, then click `(4, 1)`. Read the panel and explain how both tuple entries changed. In the source, change the initial tuple and run again. Tuple entries cannot be assigned individually. Assign a new tuple to select another cell.

## Step 2 — A dictionary describes a ship

Run `02_ship_record.py`.

```python
ship = {'name': 'Scout', 'x': 2, 'y': 3, 'vertical': False}
```

The Scout occupies `(2, 3)` and `(3, 3)`. Change x to 4 and y to 1, or click that cell. It now occupies `(4, 1)` and `(5, 1)`. Press R to update vertical and observe `(4, 1)` and `(4, 2)`. The panel lists the cells for direct comparison.

Change name to `Cruiser` while the ship has room. Its length changes from two cells to three using the existing LENGTHS rule. Record one prediction before changing each field.

## Step 3 — A list organizes the fleet

Run `03_fleet.py`. The initial fleet contains a horizontal Scout at `(2, 3)` and a vertical Cruiser at `(5, 6)`.

1. Press 2 to choose `fleet[1]`, then click `(6, 2)`.
2. Verify that the Cruiser occupies `(6, 2)`, `(6, 3)` and `(6, 4)`.
3. Verify that `fleet[0]` still occupies `(2, 3)` and `(3, 3)`.
4. Press 1 and try placing the Scout on the Cruiser. Read the rejection message and confirm that the saved record stays at its valid position.
5. Try placing a horizontal Scout at `(9, 9)`. Explain why it would leave the board.

Two list entries need separate dictionaries for independent ships. Predict the effect of `fleet = [ship, ship]` using the terminal examples.

## Course task coverage

| Task | Material | Evidence |
|---|---|---|
| Tuple lookup and reassignment | 01 and terminal examples | Predict and select a specific cell |
| Dictionary lookup and field updates | 02 | Change location, length and orientation on the board |
| List indexing and nested access | 03 | Move one fleet member independently |
| List append and len | Terminal examples | Explain the item count after append |
| Shared references | Terminal examples and slide 12 | Explain why two references can change together |
| Structure choice and access errors | Slides 17–20 | Justify choices and diagnose one error |
| Optional set deduplication | Terminal examples and slide 18 | Repeated target coordinates count once |

## Two-hour lesson

| Minutes | Activity |
|---|---|
| 0–15 | Demonstrate 03 and identify the data shown beside the board |
| 15–35 | Definitions and small tuple, list and dictionary examples |
| 35–60 | Predict nested updates and shared references |
| 60–75 | Apply 01 and 02, matching slides 5 and 14 |
| 75–85 | Break |
| 85–100 | Apply 03, matching slide 16, then verify the occupied cells |
| 100–110 | Optional set example and access-error exercise |
| 110–120 | Each student demonstrates a data edit and explains the board change |

Window handling, mouse conversion, drawing and placement checks are teacher supplied. board.py is copied from the existing Day 4 rules so cells, lengths and valid placements follow the rest of the game. Each graphical file supports `--smoke` for a one-frame startup check.

Exit task — choose a position tuple, one ship dictionary and a fleet list, then demonstrate an update to each on the board.

[Course slides](../../../slides/day02.html)

Sea assets come from Water+ by ninjikin. Ship assets come from Sea Warfare set. Source links and credits are in the course README.

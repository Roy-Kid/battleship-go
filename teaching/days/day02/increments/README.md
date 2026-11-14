# Lesson 2 — File and slide edit guide

The core route uses three runnable checkpoints. Scalar and tuple work share one ten-minute activity. The main editing time is for dictionary fields and independent records in a fleet list.

## Prepare the files

Copy this entire increments directory with assets, board.py and requirements.txt. Use Python 3.13 with the pinned Pygame dependency. Run commands from this directory.

```bash
python 01_position.py
python 02_ship_record.py
python 03_fleet.py
```

Keep personal working copies. For each source edit, predict the board result, save, close the old game window and restart the same file. The line numbers below refer to the distributed files. The EDIT/READ comments remain searchable if students insert their own lines.

## Every task maps to its file and slide

| Task | PPT page | Python file | Line(s) | Change or action | Expected board result |
|---|---|---|---|---|---|
| A1/A2 | 4 | 01_position.py | 24 | (2,3) → (4,1), then (1,4) | White cell outline moves to each tuple coordinate. |
| B1 | 5 | 02_ship_record.py | 26–27 | x=4, y=1 | Horizontal Scout covers (4,1), (5,1). |
| B2 | 6 | 02_ship_record.py | 28 | vertical=True, keeping B1 | Scout covers (4,1), (4,2). |
| B3 | 7 | 02_ship_record.py | 25 | name='Cruiser', keeping B1/B2 | Cruiser covers (4,1), (4,2), (4,3). |
| B4 | 8 | 02_ship_record.py | 56 (read) | Click (6,2), keeping the B3 file | During this run Cruiser covers (6,2), (6,3), (6,4). |
| C1 | 10 | 03_fleet.py | 26 | Second record x=6, y=2 | Cruiser moves. Scout stays at (2,3), (3,3). |
| C2 | 11 | 03_fleet.py | 29 | selected=1, keeping C1 | Cruiser gets the gold selection outline. Positions stay the same. |
| C3 | 12 | 03_fleet.py | 25 | First record x=4, y=1, keeping C1/C2 | Scout moves to (4,1), (5,1). Cruiser keeps its C1 cells. |
| D | 13 | 03_fleet.py | 55–57 (read) | Press 1. Click (6,2), then (9,9). | Both clicks are rejected. Scout keeps its C3 data and cells. |

## A1/A2 — Compact scalar and tuple activity

Spend at most two minutes comparing `00_scalars.py` line 23, `col, row = 2, 3`, with `01_position.py` line 24, `position = (2, 3)`. Both select one cell. Students make their edits in 01_position.py.

At line 24, replace the starting tuple with `(4, 1)`. Save and restart to see the white outline at column 4 and row 1. Replace it again with `(1, 4)` and repeat. Index 0 is the column and index 1 is the row. The tuple is an ordered sequence whose entries cannot be replaced individually. Assign a new tuple to express a new pair.

## B1–B4 — Change one ship dictionary

Open 02_ship_record.py with its supplied default record. Keep edits B1, B2 and B3 cumulatively in this file.

1. B1 changes lines 26–27 to `'x': 4,` and `'y': 1,`. The Scout moves horizontally from `[(2, 3), (3, 3)]` to `[(4, 1), (5, 1)]`.
2. B2 changes line 28 to `'vertical': True,`. Its start stays `(4, 1)` and its cells become `[(4, 1), (4, 2)]`.
3. B3 changes line 25 to `'name': 'Cruiser',`. Keep the B1/B2 fields. The existing LENGTHS rule now gives three cells, `[(4, 1), (4, 2), (4, 3)]`.
4. B4 reads line 56 and requires no source edit. Click `(6, 2)` during the B3 run. The accepted click updates the same dictionary and moves its cells to `[(6, 2), (6, 3), (6, 4)]`. Restarting reads the saved source record at `(4, 1)` again.

A dictionary maps unique keys to values. Students identify which field caused each visible change. Read the existing input and drawing support to trace the effect.

## C1–D — Edit independent records in a fleet list

Open 03_fleet.py fresh. This separate checkpoint has its own initial Scout and Cruiser records. Keep C1, C2 and C3 cumulatively in this file.

1. C1 edits only the second record at line 26 to `{'name': 'Cruiser', 'x': 6, 'y': 2, 'vertical': True},`. Scout keeps its initial two cells.
2. C2 edits line 29 to `selected = 1`. Cruiser gets the selection outline and data panel. This changes the selected list index while both positions remain the same.
3. C3 edits only the first record at line 25 to `{'name': 'Scout', 'x': 4, 'y': 1, 'vertical': False},`. Scout moves, while Cruiser keeps the C1 cells. Press 1 to inspect Scout in the panel.
4. D requires no source edit. Read lines 55–57. With the saved C3 data, press 1 and click `(6, 2)` to attempt overlap, then `(9, 9)` to attempt an edge placement. Both must preserve Scout at `(4, 1)`.

A list is an ordered mutable sequence. Indices 0 and 1 choose different dictionary records. The game panel prints the selected record and its exact occupied cells.

## Optional terminal examples

| PPT page | File and line | Student edit | Expected output and board effect |
|---|---|---|---|
| 15 | data_structures.py line 14 | Change append argument from Carrier to Rescue | Three names ending in Rescue. The running board is unchanged. |
| 16 | data_structures.py line 25 | Change assigned x from 6 to 7 | Both references to the first dictionary report 7. The second record keeps x=5. The running board is unchanged. |
| 17 | data_structures.py line 32 | Add the tuple (6,2) | Three distinct targets. The running board is unchanged. |

These examples run separately from the required game tasks. A set stores distinct values without positional indexing. It is an extension for this lesson.

## Two-hour schedule

| Minutes | Slides and work |
|---|---|
| 0–10 | Pages 1–3, demonstrate the final board and define the structures |
| 10–20 | Page 4, compact scalar comparison and tuple edits A1/A2 |
| 20–35 | Page 5, dictionary position edit B1 |
| 35–45 | Page 6, orientation edit B2 |
| 45–60 | Page 7, ship-name and length edit B3 |
| 60–75 | Page 8, runtime click trace B4 and individual checks |
| 75–85 | Page 9, break |
| 85–100 | Pages 10–11, second fleet record and selected index C1/C2 |
| 100–110 | Pages 12–13, independent first-record edit C3 and rejection checks D |
| 110–120 | Page 14, individual demonstration and explanation |

Pages 15–17 are optional references. Each student shows the edited source line, predicts the cells, runs the file and compares the board with the prediction.

The renderer and input support are supplied. Existing cells/can_place behavior is reused from board.py. main.py matches 03_fleet.py. starter.py matches the scalar comparison.

[Open the English slide deck](../../../slides/day02.html)

Sea assets come from Water+ by ninjikin. Ship assets come from Sea Warfare set. Course credits contain their source links.

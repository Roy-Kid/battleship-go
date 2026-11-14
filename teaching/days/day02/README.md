# Lesson 2 — Data structures

The lesson uses a visible 10×10 Battleship board. A tuple selects a cell, a dictionary describes a ship and a list organizes the fleet. The game shows current values and occupied cells beside the board.

## Definitions

| Structure | Definition | Board application |
|---|---|---|
| tuple | An ordered sequence whose entries cannot be replaced | A `(column, row)` pair |
| dict | A mapping from unique keys to values | A ship's name, x, y and orientation |
| list | An ordered mutable sequence | Multiple independent ship records |
| set | A collection of distinct values | Optional example of unique target cells |

## Start the game

```bash
python starter.py
python main.py
```

The starter displays separate coordinates on the board. main.py is the completed fleet-placement example. Click a cell to place the selected ship, press R to rotate and use 1/2 to choose a ship. x/y values are zero-based column/row coordinates. The supplied rules reject overlap and out-of-bounds placement.

## Incremental classroom route

```bash
python increments/00_scalars.py
python increments/01_position.py
python increments/02_ship_record.py
python increments/03_fleet.py
```

For a concrete experiment, the horizontal Scout at `(2, 3)` covers `(2, 3)` and `(3, 3)`. Move it to `(4, 1)` and predict its new cells. Rotate it and compare the two cells again. Then select the Cruiser through fleet[1] and verify that moving it leaves the Scout's record unchanged.

Minimum outcome is a tuple selecting a cell and a dictionary controlling a ship. Standard outcome is two independently placed ships with an explanation of nested list/dictionary access. The set example is optional.

[Full tasks, acceptance checks and 120-minute plan](increments/README.md)

[English slides](../../slides/day02.html)

[Teacher guide](../../slides/day02_teacher.md)

Keep the complete folder with assets, board.py and requirements.txt. Asset credits are in the course README.

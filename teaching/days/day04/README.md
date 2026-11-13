# Day 4: Functions

Two hours. Core programming concept: **functions**. Other syntax is review or teacher-supplied support.

## Core concept: functions

**Definition:** A function is a named block of instructions that can receive arguments and return a result.

**Example:**

```python
from board import cells
ship = {'name': 'Scout', 'x': 2, 'y': 3, 'vertical': False}
print(cells(ship))  # [(2, 3), (3, 3)]
```

**Explain it:** Identify the argument and returned value in cells(ship). Explain how can_place uses its result.

The game feature is an application of this concept. Assess whether you can explain and use the concept, as well as run the game.

## Run

Enter this directory in an active Python 3.13 environment:

```bash
python starter.py
# Reference result:
python main.py
```

`starter.py` is the classroom starting point; `main.py` is the reference solution. Build today's feature from the previous working version.

## Student tasks

First define and call the small report_position example from the slides in a separate practice file. Then identify parameters and returned results in board.py. Represent a ship by its start cell and orientation. Call can_place before committing a placement, and color previews red or green.

## Teacher supplied

board.py is a verified tool supplied by the teacher. Read cells, then use can_place; students do not need to rewrite every helper in one lesson.

## Challenge and checks

Use Space for a random fleet, 1/2/3 to reselect a ship, and R to rotate. When moving a named ship, exclude its previous occupied cells.

Predict, run, then explain. Save a working version after each step. This folder includes independent source and assets; copy it whole without neighboring day folders.

Sea: Water+ / ninjikin. Ships: Sea Warfare set. See [course credits](../../README.md#assets).

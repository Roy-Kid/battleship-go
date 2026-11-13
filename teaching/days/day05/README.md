# Day 5: Conditional branching

Two hours. Core programming concept: **conditional branching**. Other syntax is review or teacher-supplied support.

## Core concept: conditional branching

**Definition:** A conditional chooses which block of instructions runs according to whether a condition is true or false.

**Example:**

```python
result = {'kind': 'miss', 'ship': None}
if result['kind'] == 'miss':
    message = 'Try another cell'
else:
    message = 'Ship hit!'
print(message)
```

**Explain it:** Predict which branch runs for miss, hit and sunk. Does assigning = test equality?

The game feature is an application of this concept. Assess whether you can explain and use the concept, as well as run the game.

## Run

Enter this directory in an active Python 3.13 environment:

```bash
python starter.py
# Reference result:
python main.py
```

`starter.py` is the classroom starting point; `main.py` is the reference solution. The starter includes the placement, firing and drawing support; replace its marked feedback placeholder with your own conditional chain.

## Student tasks

Press Enter to lock your fleet. The teacher supplies the fire call and shot-recording scaffold. After a valid result, write if/elif/else branches that select MISS, SUNK or HIT feedback. Click the right board to apply the branch to real results. Keep the existing phase and coordinate guards.

## Teacher supplied

This is shooting practice without alternating turns or final victory. board.py keeps the same interface.

## Challenge and checks

Click a target twice and check that the shot count does not increase. Explain why shots needs to remember history.

Predict, run, then explain. Save a working version after each step. This folder includes independent source and assets; copy it whole without neighboring day folders.

Sea: Water+ / ninjikin. Ships: Sea Warfare set. See [course credits](../../README.md#assets).

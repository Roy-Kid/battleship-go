# Day 6: State machines

Two hours. Core programming concept: **state machines**. Other syntax is review or teacher-supplied support.

**Goal:** Finish a shooting practice game with sinking, victory, score and accuracy.

Materials: [slides](../../slides/day06.html), [teacher guide](../../slides/day06_teacher.md), [Week 2 plan](../../week02.md).

## Core concept: state machines

**Definition:** A state machine represents a program as named states and transitions. An event changes state only when its transition rule allows it.

**Example:**

```python
phase = 'battle'
sunk = 3
if phase == 'battle' and sunk == 3:
    phase = 'finished'
print(phase)  # finished
```

**Explain it:** Name the states before and after victory, the event that triggers the transition, and an action forbidden after it.

The game feature is an application of this concept. Assess whether you can explain and use the concept, as well as run the game.

## Start here

Enter this directory with Python 3.13 and the course requirements installed:

```bash
python starter.py
# Reference result:
python main.py
```

The Day 5 shooting practice: ships can be placed and targets can be fired on, but no final score or win state is shown.

## Trace the state machine

| Current phase | Event | Next phase |
|---|---|---|
| placement | Enter with a complete fleet | battle |
| placement | Enter with an incomplete fleet | placement |
| battle | A valid shot, fewer than three sunk ships | battle |
| battle | The final enemy ship is sunk | finished |
| finished | Another board click | finished; no new attack |

Before editing, trace one legal path from placement to finished and one blocked action. The statistics line is an output of the current records and phase; it must not create another changing score state.

## Student tasks

1. Run `starter.py`. Place three ships (or press Space), then Enter to start. Fire twice at the same target and explain why the second click changes nothing.
2. Open `board.py`. Trace how `fire` returns `miss`, `hit` or `sunk`. The last hit on a ship returns `sunk`; it counts as a hit too. The helper already detects sinking, so do not add another detector.
3. In `starter.py`, immediately after the successful `fire(...)` call, check `statistics(shots)['sunk'] == 3`. Set `phase = 'finished'` and a win message. Keep the existing `phase == 'battle'` input guard.
4. After drawing the boards, call `statistics(shots)` and display score, hits/shots and accuracy with the existing `text` helper. Add the 100-point victory bonus to the displayed total when finished. Derive it from phase instead of adding it every frame.
5. Compare only these edits with `main.py`, then test the cases below.

## Guided experiment and reference

Create a temporary `practice.py` in this folder and run it separately from the game:

```python
from board import fire, statistics, validate_fleet

fleet = validate_fleet([
    {'name': 'Carrier', 'x': 0, 'y': 0, 'vertical': False},
    {'name': 'Cruiser', 'x': 0, 'y': 2, 'vertical': False},
    {'name': 'Scout', 'x': 0, 'y': 4, 'vertical': False},
])
shots = {}
print(statistics(shots))
fire(fleet, shots, 9, 9)  # miss
for x in range(4):
    print(fire(fleet, shots, x, 0)['kind'])
print(statistics(shots))
```

Predict first. Answers: initially all statistics are 0; results are hit, hit, hit, sunk; then shots=5, hits=4, sunk=1, accuracy=80, score=90. `statistics` reports the base score; the match/UI adds the victory bonus.

## Acceptance checks

| Case | Expected result |
|---|---|
| No shots | 0 shots, 0% accuracy, no division error. |
| Partial ship | The first three Carrier cells return hit; the fourth returns sunk. |
| Repeated target | No new record, score or sunk count. |
| Complete fleet | 9 hits and 3 sinkings: base score 240, victory total 340. |
| After victory | Further board clicks cannot fire or change score. |

Predict before running. Record expected and actual behavior, then explain any difference. Keep a working copy after each step.

## Challenge and exit question

Add a ships-sunk label using the existing statistics result. Explain why misses lower accuracy without reducing score.

Exit question: Explain how a sunk result differs from a hit, and why the victory bonus stays 100 even after many frames.

## Teacher supplied

The local board.py already provides fire and statistics. Read and call them directly. This lesson still has no computer turn and no networking.

This directory contains independent code and assets. Copy the whole folder. Sea: Water+ / ninjikin; ships: Sea Warfare set. See [course credits](../../README.md#assets).

# Day 7: Algorithms

Two hours. Core programming concept: **algorithms**. Other syntax is review or teacher-supplied support.

**Goal:** Alternate valid shots with a computer that chooses an untried cell.

Materials: [slides](../../slides/day07.html), [teacher guide](../../slides/day07_teacher.md), [Week 2 plan](../../week02.md).

## Core concept: algorithms

**Definition:** An algorithm is a precise sequence of steps for solving a problem. Its inputs and rules determine the permitted outputs.

**Example:**

```python
import random
incoming = {'0,0': {'kind': 'miss', 'ship': None}}
choices = [(x, y) for x in range(10) for y in range(10)
           if f'{x},{y}' not in incoming]
print(len(choices))  # 99
target = random.choice(choices)
```

**Explain it:** Explain the select-untried-target algorithm as input, steps and output. Why can it never repeat a recorded target?

The game feature is an application of this concept. Assess whether you can explain and use the concept, as well as run the game.

## Start here

Enter this directory with Python 3.13 and the course requirements installed:

```bash
python starter.py
# Reference result:
python main.py
```

The completed Day 6 game, including score and victory, is provided in starter.py.

## Student tasks

1. Add `incoming = {}`, `my_turn = True` and `ai_at = 0` beside `shots`. Import `random` if needed (the starter already imports it).
2. Add `my_turn` to the existing player attack condition. After a successful `fire`, set `my_turn = False` and `ai_at = pygame.time.get_ticks() + 600`. Keep these updates inside `try`, after validation. A rejected click must not end the turn.
3. Outside the event `for` loop, but inside `while running`, check that phase is battle, it is the computer's turn, and the current time has reached `ai_at`.
4. Build the untried candidate list shown below. Call the existing `fire(fleet, incoming, *random.choice(choices))` once. Check the computer's sunk count; finish if it is 3, otherwise return control to the player.
5. Draw incoming markers on the left board **after** drawing the ships. Compare the corresponding sections with `main.py`.

## Guided experiment and reference

The teacher supplies this selection code:

```python
choices = [(x, y) for x in range(10) for y in range(10)
           if f'{x},{y}' not in incoming]
```

Explain it aloud: visit each board cell, keep it only if it has not been attacked, then choose one. With 7 distinct incoming shots there are 93 choices. `shots` stores your attacks on the enemy; `incoming` stores the computer's attacks on you.

The computer action belongs outside event handling. If it ran only when an event arrived, it could wait forever while the mouse stayed still. A deadline check allows redraw and window closing during the pause.

## Acceptance checks

| Case | Expected result |
|---|---|
| Valid hit or miss | Exactly one computer shot follows; hits do not grant extra turns. |
| Repeated player target | No computer shot is scheduled; your turn remains active. |
| Computer selection | Every new incoming record has a different key. |
| Waiting | Window remains responsive during the 600 ms delay. |
| Victory or defeat | Attacks stop on either outcome; only a player win earns the player victory bonus. |

Predict before running. Record expected and actual behavior, then explain any difference. Keep a working copy after each step.

## Challenge and exit question

Change the delay to 300 or 1000 ms and explain the effect. Keep the same rules. Optionally outline a smarter targeting idea without implementing it.

Exit question: Why does the computer choose from incoming rather than shots? Why is the deadline check outside the event loop?

## Teacher supplied

Keep drawing and board.py. The teacher supplies the candidate-list comprehension and explains its meaning. Use pygame.time.get_ticks for the 600 ms delay; the game loop must keep processing events.

This directory contains independent code and assets. Copy the whole folder. Sea: Water+ / ninjikin; ships: Sea Warfare set. See [course credits](../../README.md#assets).

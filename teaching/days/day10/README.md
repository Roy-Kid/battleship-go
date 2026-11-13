# Day 10: Testing

Two hours. Core programming concept: **testing**. Other syntax is review or teacher-supplied support.

**Goal:** Add a statistics line and three recent battle reports, then demonstrate a verified personal edition.

Materials: [slides](../../slides/day10.html), [teacher guide](../../slides/day10_teacher.md), [Week 2 plan](../../week02.md).

## Core concept: testing

**Definition:** A test compares observed behavior with an expected result for a chosen input or action.

**Example:**

```python
reports = ['A1 miss', 'B2 hit', 'C3 miss', 'D4 sunk']
expected = ['B2 hit', 'C3 miss', 'D4 sunk']
actual = reports[-3:]
print(actual == expected)  # True
```

**Explain it:** Choose a normal case and an edge case, predict each result, then record actual behavior and decide whether it passes.

The game feature is an application of this concept. Assess whether you can explain and use the concept, as well as run the game.

## Start here

Enter this directory with Python 3.13 and the course requirements installed:

```bash
python starter.py  # Start in solo mode. See multiplayer commands below.
```

starter.py is the Day 9 integrated game with a statistics placeholder and one recent report. Edit it directly. main.py is the finished reference, equivalent to the refactored edition.

## Student tasks

1. Before editing, predict the latest-three output for empty, one-item, three-item and four-item report lists. Record those expected results. Run `python starter.py` in solo mode. Find the placeholder `Battle statistics arrive in Day 10.` and the preceding `me = state['me']`.
2. Replace the placeholder text call with the statistics call below. Use snapshot values directly; the score already includes the victory bonus when appropriate.
3. Find the report loop `enumerate(state['log'][-1:])` and change the slice to `[-3:]`. Keep the existing 24-pixel line spacing and the `if not editable` guard so reports do not collide with placement controls.
4. Choose one personal change: title, colors or the wording/order of statistics. Keep text within the window and retain recognizable turn and win feedback.
5. Compare with `main.py`, then exchange projects with a partner. Run the checklist, fix one observed problem, rerun the affected checks and present your result.

## Guided experiment and reference

Use the existing text helper:

```python
text(f"Score {me['score']}   Hits {me['hits']}/{me['shots']}   Accuracy {me['accuracy']}%",
     60, 520, face=small)
```

Recent reports:

```python
if not editable:
    for i, line in enumerate(state['log'][-3:]):
        text(line, 60, 565 + i * 24, face=small)
```

`[-3:]` safely gives up to three items, even if the list is shorter or empty. `enumerate` pairs each report with 0, 1 or 2 for its vertical position. The server retains up to four reports; the client chooses to display three.

For multiplayer checks, use separate terminals:

```bash
python server.py
python starter.py --connect 127.0.0.1 --name Alice
python starter.py --connect 127.0.0.1 --name Bob
```

Use `main.py` for the reference result. LAN setup is the same as Day 9, port 65432.

## Acceptance checks

| Case | Expected result |
|---|---|
| Statistics | Before firing: 0 shots and 0% accuracy; known hit/miss counts match display. |
| Victory | Final player win is 340 points; leaving the screen open does not add more. |
| Reports | At 0, 1, 2 and 4 entries, show up to the latest 3 in order with no overlap. |
| Regression | Valid placement, locked readiness, alternating turns and duplicate rejection still work. |
| Rematch and exit | Both votes reset round statistics; wins persist; disconnect and exit remain clear. |

Predict before running. Record expected and actual behavior, then explain any difference. Keep a working copy after each step.

## Challenge and exit question

Present a two-minute demo: describe the game, show your change, explain one rule, and show a bug with its fix. Save source and a screenshot with a short reflection.

Exit question: Which snapshot fields did you display, and which check gives evidence that your change works?

## Teacher supplied

Reuse the validated rules and the server snapshot. The me dictionary already contains score, hits, shots and accuracy; avoid a second scoring formula in the client.

This directory contains independent code and assets. Copy the whole folder. Sea: Water+ / ninjikin; ships: Sea Warfare set. See [course credits](../../README.md#assets).

# Day 4 teacher guide: Functions

**One core concept: functions.** A function is a named block of instructions that can receive arguments and return a result.

[Student lesson](../days/day04/README.md) · [Slides](day04.html). Audience: 3–5 beginner students around age 15. Duration: 120 minutes.

## Preparation

Copy the entire daily directory, including assets. Run its starter and reference with the course Python environment. Open the HTML deck with the shared theme.css and presentation.js alongside it. N shows slide notes. Introduce the definition before showing game code.

## Two-hour schedule

| Minutes | Activity | Evidence |
|---|---|---|
| 0–15 | Recall the previous concept and show today's game result | Student identifies the data being changed |
| 15–35 | Trace arguments and returned values | Prediction before execution |
| 35–75 | Call cells and can_place for placement | Working student change |
| 75–85 | Break | Saved source |
| 85–110 | Explain a successful and rejected placement | Recorded expected/actual behavior |
| 110–120 | Explain the concept and demonstrate | Independent exit answer |

## Example and explanation

```python
from board import cells
ship = {'name': 'Scout', 'x': 2, 'y': 3, 'vertical': False}
print(cells(ship))  # [(2, 3), (3, 3)]
```

Ask students to predict, run and explain this example before applying it to the game. Keep unfamiliar event, drawing and timing support supplied. Use the student lesson for the exact game edits.

Exit question: Identify the argument and returned value in cells(ship). Explain how can_place uses its result.

## Assessment

Minimum: explain the definition in their own words and complete the smallest example with guidance. Standard: independently apply it to the game and justify the expected result. Extension: transfer the concept to a second example. Ask questions while a partner diagnoses; each student saves and explains their own file.

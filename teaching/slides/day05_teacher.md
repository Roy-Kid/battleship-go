# Day 5 teacher guide: Conditional branching

**One core concept: conditional branching.** A conditional chooses which block of instructions runs according to whether a condition is true or false.

[Student lesson](../days/day05/README.md) · [Slides](day05.html). Audience: 3–5 beginner students around age 15. Duration: 120 minutes.

## Preparation

Copy the entire daily directory, including assets. Run its starter and reference with the course Python environment. Open the HTML deck with the shared theme.css and presentation.js alongside it. N shows slide notes. Introduce the definition before showing game code.

## Two-hour schedule

| Minutes | Activity | Evidence |
|---|---|---|
| 0–15 | Recall the previous concept and show today's game result | Student identifies the data being changed |
| 15–35 | Evaluate true/false comparisons | Prediction before execution |
| 35–75 | Choose feedback after fire returns a result | Working student change |
| 75–85 | Break | Saved source |
| 85–110 | Trace miss, hit and sunk branches | Recorded expected/actual behavior |
| 110–120 | Explain the concept and demonstrate | Independent exit answer |

## Example and explanation

```python
result = {'kind': 'miss', 'ship': None}
if result['kind'] == 'miss':
    message = 'Try another cell'
else:
    message = 'Ship hit!'
print(message)
```

Ask students to predict, run and explain this example before applying it to the game. Keep unfamiliar event, drawing and timing support supplied. Use the student lesson for the exact game edits.

Exit question: Predict which branch runs for miss, hit and sunk. Does assigning = test equality?

## Assessment

Minimum: explain the definition in their own words and complete the smallest example with guidance. Standard: independently apply it to the game and justify the expected result. Extension: transfer the concept to a second example. Ask questions while a partner diagnoses; each student saves and explains their own file.

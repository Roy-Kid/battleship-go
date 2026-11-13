# Day 3 teacher guide: Loops

**One core concept: loops.** A loop repeats a block of instructions. A for loop visits each item in an iterable, such as range(11).

[Student lesson](../days/day03/README.md) · [Slides](day03.html). Audience: 3–5 beginner students around age 15. Duration: 120 minutes.

## Preparation

Copy the entire daily directory, including assets. Run its starter and reference with the course Python environment. Open the HTML deck with the shared theme.css and presentation.js alongside it. N shows slide notes. Introduce the definition before showing game code.

## Two-hour schedule

| Minutes | Activity | Evidence |
|---|---|---|
| 0–15 | Recall the previous concept and show today's game result | Student identifies the data being changed |
| 15–35 | Trace range and count repetitions | Prediction before execution |
| 35–75 | Draw board lines using a loop | Working student change |
| 75–85 | Break | Saved source |
| 85–110 | Predict line counts and highlight valid cells | Recorded expected/actual behavior |
| 110–120 | Explain the concept and demonstrate | Independent exit answer |

## Example and explanation

```python
for i in range(11):
    print(i)  # 0 through 10: eleven iterations
```

Ask students to predict, run and explain this example before applying it to the game. Keep unfamiliar event, drawing and timing support supplied. Use the student lesson for the exact game edits.

Exit question: Why does a ten-cell board need eleven boundary lines? What changes if range(11) becomes range(10)?

## Assessment

Minimum: explain the definition in their own words and complete the smallest example with guidance. Standard: independently apply it to the game and justify the expected result. Extension: transfer the concept to a second example. Ask questions while a partner diagnoses; each student saves and explains their own file.

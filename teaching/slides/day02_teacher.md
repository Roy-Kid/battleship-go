# Day 2 teacher guide: Data structures

**One core concept: data structures.** A data structure organizes related values and gives us a way to access and update them.

[Student lesson](../days/day02/README.md) · [Slides](day02.html). Audience: 3–5 beginner students around age 15. Duration: 120 minutes.

## Preparation

Copy the entire daily directory, including assets. Run its starter and reference with the course Python environment. Open the HTML deck with the shared theme.css and presentation.js alongside it. N shows slide notes. Introduce the definition before showing game code.

Use the [incremental checkpoints](../days/day02/increments/README.md) alongside the deck. Run `data_structures.py` for slides 5–13, use `01_position.py` and `02_ship_record.py` for the one-ship application on slide 14, then `03_fleet.py` for slides 16–17. Slide 18's set example stays optional. Each checkpoint is complete and runnable; the last is the existing Day 2 reference. The incremental guide gives a slide-aligned schedule with the break at minutes 75–85.

Lesson 1 already demonstrated movement, rotation, scaling and reset. Do not introduce those again as today's new material. Keep event handling, boundary checks and drawing supplied; students change the representation and access of the data.

## Two-hour schedule

| Minutes | Activity | Evidence |
|---|---|---|
| 0–15 | Recall the previous concept and show today's game result | Student identifies the data being changed |
| 15–35 | Inspect tuple, list and dictionary examples | Prediction before execution |
| 35–75 | Group one ship, then store two records | Working student change |
| 75–85 | Break | Saved source |
| 85–110 | Predict nested updates and explain choices | Recorded expected/actual behavior |
| 110–120 | Explain the concept and demonstrate | Independent exit answer |

## Example and explanation

```python
ship = {'name': 'Scout', 'x': 200, 'y': 180}
fleet = [ship]
fleet[0]['x'] += 40
print(fleet[0]['x'])  # 240
```

Ask students to predict, run and explain this example before applying it to the game. Keep unfamiliar event, drawing and timing support supplied. Use the student lesson for the exact game edits.

Exit question: Explain why a ship uses a dictionary, a fleet uses a list, and a position can use a tuple.

## Assessment

Minimum: explain the definition in their own words and complete the smallest example with guidance. Standard: independently apply it to the game and justify the expected result. Extension: transfer the concept to a second example. Ask questions while a partner diagnoses; each student saves and explains their own file.

## Data-structure teaching choices and answer key

Tuple: ordered entries cannot be replaced; use a new tuple to express a new position. List: ordered, mutable sequence for multiple ships. Dictionary: key-based access to fields of one ship. The core practice covers those three; sets are optional for distinct target cells. Do not require event-handling, loop writing, copying semantics or algorithmic complexity today.

The nested-access prediction prints 2, 240, 500, 240. fleet[0] and ship refer to the same dictionary. Two references to one dictionary are not two independent ships; create two records. A dictionary preserves insertion order, but its teaching purpose here is named access. Explain KeyError versus IndexError through one small example, without derailing the core task.

The starter is a working scalar version with keyboard support. Let students refactor one record first. Supply the fleet drawing/selection block when moving to two ships. The image is ship_image; the data record is ship. Pixel x/y values here differ from grid-cell coordinates in Day 4.

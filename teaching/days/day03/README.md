# Day 3: Loops

Two hours. Core programming concept: **loops**. Other syntax is review or teacher-supplied support.

## Core concept: loops

**Definition:** A loop repeats a block of instructions. A for loop visits each item in an iterable, such as range(11).

**Example:**

```python
for i in range(11):
    print(i)  # 0 through 10: eleven iterations
```

**Explain it:** Why does a ten-cell board need eleven boundary lines? What changes if range(11) becomes range(10)?

The game feature is an application of this concept. Assess whether you can explain and use the concept, as well as run the game.

## Run

Enter this directory in an active Python 3.13 environment:

```bash
python starter.py
# Reference result:
python main.py
```

`starter.py` is the classroom starting point; `main.py` is the reference solution. This is a simplified independent scene so today can focus on repetition.

## Student tasks

Draw 11 horizontal and 11 vertical boundaries with a loop. Explain the first and last iteration and predict what range(10) changes. Use the supplied mouse-cell conversion and highlight to see the board redraw during interaction.

## Teacher supplied

The teacher supplies the window, mouse-coordinate conversion and valid-cell highlight from main.py. Students explain and write the repeated drawing; complex containers and inheritance can wait.

## Challenge and checks

Print coordinates on click. Explain why clicking outside the board should not produce a valid target.

Predict, run, then explain. Save a working version after each step. This folder includes independent source and assets; copy it whole without neighboring day folders.

Sea: Water+ / ninjikin. Ships: Sea Warfare set. See [course credits](../../README.md#assets).

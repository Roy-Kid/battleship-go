# Lesson 2 increments: data structures

**One core concept: organize related values and access or update them.**

These experiments follow the [Day 2 slides](../../../slides/day02.html): a tuple for a position, a dictionary for one ship, and a list for a fleet. Keyboard controls were introduced in Lesson 1. Input handling, boundaries and drawing are supplied support throughout this lesson.

## Run and distribute

With the course Python environment active, enter this directory:

```bash
python data_structures.py  # Predict the small examples before running them.
python 00_scalars.py       # Working starting point with separate values.
python 01_position.py      # One coordinate pair: a tuple.
python 02_ship_record.py   # One ship: a dictionary with named fields.
python 03_fleet.py         # Several ships: a list of separate dictionaries.
```

First demonstrate `03_fleet.py` briefly: select a ship with 1/2, then move or rotate it. Ask which values describe one ship and which structure could hold several ships. The goal is to explain the data behind the animation.

Copy this entire directory, including `assets/` and `requirements.txt`, for a standalone student project. It has no runtime dependency on adjacent lessons. The slide links above refer to the full course checkout; distribute the whole `slides/` directory separately if needed. Python 3.13 and Pygame 2.6.1 are the course environment. If necessary, install with `python -m pip install -r requirements.txt`.

## Slide-to-code map

| Slides | Concept or activity | File |
|---|---|---|
| 1–4 | Definition; separate values versus a record | `00_scalars.py`, then the examples below |
| 5–6 | Tuple lookup and assignment of a new tuple | `data_structures.py`, `01_position.py` |
| 7 | List indices, append and length | List section of `data_structures.py` |
| 8–9 | Dictionary keys versus numbered indices | Dictionary section of `data_structures.py` |
| 10–12 | Fleet records, nested access and shared references | Fleet section of `data_structures.py` |
| 13 | Predict, run and explain the small examples | `data_structures.py` |
| 14 | Apply the structures to one ship | `01_position.py` → `02_ship_record.py` |
| 15 | Break after saving a working one-ship version | `02_ship_record.py` |
| 16–17 | Apply the structures to a fleet; justify choices | `03_fleet.py` |
| 18 | Optional: distinct target cells with a set | Set section of `data_structures.py` |
| 19–20 | Diagnose access errors; explain the concept | Saved examples and student demonstration |

The small examples are the existing Day 2 `data_structures.py`. They cover tuple, list and dictionary syntax before the game application. Do not turn the set extension into a fourth required game feature.

## Task coverage

| Course task | Runnable file | Student check |
|---|---|---|
| Start with separate values | `00_scalars.py` | Identify x, y and vertical before grouping them |
| Read and replace a coordinate tuple | `01_position.py` | Predict both entries after a move |
| Group fields in a dictionary | `02_ship_record.py` | Update x while y, name and orientation stay unchanged |
| Store and select two records | `03_fleet.py` | Use 1/2 and change each ship independently |
| List indexing, append and length | `data_structures.py` | Explain the first index and the count after append |
| Nested lookup and shared references | `data_structures.py` | Predict which record changes through fleet[0] |
| Choose a structure and explain errors | This guide and slide 19 | Explain tuple, list and dict choices and diagnose an access error |
| Optional unique targets | `data_structures.py` | Explain why duplicate coordinates count once |

## Starting point

Run `python 00_scalars.py` and keep a personal copy for editing. It is the existing Day 2 starter, included locally with its assets. The numbered checkpoints show working results after each representation change. Use them to compare your edits after making a prediction.

## Step 1: a position tuple

Run `python 01_position.py`. Focus on A, B and C; keep the controls supplied.

```python
position = (200, 180)
position = (position[0] + 40, position[1])
print(position)  # (240, 180)
```

Index 0 reads x; index 1 reads y. Tuple entries cannot be replaced. Assign a new tuple when the position changes; `position[0] = 240` would raise `TypeError`.

**Student edits:** change the initial tuple, predict the effect of swapping its entries, and trace one supplied movement update. Explain why `screen.blit(picture, position)` can use the pair directly.

**Acceptance:** the ship still moves and rotates. The student can identify both entries, predict a new position and explain reassignment. Coordinates use pixels and locate the image's top-left corner; Lesson 1's combined reference used a center point.

## Step 2: a ship dictionary

Run `python 02_ship_record.py`. Group the related values in one record:

```python
ship = {'name': 'Scout', 'x': 200, 'y': 180, 'vertical': True}
ship['x'] += 40
position = (ship['x'], ship['y'])
```

The image is `ship_image`; the record is `ship`. Dictionary keys name the fields. `ship['x']` reads a named field, while `position[0]` reads a numbered entry. Build a position tuple from the record when drawing.

**Student edits:** rename the ship, change one starting field, then replace the scalar values in `00_scalars.py` with dictionary access. Use this numbered version as a checkpoint after trying the refactor.

**Acceptance:** the existing controls still work. Changing x leaves y and name unchanged. The student can point to one key lookup, one field update and the tuple passed to `blit`. This is the minimum game outcome for the lesson.

## Step 3: a fleet list

Run `python 03_fleet.py`. This is the existing Day 2 `main.py` reference, included here so the directory runs independently.

```python
fleet = [
    {'name': 'Scout', 'x': 200, 'y': 180, 'vertical': True},
    {'name': 'Cruiser', 'x': 500, 'y': 300, 'vertical': False},
]
ship = fleet[0]
ship['x'] += 40
```

Read nested access from left to right: `fleet[0]` selects a record, then `['x']` selects its field. `ship` refers to that record; it is not a copy. Two ships need two separate dictionaries. With `fleet = [ship, ship]`, both list entries refer to the same record.

**Student edits:** predict both x values after changing one record, then verify the prediction. Change the second ship's initial position. Use the supplied 1/2 selection and drawing loop to demonstrate independent updates. Loop syntax is next lesson's core concept.

**Acceptance:** select and move each ship independently; rotate one without changing the other. Explain why index 0 chooses the first ship and why its fields use string keys. Both rotated images stay inside the window using supplied boundary handling.

## Optional set experiment

Use the final section of `data_structures.py`, matching slide 18:

```python
targets = {(2, 3), (2, 3), (4, 1)}
print(len(targets))       # 2
print((2, 3) in targets)  # True
```

A set stores distinct values without numbered positions. `set()` creates an empty set; `{}` creates an empty dictionary. Do not rely on printed set order. These targets are example grid cells, separate from today's ship pixel coordinates.

## 120-minute schedule

| Minutes | Activity | Evidence |
|---|---|---|
| 0–15 | Define a data structure; compare separate values and a record | Name the values belonging to one ship |
| 15–35 | Tuple, list and dictionary examples, slides 4–9 | Predict an index lookup and a key lookup |
| 35–60 | Fleet examples, nested updates and shared references, slides 10–13 | Predict which record changes; run the small examples |
| 60–75 | Apply a position tuple and one dictionary, slide 14 | Save a working one-ship version |
| 75–85 | Break, slide 15 | Saved source |
| 85–100 | Store two records and justify the structures, slides 16–17 | Demonstrate independent updates |
| 100–110 | Optional set; access-error exercise, slides 18–19 | Explain a duplicate or diagnose one access error |
| 110–120 | Demonstrate and explain, slide 20 | Choose and justify structures for position, ship and fleet |

If students need more practice, keep the one-ship dictionary outcome and skip the set. Do not spend this lesson reteaching arrow keys, rotation, scaling or reset.

## Troubleshooting and exit check

- `KeyError`: check the exact field name; `'X'` differs from `'x'`.
- `IndexError`: a two-ship fleet has indices 0 and 1, with no item at index 2.
- `TypeError` on tuple assignment: create a new tuple instead of replacing an entry.
- Both ships move together: check that the list contains two separate dictionaries.
- Confusing image and data: keep the image named `ship_image` and the record named `ship`.

Each student should define a data structure, justify tuple/dict/list choices, show one lookup and update, and predict which values stay unchanged.

The starting point and all three Pygame steps support the existing teacher check `--smoke`, which renders one frame and exits. Interactive checks still require selecting, moving and rotating the ships.

Sea: [Water+ / ninjikin](https://ninjikin.itch.io/water). Ships: [Sea Warfare set](https://opengameart.org/content/sea-warfare-set-ships-and-more). Keep the original asset credits.

# Day 2: Data structures

Two hours. **One core programming concept: data structures.** Keyboard events and drawing loops are teacher-supplied support; they make changes to your data visible.

## Definition and examples

A **data structure** organizes related values and gives us a way to access and update them. Choose the structure to match what the values mean and how you need to use them.

| Structure | Definition | Game example | Access |
|---|---|---|---|
| tuple | An ordered sequence whose entries cannot be replaced | One position: `(200, 180)` | `position[0]` |
| list | An ordered sequence whose entries can be changed, added or removed | Several ships: `[scout, cruiser]` | `fleet[0]` |
| dict | A mapping from unique keys to values | One ship with named fields | `ship['x']` |
| set (extension) | A collection of distinct values without positional order | Unique attacked cells | `(2, 3) in targets` |

```python
position = (200, 180)
ship = {'name': 'Scout', 'x': 200, 'y': 180, 'vertical': True}
fleet = [ship]
fleet[0]['x'] += 40
print(ship['x'])  # 240: fleet[0] and ship refer to the same dictionary
```

A list answers “which numbered item?” A dictionary answers “which named field?” Indices start at zero. A tuple can group a coordinate pair; create a new tuple when its coordinates change. A dictionary can directly update its x/y fields. Python dictionaries preserve insertion order, but this lesson uses their keys to express meaning, not numbered positions.

## Materials and run commands

[Slides](../../slides/day02.html) · [Teacher guide](../../slides/day02_teacher.md).

With the course Python environment active, enter this folder:

```bash
python data_structures.py  # Predict, then run each section
python starter.py          # Scalar-value starting point, controls supplied
python main.py             # Reference: fleet list containing two ship dictionaries
```

The game uses pixel coordinates today. In later board lessons x/y denote column/row cells. `main.py` uses 1/2 to select a ship, arrows to move and R to rotate; both ships stay inside the window.

## Guided tasks

1. **Predict and inspect.** Run `data_structures.py` one section at a time. Explain the difference between `position[0]`, `names[0]` and `ship['x']`.
2. **Group one ship.** In `starter.py`, replace the separate x, y and vertical values with one dictionary. Use the field names x, y and vertical. Rename the loaded image to `ship_image` so the image and the record have distinct names. Update the supplied controls and drawing to read/write dictionary fields.
3. **Use a position tuple.** Pass `(ship['x'], ship['y'])` to blit. Explain why swapping the two values changes the result.
4. **Store a fleet.** Put two separate ship dictionaries in a list. Use `fleet[0]` and `fleet[1]` to inspect their names and change one x value. The teacher supplies the two-ship drawing and selection loop from `main.py`; trace how it reads the records rather than learning loop syntax today.
5. **Check the result.** Select each ship and move it. Confirm only that ship's record changes. Compare the marked data access in `main.py` after trying your own version.

Minimum: group one ship in a dictionary and explain one lookup and update. Standard: list two distinct records and demonstrate independent changes. Extension: unique targets with a set.

## Predict → run → explain

```python
ship = {'name': 'Scout', 'x': 200, 'y': 180}
fleet = [ship, {'name': 'Cruiser', 'x': 500, 'y': 300}]
fleet[0]['x'] += 40
print(len(fleet))
print(fleet[0]['x'])
print(fleet[1]['x'])
print(ship['x'])
```

Expected output: 2, 240, 500, 240. The first list entry refers to the original ship dictionary. `fleet = [ship, ship]` would refer to the same record twice; create a new dictionary for a different ship.

Extension:

```python
targets = {(2, 3), (2, 3), (4, 1)}
print(len(targets))       # 2
print((2, 3) in targets)  # True
```

A set removes duplicate values. It has no numbered positions. `{}` creates an empty dictionary; `set()` creates an empty set. A set stores these coordinate tuples because they contain hashable integer values.

## Acceptance and explanation

| Check | Expected result |
|---|---|
| First list item | Index 0 selects the first record |
| Named field update | Changing x leaves y and the other ship unchanged |
| Position tuple | First value is x, second is y |
| Two records | Moving one ship does not move the other |
| Bounds and rotation | Supplied controls keep both rotated images inside the window |
| Extension: duplicate target | Repeated tuple appears once in the set |

Exit question: define a data structure, choose structures for a position, one ship and a fleet, and justify each choice with an access example.

Copy the entire folder, including assets. Sea: Water+ / ninjikin; ships: Sea Warfare set. See [course credits](../../README.md#assets).

# Lesson 1: three stages, then combine

The window, asset paths, clock and exit loop are teacher-supplied support. Each stage produces a complete visible result; learn the Python needed for that result.

## Play the completed version first

```bash
python 03_combined.py
```

Play for five minutes: arrows move, R rotates, +/- scales, Space resets. The equals key also enlarges. Ask which numbers control position, angle and size.

## Stage 1: draw a scene

Run `python 01_scene.py` to see the sea and ship.

- Change x and y: assignment, integers, coordinates and tuples.
- Compare load with blit: reading an image versus displaying it.
- Swap the two drawing lines: drawing order and occlusion.
- Comment out the sea drawing, then change background: comments and RGB colors.

Position means the image's top-left corner here. The supplied window setup and loop keep the scene visible.

## Stage 2: transform an image

Run `python 02_transform.py`. The original is on the left and the result on the right.

- Keep angle=0 and change width/height: proportional enlargement versus stretching.
- Fix the size and try angles 0, 90, 180, 45 and -90.
- Specify both size and angle: scale first, then rotate.
- Connect numeric arguments, function calls and returned results stored in variables.

Positive angles rotate anticlockwise, negative clockwise. Width and height must be positive. The original is 20×100; 60×300 is three times larger. Center alignment is supplied for easy comparison.

## Stage 3: combine and control

Run `python 03_combined.py` or `python main.py` in the parent folder. Follow the Combine A–E comments:

1. A: position, angle and scale factor are state the program remembers.
2. B: a key press updates state using if; Space restores defaults.
3. D: each frame scales and rotates the original using current state.
4. E: draw sea, then ship, then refresh.
5. C is optional: check held arrows each frame to preview Day 2 movement.

Keep one window and one loop. Move the core statements instead of pasting three complete programs together. Initialize variables before while; handle key presses inside the event loop; draw outside for but inside while.

The combined version positions the image by its center so rotation and scaling keep the center fixed. Stage 1 uses the top-left corner: explain this change explicitly. Scale ranges from 0.5 to 4.0. Moving off screen is allowed; Space resets. The teacher explains int, min/max and %360 as supporting tools.

## 120-minute schedule

| Time | Activity |
|---|---|
| 0–10 | Play the result: rotation, scaling and movement |
| 10–35 | Stage 1: display, position and layers; change your own scene |
| 35–60 | Stage 2: predict transforms, then compare with the original |
| 60–70 | Break |
| 70–105 | Stage 3: combine core statements and update variables with keys; movement optional |
| 105–120 | Independent change and demonstration; explain the code and visible effect |

Use the [HTML deck](../../../slides/day01.html) and `../python_basics.py` as references when needed. Prioritize a complete scene and repeated practice over memorizing setup code.

## Environment and assets

Python 3.13 + Pygame 2.6.1. Copy the entire increments folder, including assets. All three programs accept the teacher-only `--smoke` option to render one frame and exit.

Sea: Water+ / ninjikin. Ships: Sea Warfare set. See [course credits](../../../README.md#assets).

# Day 1 teacher guide: Data and operations

**One core concept: data and operations.** Data are values a program stores and uses. An operation reads, combines or changes values to produce a result.

Begin with the definition, work through the example in the student lesson, ask for a prediction, then apply it to the game. Treat other syntax as review or supplied support. The exit explanation is: Identify the data, operation and result in x = x + 40. Predict before running.

Use the [incremental experiments](../days/day01/increments/README.md) and their 120-minute schedule by default. Play 03 first, then teach the complete scene in 01, transforms in 02, and combination and controls in 03. The single-file route below remains an alternative; choose slides as needed.

Goal: each student runs a program, displays a ship, changes its coordinates and explains the result. Optional extensions are not required for passing the lesson.

## Before class

1. Prepare Python 3.13, Pygame 2.6.1 and an editor on each machine. Run `python teaching/days/day01/starter.py` to see the sea, then main.py to see the ship.
2. Copy the whole day01 folder, including assets, to each student's workspace. Supply a working starting point rather than asking them to copy initialization code.
3. Open day01.html in a browser. Arrows navigate, N shows notes, O opens the overview, F toggles full screen. Keep the slides folder together for offline use.
4. The game loop, asset paths and initial scaling are supplied support. Leave time for independent editing.

## Alternative single-file schedule

| Time | Activity | Required result |
|---|---|---|
| 0–15 | Show the final game and today's goal; discuss program steps | Each student names an effect they want to make |
| 15–35 | Find files, run the starter, introduce output, variables and coordinates | A sea window on every machine |
| 35–55 | Predict and run short Python experiments | Numbers/text, assignment, tuples, calls, comments, indentation |
| 55–75 | Add a ship to starter.py and change x/y; read the supplied conditions and loop | Each student displays a ship and explains two position changes |
| 75–85 | Break | Save files |
| 85–110 | Change title, add a second ship or explore background colors | One independent change |
| 110–120 | Debug, demonstrate and explain | Identify the edited line and its visible effect |

The deck has 48 slides. Its core teaches data and operations; the final eleven slides are optional syntax and debugging references. Do not give every slide equal time. Use arithmetic and types to explain data and operations. Keep function definitions, for, if/while syntax and input conversion in the optional reference section; only read enough of the supplied loop to run the scene. Use this table for overall timing; individual slide notes are suggested positions, not a second schedule.

## Files and teaching prompts

- `python_basics.py`: use print, numbers/strings, arithmetic and assignment for the core concept. Tuple syntax is preview; conditionals, loops and function definitions are optional references.
- `starter.py`: insert `screen.blit(ship, (x, y))` after the sea drawing and before refresh.
- `main.py`: combined reference for demonstration; students first make their own edits.

Ask why `x = x + 40` works: read the old value, calculate, then assign. Ask where print appears (terminal) and where blit draws (window). If background color changes are invisible, the sea covers it; comment out the sea drawing. Change one value at a time to explain cause and effect. `(200, 180)` locates the top-left corner, not the center. A top-left corner at `(0,0)` does not place the entire ship off screen; its dimensions also matter.

Avoid input inside the game loop and print on every frame. Do not run an unbounded while True experiment without an exit.

## Different starting levels

Minimum: display one ship and explain x/y directions. Standard: change title and position, and fix a spelling or indentation error. Extension: add a ship, explore colors, functions or input. Fast finishers predict a partner's result and exchange explanations while each student edits their own file.

For 3–5 students, allow around a minute each to demonstrate. Assess whether they can run, explain and independently change their program.

## After class

Save each student's starter.py and a screenshot. Continue from their own version next lesson; day02/starter.py is a recovery point. Do not require memorization of the event loop or networking concepts.

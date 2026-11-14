# Battleship Lab: a 20-hour beginner Python course

For a small class of 3–5 students, around age 15. Ten lessons, two hours each. This is the English edition on the `English` branch. Week 1 builds the scene and board; Week 2 completes the rules, computer opponent and multiplayer game.

## Course materials

| Lesson | One core concept | Game application | Materials |
|---|---|---|---|
| 1 | **Data and operations** | Display and transform a ship | [Lesson](days/day01/README.md), [slides](slides/day01.html), [teacher guide](slides/day01_teacher.md) |
| 2 | **Data structures** | Organize and control two ship records | [Lesson](days/day02/README.md), [slides](slides/day02.html), [teacher guide](slides/day02_teacher.md) |
| 3 | **Loops** | Draw the board | [Lesson](days/day03/README.md), [slides](slides/day03.html), [teacher guide](slides/day03_teacher.md) |
| 4 | **Functions** | Validate fleet placement | [Lesson](days/day04/README.md), [slides](slides/day04.html), [teacher guide](slides/day04_teacher.md) |
| 5 | **Conditional branching** | Choose shot feedback | [Lesson](days/day05/README.md), [slides](slides/day05.html), [teacher guide](slides/day05_teacher.md) |
| 6 | **State machines** | Finish a practice game | [Lesson](days/day06/README.md), [slides](slides/day06.html), [teacher guide](slides/day06_teacher.md) |
| 7 | **Algorithms** | Select an untried computer target | [Lesson](days/day07/README.md), [slides](slides/day07.html), [teacher guide](slides/day07_teacher.md) |
| 8 | **Serialization** | Exchange JSON messages | [Lesson](days/day08/README.md), [slides](slides/day08.html), [teacher guide](slides/day08_teacher.md) |
| 9 | **Interfaces** | Play through a shared interface | [Lesson](days/day09/README.md), [slides](slides/day09.html), [teacher guide](slides/day09_teacher.md) |
| 10 | **Testing** | Verify statistics and demonstrate | [Lesson](days/day10/README.md), [slides](slides/day10.html), [teacher guide](slides/day10_teacher.md) |

[Week 2 teaching plan](week02.md) includes preparation, pacing, assessment and an offline fallback. Every lesson has an English HTML deck with a definition, worked example, prediction exercise, application and concept check. The game feature gives the concept a concrete use; other syntax is review or teacher-supplied support.

Open any HTML deck directly in a browser. No network or web server is needed. Keep the whole `slides/` directory together: decks share `theme.css` and `presentation.js`. Day 1's images are embedded. Arrow keys change slides; **N** toggles teacher notes, **O** opens the overview, **F** toggles full screen. Day 1 ends with optional syntax references. Print from the browser for a static copy.

## Setup and completed game

Use Python 3.13 and Pygame 2.6.1. From the repository root:

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --only-binary=:all: -r teaching/requirements.txt
python teaching/refactored/main.py
```

On Windows, activate with `.venv\Scripts\activate` instead. If the environment is already active, only install the requirements and run the game. With `uv`, the equivalent install is `uv pip install --only-binary=:all: -r teaching/requirements.txt`.

The default opponent is the computer; Tkinter is not required. Both boards are visible. Place three ships, with lengths 4, 3 and 2. Click to place, use 1/2/3 to select a ship, and R to rotate. Select an existing ship and click a valid new position to move it. Previewing overlap is allowed, but invalid placement cannot be submitted. Ready locks the fleet. Buttons also randomize or clear the fleet.

Each first hit earns 10 points, each first sinking earns an additional 50, and victory adds 100. Misses and hits both leave markers. A repeat shot costs no turn. Every valid shot ends the turn, including a hit. The highest score is `9 × 10 + 3 × 50 + 100 = 340`. Accuracy is hits divided by valid shots, rounded to a whole percent; with no shots it is 0%.

Placement uses clicks. Continuous dragging can be a later extension once students understand cell rules.

## Multiplayer

Run each command in a separate terminal with the same Python environment active:

```bash
python teaching/refactored/server.py
python teaching/refactored/main.py --connect 127.0.0.1 --name Alice
python teaching/refactored/main.py --connect 127.0.0.1 --name Bob
```

For a LAN game, start the server with `--host 0.0.0.0` and replace the clients' `127.0.0.1` with the server computer's LAN IP. Allow inbound connections through its firewall and use the same port on all computers (default **65432**). Day 8's separate message lab uses **65433** and client option `--host`; Days 9–10 use `--connect`.

The server hosts one room for two players. Both must vote for a rematch; the first player alternates each round. After a disconnect, close and reconnect both clients; the room clears when both players leave. Automatic reconnection and internet room discovery are outside this course.

The server validates fleets, phases, turns, coordinates and repeated shots, and computes sinking, victory and scores. Background I/O keeps the Pygame loop responsive. Newline-delimited JSON handles TCP fragmentation and preserves Unicode and asterisks.

## Code responsibilities

| File | Responsibility |
|---|---|
| `refactored/board.py` | Occupied cells, valid layouts, shot results, statistics |
| `refactored/match.py` | Players, readiness, turns, victory and rematch votes |
| `refactored/main.py` | Pygame drawing, controls and solo mode |
| `refactored/network.py` | Teacher-supplied framing, sending, receiving and background thread |
| `refactored/server.py` | One multiplayer room, connections and match lock |

The repository-root entry points still run the original game. Use the commands above for the teaching edition.

## Independent daily projects

Each directory from `days/day01` to `days/day10` contains its own source and assets. Copy a whole directory to a student; it has no dependency on neighboring days or `refactored/`. Enter that directory and run `python starter.py` for the class starting point or `python main.py` for the reference result. See each day's README for exact edits.

Day 2 applies data structures to the game board. A tuple selects a cell, a dictionary controls ship placement and orientation, and a list organizes the fleet. Sets are an extension. Day 3 returns to a simplified independent scene to focus on loops.

Days 5–6 are shooting practice without an opponent taking turns. Day 7 adds the computer. Day 8 deliberately leaves the graphics behind to make messages visible. Days 9–10 use teacher-supplied networking: students trace requests and change focused pieces of display code. Random fleet placement and two-vote rematches are supplied on Day 9.

Suggested two-hour rhythm: 15 minutes play/review, 20 for the core concept, 40 implementation, 10 break, 25 challenge, 10 demonstration. Explain concepts between short experiments.

## Day 1 routes

- Recommended: [three incremental experiments](days/day01/increments/README.md), beginning with a short play of the combined version.
- Original basic task: `days/day01/starter.py`, initially showing only the sea.
- Combined reference: `days/day01/main.py`, with movement, rotation, scaling and reset.
- Syntax experiments: `days/day01/python_basics.py`, without Pygame; predict before running.
- [HTML slides](slides/day01.html): concepts, coordinate lab, tasks, debugging and notes.
- [Teacher guide](slides/day01_teacher.md): 120-minute schedule and teaching choices.

The browser coordinate lab is a demonstration, not a Python interpreter. Students edit Python in their editor. All course explanations, comments and UI labels are in English.

## Day 2 incremental route

Follow the [Day 2 increments](days/day02/increments/README.md) with the [data structures slides](slides/day02.html). Predict and run the existing terminal examples, then apply a board-cell tuple, one ship dictionary, and a list of two separately placed ships in three runnable checkpoints. The last checkpoint is the existing Day 2 `main.py`. Sets remain optional; controls and drawing are supplied support.

The guide maps the code to slide numbers, includes acceptance checks and follows the deck's 120-minute sequence. Copy the whole `increments/` directory for standalone use, including its local assets and requirements.

## Pre-class checks

```bash
python -m unittest discover -s teaching/tests -v
python teaching/refactored/main.py
```

Check closing the window, rotating and repositioning all ships, rejection of invalid placement, fleet locking, miss markers, repeat shots, sinking and the final score. Then complete a real two-client match, a rematch and a disconnect. Test the LAN on two classroom computers before teaching. Automated rules and local connection checks do not replace that classroom check.

## Assets

The sea comes from the original project's [Water+ by ninjikin](https://ninjikin.itch.io/water); ships come from [Sea Warfare set](https://opengameart.org/content/sea-warfare-set-ships-and-more). Keep these credits. This directory does not relicense the assets. See the repository-root README for the original project.

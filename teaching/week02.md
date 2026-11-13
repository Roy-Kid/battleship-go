# Week 2: from shooting practice to a shared game

Five two-hour lessons, Days 6–10. Students start with a working scene, 10×10 board, placement and shot records from Week 1. By the end, they can play a complete match, trace an action through a server, and present a tested personal edition.

## One programming concept per lesson

| Day | Core concept | Definition and application |
|---|---|---|
| 6 | State machines | Named states and legal transitions; finish after three sinkings |
| 7 | Algorithms | Precise steps that select one untried target |
| 8 | Serialization | Convert structured data to JSON and reconstruct it |
| 9 | Interfaces | Defined operations, inputs and results between client and server |
| 10 | Testing | Compare actual behavior with predicted results, including edge cases |

Use the same sequence every day: definition → small example → prediction → game application → independent explanation. Statistics, timing and display details support the core concept; they are not additional equal-weight learning goals.

## Prepare before the week

Use the course's Python 3.13 environment and pinned Pygame requirements. Copy complete daily folders so students can recover without importing neighboring days. Verify each starter/reference pair. Read [the setup and rules](README.md). Keep the entire slides folder for offline decks; arrows navigate, N shows notes, O opens the overview and F toggles full screen.

Run the rules/protocol checks from the repository root:

```bash
python -m unittest discover -s teaching/tests -v
```

Then play the game manually. Verify a two-client match, both rematch votes, a disconnect, and a connection between the actual classroom computers. Reserve three terminals and distinct player names. The message lab uses 65433; the game uses 65432. Prepare a local two-client fallback for unavailable LAN access.

## Daily progression

| Day | Student contribution | Teacher provides | Evidence |
|---|---|---|---|
| [6](days/day06/README.md) | Victory phase and statistics display | Verified fire/statistics functions | Fixed-fleet calculation; win stays at 340 |
| [7](days/day07/README.md) | Turn guard, deadline, computer response and incoming markers | Drawing code and candidate-list support | A repeat shot does not trigger the computer |
| [8](days/day08/README.md) | Modify name/text messages and explain their route | Server, JSON framing, sockets and threads | Two terminals exchange exact Unicode text |
| [9](days/day09/README.md) | Trace ready/attack/rematch; change one status label | Integrated network game | Match, two-vote rematch and disconnect |
| [10](days/day10/README.md) | Render snapshot statistics and latest three reports | Existing rules and Day 9 starting point | Partner checklist and two-minute demo |

Each day has a student lesson, HTML deck and teacher guide linked from [the course index](README.md#course-materials). Starter progression is deliberate: Day 6 starts from Day 5; Day 7 from Day 6; Day 8 is a separate terminal lab; Day 9 starts with Day 7 solo code and transitions to a supplied integration; Day 10 starts from Day 9's integrated game.

## Rhythm and scope

Use 15 minutes for recap/play, 20 for a new idea, 40 for implementation, 10 for a break, 25 for a challenge and checking, and 10 for explanation. Teacher guides give exact 120-minute plans. In a class of five, split Day 10's final ten minutes into two minutes each; setup and file saving happen beforehand.

Students work on a focused change before comparing with the reference. Give the minimum task first and keep extensions optional. Pair a driver with a navigator, swap midway, and ensure everyone can explain and save their own version. A third learner can record checks and rotate into coding.

Keep low-level threading, locking, TCP framing and socket lifecycle teacher supplied. Explain their purpose when needed to understand the program. The learning target is to connect data, rules and visible behavior.

## Shared vocabulary

| Term | Meaning in this project |
|---|---|
| fleet | Three ships, each storing name, starting x/y and orientation |
| shots | Your valid attacks on the opponent, keyed by "x,y" |
| incoming | The opponent's valid attacks on your fleet |
| phase | placement, battle or finished; multiplayer also has lobby/disconnected |
| request | An action the client asks the server to perform |
| snapshot | The server's current view for one player |
| hit / sunk | A hit damages a ship; sunk is its final hit and also counts as a hit |
| accuracy | Hits / valid shots × 100, rounded; 0% before any shots |

Valid hits and misses both end the turn. A duplicate or invalid action changes neither the board nor the turn. Base score is hits×10 + sunk×50. Victory adds 100 once, producing 340 after all nine occupied cells are hit. The client displays server statistics in the integrated version.

## Record learning and verify the result

For each day collect a working source file, one screenshot or terminal transcript, an expected/actual check and an independent explanation. Use this short record during partner review:

| Check / action | Expected result | Actual result | Pass or next change |
|---|---|---|---|
| Example: fire at the same cell twice | Shot count stays the same | Student records observation | Student records decision |

Assess working behavior, reasoning and independent editing. A student meets the minimum with guidance and one correct explanation; the standard is completing the task and its acceptance list independently. Extra decoration does not replace correct rules.

Final demonstration: introduce the game, show a personal change, explain one rule, and show one bug and its fix. Partner checks cover placement, turn changes, repeat targets, victory, statistics, reports, rematch and disconnect. Keep a list of checks still pending on classroom hardware.

## Fallbacks

If a learner's file breaks, use that day's complete starter directory and reapply one change. If the LAN fails, use one server and two clients on one computer. If all networking is unavailable, trace dictionaries on paper on Day 8 and use integrated solo mode on Days 9–10; schedule the actual peer connection later and label it unverified.

# Day 7 teacher guide: Algorithms

**One core concept: algorithms.** An algorithm is a precise sequence of steps for solving a problem. Its inputs and rules determine the permitted outputs.

Begin with the definition, work through the example in the student lesson, ask for a prediction, then apply it to the game. Treat other syntax as review or supplied support. The exit explanation is: Explain the select-untried-target algorithm as input, steps and output. Why can it never repeat a recorded target?

Audience: beginner students around age 15, 3–5 learners. Duration: 120 minutes. [Student lesson](../days/day07/README.md) · [Slide deck](day07.html) · [Week 2 plan](../week02.md).

## Learning outcome

Alternate valid shots with a computer that chooses an untried cell. Assess the student's explanation as well as the working result.

## Before class

Copy the whole day07 directory, including assets. Run the starter and reference in the prepared Python 3.13/Pygame 2.6.1 environment. Open the deck offline; N shows notes, O opens the overview. Check the student tasks against the supplied code before distributing it.

The completed Day 6 game, including score and victory, is provided in starter.py.

Keep drawing and board.py. The teacher supplies the candidate-list comprehension and explains its meaning. Use pygame.time.get_ticks for the 600 ms delay; the game loop must keep processing events.

## 120-minute lesson

| Minutes | Activity | Evidence |
|---|---|---|
| 0–15 | Replay Day 6 and identify missing opponent behavior | Baseline win and score |
| 15–35 | Trace two turns on paper | Correct shots/incoming distinction |
| 35–75 | Add turn guard, deadline and computer attack | One player/computer exchange |
| 75–85 | Break | Save |
| 85–110 | Check duplicates, timing and both outcomes | Partner records results |
| 110–120 | Demonstrate turn control | Explain one guard and one state update |

Use the deck for short explanations, then return to the editor. Notes on every slide provide prompts and expected answers. If time runs short, finish the core changes and acceptance checks before the optional challenge.

## Demonstration and answer key

The enemy chooses cells on your board, so incoming is its history. After n distinct incoming shots there are 100−n candidates. The 600 ms deadline delays the action while the main loop keeps handling input and drawing.

Have students predict before you run the guided experiment in the student lesson. Ask them to point to the responsible line rather than only describe the screen.

## Common difficulties

If the computer fires every frame, check the my_turn update. If nothing happens until the mouse moves, the computer block is nested inside the event loop. If an incoming marker is hidden, draw it after the ship. Keep the phase guard so no response occurs after a winning shot.

## Assessment and support

Minimum: run the supplied code, make the core edit with guidance, and explain one input/output example. Standard: complete the core task independently and verify the acceptance list. Extension: finish the optional challenge and help a partner diagnose a problem through questions.

For pairs, use driver and navigator roles and swap halfway through the implementation block. Each learner saves their own result. With an odd number, the third student records predictions and checks, then rotates roles.

Exit question: Why does the computer choose from incoming rather than shots? Why is the deadline check outside the event loop?

Save the working source, a screenshot or terminal transcript, and one expected/actual check. Use these for the next lesson's recap.

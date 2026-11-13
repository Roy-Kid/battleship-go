# Day 6 teacher guide: State machines

**One core concept: state machines.** A state machine represents a program as named states and transitions. An event changes state only when its transition rule allows it.

Begin with the definition, work through the example in the student lesson, ask for a prediction, then apply it to the game. Treat other syntax as review or supplied support. The exit explanation is: Name the states before and after victory, the event that triggers the transition, and an action forbidden after it.

Audience: beginner students around age 15, 3–5 learners. Duration: 120 minutes. [Student lesson](../days/day06/README.md) · [Slide deck](day06.html) · [Week 2 plan](../week02.md).

## Learning outcome

Finish a shooting practice game with sinking, victory, score and accuracy. Assess the student's explanation as well as the working result.

## Before class

Copy the whole day06 directory, including assets. Run the starter and reference in the prepared Python 3.13/Pygame 2.6.1 environment. Open the deck offline; N shows notes, O opens the overview. Check the student tasks against the supplied code before distributing it.

The Day 5 shooting practice: ships can be placed and targets can be fired on, but no final score or win state is shown.

The local board.py already provides fire and statistics. Read and call them directly. This lesson still has no computer turn and no networking.

## 120-minute lesson

| Minutes | Activity | Evidence |
|---|---|---|
| 0–15 | Review hits, misses and duplicate targets | A working Day 5 baseline |
| 15–35 | Trace fire and predict statistics | Hand-calculated score and accuracy |
| 35–75 | Add finished phase and statistics display | One full practice game |
| 75–85 | Break | Save working code |
| 85–110 | Run the fixed-fleet experiment and partner checks | Evidence for each acceptance case |
| 110–120 | Demonstrate and explain the bonus | One code-based explanation per student |

Use the deck for short explanations, then return to the editor. Notes on every slide provide prompts and expected answers. If time runs short, finish the core changes and acceptance checks before the optional challenge.

## Demonstration and answer key

A Carrier gives 4×10+50=90. The whole fleet gives 9×10+3×50=240 before the 100-point victory bonus. Any number of misses leaves the final score at 340 but lowers accuracy.

Have students predict before you run the guided experiment in the student lesson. Ask them to point to the responsible line rather than only describe the screen.

## Common difficulties

If score increases every frame, the student is accumulating a display value: derive it from statistics and phase. If sinking is counted twice, check that sunk is one recorded result, not a second shot. If accuracy crashes on an empty dictionary, use the supplied statistics function.

## Assessment and support

Minimum: run the supplied code, make the core edit with guidance, and explain one input/output example. Standard: complete the core task independently and verify the acceptance list. Extension: finish the optional challenge and help a partner diagnose a problem through questions.

For pairs, use driver and navigator roles and swap halfway through the implementation block. Each learner saves their own result. With an odd number, the third student records predictions and checks, then rotates roles.

Exit question: Explain how a sunk result differs from a hit, and why the victory bonus stays 100 even after many frames.

Save the working source, a screenshot or terminal transcript, and one expected/actual check. Use these for the next lesson's recap.

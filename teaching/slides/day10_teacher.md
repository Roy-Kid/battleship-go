# Day 10 teacher guide: Testing

**One core concept: testing.** A test compares observed behavior with an expected result for a chosen input or action.

Begin with the definition, work through the example in the student lesson, ask for a prediction, then apply it to the game. Treat other syntax as review or supplied support. The exit explanation is: Choose a normal case and an edge case, predict each result, then record actual behavior and decide whether it passes.

Audience: beginner students around age 15, 3–5 learners. Duration: 120 minutes. [Student lesson](../days/day10/README.md) · [Slide deck](day10.html) · [Week 2 plan](../week02.md).

## Learning outcome

Add a statistics line and three recent battle reports, then demonstrate a verified personal edition. Assess the student's explanation as well as the working result.

## Before class

Copy the whole day10 directory, including assets. Run the starter and reference in the prepared Python 3.13/Pygame 2.6.1 environment. Open the deck offline; N shows notes, O opens the overview. Check the student tasks against the supplied code before distributing it.

starter.py is the Day 9 integrated game with a statistics placeholder and one recent report. Edit it directly. main.py is the finished reference, equivalent to the refactored edition.

Reuse the validated rules and the server snapshot. The me dictionary already contains score, hits, shots and accuracy; avoid a second scoring formula in the client.

## 120-minute lesson

| Minutes | Activity | Evidence |
|---|---|---|
| 0–15 | Set the final demonstration goal | Choose one personal change |
| 15–35 | Read snapshot statistics and slices | Predict empty and short logs |
| 35–75 | Add statistics and reports, then personalize | A working student edition |
| 75–85 | Break | Save |
| 85–110 | Partner regression check and fixes | Record expected/actual behavior |
| 110–120 | Two-minute demonstrations | Show change, rule and fix |

Use the deck for short explanations, then return to the editor. Notes on every slide provide prompts and expected answers. If time runs short, finish the core changes and acceptance checks before the optional challenge.

## Demonstration and answer key

Match.view computes the win bonus once as a derived value. The client renders me fields unchanged. A slice does not fail on an empty list; the guarded loop draws no reports during editable placement.

Have students predict before you run the guided experiment in the student lesson. Ask them to point to the responsible line rather than only describe the screen.

## Common difficulties

If the final score is 440, the UI added a second victory bonus. If reports collide with buttons, keep the not-editable guard. If old reports survive a rematch, check that they come from the current snapshot rather than a second local history.

## Assessment and support

Minimum: run the supplied code, make the core edit with guidance, and explain one input/output example. Standard: complete the core task independently and verify the acceptance list. Extension: finish the optional challenge and help a partner diagnose a problem through questions.

For pairs, use driver and navigator roles and swap halfway through the implementation block. Each learner saves their own result. With an odd number, the third student records predictions and checks, then rotates roles.

Exit question: Which snapshot fields did you display, and which check gives evidence that your change works?

Save the working source, a screenshot or terminal transcript, and one expected/actual check. Use these for the next lesson's recap.

## Connection preparation and fallback

Test local connections first, then two classroom computers. Day 8 uses port 65433 and client --host; Days 9–10 use 65432 and --connect. Keep a server plus two clients on one computer as the LAN fallback. If networking is unavailable altogether, use the message trace on paper for Day 8 or integrated solo mode for Days 9–10. Record that a real peer match is still pending; a paper trace or solo game does not establish LAN success.

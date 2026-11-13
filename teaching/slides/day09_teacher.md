# Day 9 teacher guide: Interfaces

**One core concept: interfaces.** An interface specifies how one part of a program asks another part to do something: the available operations, required inputs and promised results.

Begin with the definition, work through the example in the student lesson, ask for a prediction, then apply it to the game. Treat other syntax as review or supplied support. The exit explanation is: State the inputs, precondition and response for an attack request. Why must clients keep the field names unchanged?

Audience: beginner students around age 15, 3–5 learners. Duration: 120 minutes. [Student lesson](../days/day09/README.md) · [Slide deck](day09.html) · [Week 2 plan](../week02.md).

## Learning outcome

Complete a two-player game and trace a click through the server to both clients. Assess the student's explanation as well as the working result.

## Before class

Copy the whole day09 directory, including assets. Run the starter and reference in the prepared Python 3.13/Pygame 2.6.1 environment. Open the deck offline; N shows notes, O opens the overview. Check the student tasks against the supplied code before distributing it.

starter.py is the Day 7 solo game. It does not accept --connect. main.py is the teacher-supplied integrated version; begin by comparing the two, then edit a personal copy of main.py.

main.py, match.py, network.py and server.py form the integration scaffold. Students read submit calls and state displays; they are not expected to implement the transport or rewrite the entire game.

## 120-minute lesson

| Minutes | Activity | Evidence |
|---|---|---|
| 0–15 | Compare solo starter with integrated main | Identify familiar behavior |
| 15–35 | Teacher traces request → Match → snapshot | Annotate one request |
| 35–75 | Connect two clients, ready and play | A synchronized battle |
| 75–85 | Break | Keep a saved working file |
| 85–110 | Change one label; check rematch and disconnect | Partner completes the acceptance list |
| 110–120 | Explain one server decision | Show the corresponding code path |

Use the deck for short explanations, then return to the editor. Notes on every slide provide prompts and expected answers. If time runs short, finish the core changes and acceptance checks before the optional challenge.

## Demonstration and answer key

The client expresses intent; the server owns the opponent fleet and checks phase, turn, coordinates and history. A snapshot is a player-specific view, not the entire Match object.

Have students predict before you run the guided experiment in the student lesson. Ask them to point to the responsible line rather than only describe the screen.

## Common difficulties

Do not pass --connect to starter.py; it is the standalone Day 7 baseline. If a room is full after testing a disconnect, close both clients so it clears. If an attack seems delayed, wait for a snapshot; changing local state would create two authorities. Teacher demonstration can accelerate a full match by targeting a known test fleet.

## Assessment and support

Minimum: run the supplied code, make the core edit with guidance, and explain one input/output example. Standard: complete the core task independently and verify the acceptance list. Extension: finish the optional challenge and help a partner diagnose a problem through questions.

For pairs, use driver and navigator roles and swap halfway through the implementation block. Each learner saves their own result. With an odd number, the third student records predictions and checks, then rotates roles.

Exit question: Why does the client send an attack request instead of announcing a hit? Name one rule the server checks.

Save the working source, a screenshot or terminal transcript, and one expected/actual check. Use these for the next lesson's recap.

## Connection preparation and fallback

Test local connections first, then two classroom computers. Day 8 uses port 65433 and client --host; Days 9–10 use 65432 and --connect. Keep a server plus two clients on one computer as the LAN fallback. If networking is unavailable altogether, use the message trace on paper for Day 8 or integrated solo mode for Days 9–10. Record that a real peer match is still pending; a paper trace or solo game does not establish LAN success.

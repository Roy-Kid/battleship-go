# Day 8 teacher guide: Serialization

**One core concept: serialization.** Serialization converts structured data into a representation that can be stored or transmitted. Deserialization reconstructs the data from that representation.

Begin with the definition, work through the example in the student lesson, ask for a prediction, then apply it to the game. Treat other syntax as review or supplied support. The exit explanation is: Distinguish a Python dictionary, JSON text and encoded bytes. Which step reconstructs the dictionary?

Audience: beginner students around age 15, 3–5 learners. Duration: 120 minutes. [Student lesson](../days/day08/README.md) · [Slide deck](day08.html) · [Week 2 plan](../week02.md).

## Learning outcome

Send named messages between two terminals, then try two classroom computers. Assess the student's explanation as well as the working result.

## Before class

Copy the whole day08 directory, including assets. Run the starter and reference in the prepared Python 3.13/Pygame 2.6.1 environment. Open the deck offline; N shows notes, O opens the overview. Check the student tasks against the supplied code before distributing it.

This is a separate terminal experiment. starter.py already includes connection and receiver support; it does not open a Pygame window.

server.py, network.py, sockets, threads, locking and newline framing are teacher supplied. Students edit the message dictionary and printed text. Keep the name/text schema intact.

## 120-minute lesson

| Minutes | Activity | Evidence |
|---|---|---|
| 0–15 | Trace sender → server → receivers | Predict who sees a broadcast |
| 15–35 | Run three terminals locally | Two clients exchanging messages |
| 35–75 | Edit text, inspect dictionary/JSON and test Unicode | Saved before/after message |
| 75–85 | Break | Leave clients or save notes |
| 85–110 | Teacher-guided LAN connection or local fallback | A partner receives a coordinate report |
| 110–120 | Explain fields and close clients | One message traced by each student |

Use the deck for short explanations, then return to the editor. Notes on every slide provide prompts and expected answers. If time runs short, finish the core changes and acceptance checks before the optional challenge.

## Demonstration and answer key

The broadcast goes to all current members, including its sender. A coordinate inside text has no game meaning yet. The newline is framing for the supplied protocol; packet boundaries are not message boundaries.

Have students predict before you run the guided experiment in the student lesson. Ask them to point to the responsible line rather than only describe the screen.

## Common difficulties

Connection refused usually means no server is listening at that address/port. A timeout on the LAN calls for address and firewall checks. Students often run terminal commands inside Python files or forget which file they edited. Keep the local three-terminal fallback ready.

## Assessment and support

Minimum: run the supplied code, make the core edit with guidance, and explain one input/output example. Standard: complete the core task independently and verify the acceptance list. Extension: finish the optional challenge and help a partner diagnose a problem through questions.

For pairs, use driver and navigator roles and swap halfway through the implementation block. Each learner saves their own result. With an odd number, the third student records predictions and checks, then rotates roles.

Exit question: Point to the message dictionary and explain the roles of name, text, server address and port.

Save the working source, a screenshot or terminal transcript, and one expected/actual check. Use these for the next lesson's recap.

## Connection preparation and fallback

Test local connections first, then two classroom computers. Day 8 uses port 65433 and client --host; Days 9–10 use 65432 and --connect. Keep a server plus two clients on one computer as the LAN fallback. If networking is unavailable altogether, use the message trace on paper for Day 8 or integrated solo mode for Days 9–10. Record that a real peer match is still pending; a paper trace or solo game does not establish LAN success.

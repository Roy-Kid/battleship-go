# Day 9: Interfaces

Two hours. Core programming concept: **interfaces**. Other syntax is review or teacher-supplied support.

**Goal:** Complete a two-player game and trace a click through the server to both clients.

Materials: [slides](../../slides/day09.html), [teacher guide](../../slides/day09_teacher.md), [Week 2 plan](../../week02.md).

## Core concept: interfaces

**Definition:** An interface specifies how one part of a program asks another part to do something: the available operations, required inputs and promised results.

**Example:**

```python
# In the integrated game:
connection.submit('attack', x=3, y=4)
# The request asks for an attack. It does not promise a hit.
# The next snapshot supplies the result.
```

**Explain it:** State the inputs, precondition and response for an attack request. Why must clients keep the field names unchanged?

The game feature is an application of this concept. Assess whether you can explain and use the concept, as well as run the game.

## Start here

Enter this directory with Python 3.13 and the course requirements installed:

```bash
python starter.py  # Start in solo mode. See multiplayer commands below.
```

starter.py is the Day 7 solo game. It does not accept --connect. main.py is the teacher-supplied integrated version; begin by comparing the two, then edit a personal copy of main.py.

## Student tasks

1. Run `python starter.py` to identify the familiar solo behavior. Close it. Run `python main.py` to see the same rules through the integrated solo interface.
2. Launch one server and two copies of `main.py` using the commands below. Choose Random fleet, then Ready in both windows. Identify the active turn.
3. Find the three `connection.submit` calls for ready, attack and rematch. Record their fields. An attack sends x/y, not a hit result or a new score.
4. Trace `server.py` calling `Match.attack`, then `Match.view`. Find how the returned state drives `state['my_turn']`, `state['shots']` and the phase status text.
5. Make one focused UI edit in your personal copy of main.py, such as changing the waiting or turn label. Keep action names and snapshot keys unchanged. Restart to verify the edit.
6. Complete a match, try a one-vote rematch, then vote from both clients. Finally close one client and observe the disconnect message on the other.

## Guided experiment and reference

Run each line in a separate terminal from this directory:

```bash
python server.py
python main.py --connect 127.0.0.1 --name Alice
python main.py --connect 127.0.0.1 --name Bob
```

For the LAN: server `--host 0.0.0.0`, clients `--connect SERVER_LAN_IP`; port **65432**. Use distinct names of 1–16 characters. There is one room with two places.

| Request | Fields supplied by the UI | Server decision |
|---|---|---|
| ready | fleet | Validate and lock all three ships; start when both are ready |
| attack | x, y | Check phase, turn, bounds and duplicate; resolve result |
| rematch | none | Record one vote; reset only after both agree |

`Connection.submit` adds the `action` field. `Connection` handles join and state polling. A snapshot includes your fleet, your shots and incoming shots. Its enemy summary intentionally omits the enemy fleet. Wins persist across a rematch; fleets and shots reset, and the opening player alternates.

## Acceptance checks

| Case | Expected result |
|---|---|
| Ready lock | A player who is ready cannot reposition ships. |
| Turn and repeat | Out-of-turn or repeated attacks cannot change records or consume another turn. |
| Hidden information | The enemy summary contains no fleet coordinates. |
| Rematch | One vote keeps the finished game; two start a fresh placement phase. |
| Disconnect | Remaining client reports departure; close both before reconnecting. |

Predict before running. Record expected and actual behavior, then explain any difference. Keep a working copy after each step.

## Challenge and exit question

Use two classroom computers. Ask a partner to predict the snapshot after a miss, then check the board and turn display.

Exit question: Why does the client send an attack request instead of announcing a hit? Name one rule the server checks.

## Teacher supplied

main.py, match.py, network.py and server.py form the integration scaffold. Students read submit calls and state displays; they are not expected to implement the transport or rewrite the entire game.

This directory contains independent code and assets. Copy the whole folder. Sea: Water+ / ninjikin; ships: Sea Warfare set. See [course credits](../../README.md#assets).

# Day 8: Serialization

Two hours. Core programming concept: **serialization**. Other syntax is review or teacher-supplied support.

**Goal:** Send named messages between two terminals, then try two classroom computers.

Materials: [slides](../../slides/day08.html), [teacher guide](../../slides/day08_teacher.md), [Week 2 plan](../../week02.md).

## Core concept: serialization

**Definition:** Serialization converts structured data into a representation that can be stored or transmitted. Deserialization reconstructs the data from that representation.

**Example:**

```python
import json
message = {'name': 'Alice', 'text': 'Ahoy!'}
wire_text = json.dumps(message)
restored = json.loads(wire_text)
print(restored == message)  # True
```

**Explain it:** Distinguish a Python dictionary, JSON text and encoded bytes. Which step reconstructs the dictionary?

The game feature is an application of this concept. Assess whether you can explain and use the concept, as well as run the game.

## Start here

Enter this directory with Python 3.13 and the course requirements installed:

```bash
python starter.py --name Alice  # Start the server first; see below.
```

This is a separate terminal experiment. starter.py already includes connection and receiver support; it does not open a Pygame window.

## Serialization experiment

Predict, then run this in a separate practice file before opening the network clients:

```python
import json
message = {'name': 'Alice', 'text': 'Ahoy, Båt! *'}
payload = json.dumps(message, ensure_ascii=False)
wire = payload.encode('utf-8')
restored = json.loads(wire.decode('utf-8'))
print(type(payload).__name__, type(wire).__name__)
print(restored == message)
```

Expected output: `str bytes`, then `True`. Identify serialization/deserialization and encoding/decoding separately. The supplied network helper also appends a newline so the receiver can find message boundaries.

## Student tasks

1. Use the three-terminal commands below. Send a message from Alice and confirm that both terminals show it (the sender also receives the broadcast).
2. In `starter.py`, find `message = {'name': args.name, 'text': text}`. Change the value of text to `'Captain says: ' + text`. Restart that client and observe the prefix.
3. Compare the Python dictionary with its JSON representation: Python uses single or double quotes for strings; JSON object keys and strings use double quotes. The supplied code converts between them.
4. Send accented text such as `Ahoy, Båt! *`, an empty message, and a coordinate as text such as `x=3, y=4`. Explain why text is still a string, not an attack action.
5. Restore a plain text value, then connect across the LAN with the teacher. Use `/quit` to leave each client and Ctrl+C to stop the server.

## Guided experiment and reference

Run each command in its own terminal, from this directory:

```bash
# Terminal 1
python server.py
# Terminal 2
python starter.py --name Alice
# Terminal 3
python starter.py --name Bob
```

`main.py` is the reference client and accepts the same options. Both names and message text are strings. The server limits names to 16 characters and text to 200 characters.

For the LAN, the teacher runs `python server.py --host 0.0.0.0`. Each client uses `python starter.py --host SERVER_LAN_IP --name Alice` (replace the placeholder and use a different name on the other client). Port **65433** must match, and the server firewall must allow it. `127.0.0.1` always means the computer running that command; `0.0.0.0` is a server bind address, not a client destination.

Wire example, including its terminating newline:

```text
{"name": "Alice", "text": "x=3, y=4"}

```

A TCP read may contain part of a message or several messages. The supplied reader uses the newline to find one complete JSON object.

## Acceptance checks

| Case | Expected result |
|---|---|
| Two clients | Each receives the other client’s name and exact text. |
| Edited message | The prefix appears once, after restarting the edited file. |
| Unicode and asterisk | Accents and * arrive unchanged. |
| Schema | Keep name/text as strings; extra fields are not forwarded by this server. |
| Connection failure | Read the terminal error; check server, address and 65433 before changing code. |

Predict before running. Record expected and actual behavior, then explain any difference. Keep a working copy after each step.

## Challenge and exit question

Format the typed text as a coordinate report, keeping the name/text schema. Explain why adding a field only on the sender does not make a new protocol.

Exit question: Point to the message dictionary and explain the roles of name, text, server address and port.

## Teacher supplied

server.py, network.py, sockets, threads, locking and newline framing are teacher supplied. Students edit the message dictionary and printed text. Keep the name/text schema intact.

This directory contains independent code and assets. Copy the whole folder. Sea: Water+ / ninjikin; ships: Sea Warfare set. See [course credits](../../README.md#assets).

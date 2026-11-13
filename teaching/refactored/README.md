# Completed teaching edition

Python 3.13 + Pygame 2.6.1; no Tkinter dependency. Enter this directory and run `python main.py` to play the computer.

For multiplayer, run `python server.py` in one terminal, then `python main.py --connect 127.0.0.1 --name Alice` and `python main.py --connect 127.0.0.1 --name Bob` in separate terminals.

Click the left board to place ships; 1/2/3 selects a ship and R rotates it. Random fleet, Clear and Ready buttons are below the boards. Ready locks your layout. On your turn, click the right board to attack. Both players must confirm a rematch. Esc exits.

See [the course guide](../README.md) for complete rules, asset credits, LAN setup and pre-class checks.

# Battleship Go

## 中文教学版

新增的零基础 Python 教学重构版、10 天独立代码和第一天 HTML 课件见 [teaching/README.md](teaching/README.md)。启动教学完成版：`python teaching/refactored/main.py`。以下内容为原版说明。

Battleship Go is a multiplayer battleship game made in Python using Pygame. Multiplayer uses sockets for connection under the Client-Server architecture.

![battle](https://user-images.githubusercontent.com/23248296/166291602-75f04685-2665-4e9f-ac6c-f685a8523fe9.PNG)

## Stages

This project was made using a simple state machine logic and it is represented as stages. The stages are:

 - Lobby: Connect to game server and waits untils all players are ready.
 - Ship lock: Move and rotate your ships before battle starts.
 - Battle: Guess where the enemy's ships are and sink them all.
 - Game finished: Shows who is the winner and start a new game.

## GUI

This project does not uses any third-party library, every GUI item was hand-crafted.

## Sprites

Sprites used in this project are not my authorship. There were found on internet, credits are shown below:

 - [Water+](https://ninjikin.itch.io/water): Map was created using these assets.
 - [Sea Warfare set](https://opengameart.org/content/sea-warfare-set-ships-and-more)

## How to run it
This project uses Client-Server architecture for multiplayer. So, Game server and clients have to be started to play the game.
### Game server
To run game server, run the following command and then click on button **Start**

    python game_server.py

![game server](https://user-images.githubusercontent.com/23248296/166291634-b5f7d4b0-e65b-458c-8685-352dcc3df824.PNG)

### Client
To run client, run the following command:

    python main.py

![lobby](https://user-images.githubusercontent.com/23248296/166291502-a8964bc7-5138-4bde-a7bc-ad30a4cd45dd.PNG)
# battleship-go
# battleship-go

"""Day 10 starting point: display snapshot statistics and three recent reports.
Play the computer, or use --connect IP --name Alice.
"""
import argparse
import os
from pathlib import Path
import random
import time
import pygame
from board import SIZE, LENGTHS, cells, can_place, random_fleet
from match import Match
from network import Connection

ROOT = Path(__file__).resolve().parent
CELL = 36
LEFT, RIGHT, TOP = 60, 560, 145
WIDTH, HEIGHT = 1000, 700
SEA, INK, GOLD = (18, 52, 72), (229, 242, 239), (250, 195, 88)


class Solo:
    """Use the same UI interface as Connection, with rules provided directly by Match."""
    def __init__(self, name):
        self.match = Match()
        self.match.join('you', name)
        self.match.join('cpu', 'Computer')
        self.match.ready('cpu', random_fleet())
        self.error, self.fatal = '', False
        self.due = 0

    @property
    def state(self):
        return self.match.view('you')

    def submit(self, action, **data):
        try:
            if action == 'ready':
                self.match.ready('you', data['fleet'])
            elif action == 'attack':
                self.match.attack('you', data['x'], data['y'])
            elif action == 'rematch':
                self.match.rematch('you')
                self.match.rematch('cpu')
                self.match.ready('cpu', random_fleet())
            self.error = ''
        except ValueError as exc:
            self.error = str(exc)

    def tick(self):
        if self.match.phase == 'battle' and self.match.turn == 'cpu':
            if not self.due:
                self.due = time.monotonic() + 0.55
            if time.monotonic() >= self.due:
                shots = self.match.players['cpu']['shots']
                choices = [(x, y) for x in range(SIZE) for y in range(SIZE) if f'{x},{y}' not in shots]
                self.match.attack('cpu', *random.choice(choices))
                self.due = 0
        else:
            self.due = 0

    def close(self):
        pass


def run():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--connect', metavar='HOST')
    parser.add_argument('--port', type=int, default=65432)
    parser.add_argument('--name', default='Captain')
    parser.add_argument('--smoke', action='store_true', help='render one frame and exit')
    args = parser.parse_args()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Battleship Lab — teaching edition')
    font = pygame.font.Font(str(ROOT / 'assets/font.ttf'), 18)
    small = pygame.font.Font(str(ROOT / 'assets/font.ttf'), 14)
    title = pygame.font.Font(str(ROOT / 'assets/font.ttf'), 28)
    ship_image = pygame.image.load(str(ROOT / 'assets/ship.png')).convert_alpha()
    water = pygame.image.load(str(ROOT / 'assets/sea.png')).convert()
    water = pygame.transform.scale(water, (360, 360))
    clock = pygame.time.Clock()
    connection = Connection(args.connect, args.port, args.name) if args.connect else Solo(args.name)
    fleet, selected, vertical = [], 'Carrier', False
    seen_round = 1
    notice, notice_until = '', 0
    sent_ready, sent_rematch = False, False
    buttons = {'random': pygame.Rect(60, 550, 165, 40),
               'clear': pygame.Rect(240, 550, 165, 40),
               'ready': pygame.Rect(560, 550, 180, 40),
               'rematch': pygame.Rect(560, 550, 250, 40)}

    def text(value, x, y, color=INK, face=font):
        screen.blit(face.render(str(value), True, color), (x, y))

    def board(origin, shots):
        screen.blit(water, (origin, TOP))
        shade = pygame.Surface((360, 360), pygame.SRCALPHA)
        shade.fill((4, 24, 38, 135))
        screen.blit(shade, (origin, TOP))
        for i in range(SIZE):
            text(chr(65+i), origin+i*CELL+12, TOP-25, face=small)
            text(i+1, origin-27, TOP+i*CELL+10, face=small)
        for i in range(SIZE+1):
            pygame.draw.line(screen, (71, 113, 129), (origin+i*CELL, TOP), (origin+i*CELL, TOP+360))
            pygame.draw.line(screen, (71, 113, 129), (origin, TOP+i*CELL), (origin+360, TOP+i*CELL))
        for key, shot in shots.items():
            x, y = map(int, key.split(','))
            center = (origin+x*CELL+18, TOP+y*CELL+18)
            color = (244, 104, 88) if shot['kind'] != 'miss' else (175, 208, 219)
            pygame.draw.circle(screen, color, center, 9 if shot['kind'] != 'miss' else 4)
            if shot['kind'] != 'miss':
                pygame.draw.line(screen, INK, (center[0]-4,center[1]-4),(center[0]+4,center[1]+4),2)
                pygame.draw.line(screen, INK, (center[0]+4,center[1]-4),(center[0]-4,center[1]+4),2)

    def draw_ship(ship):
        length = LENGTHS[ship['name']]
        image = pygame.transform.scale(ship_image, (CELL-8, CELL*length-8))
        if not ship['vertical']:
            image = pygame.transform.rotate(image, 90)
        screen.blit(image, (LEFT+ship['x']*CELL+4, TOP+ship['y']*CELL+4))

    running = True
    try:
        while running:
            clock.tick(30)
            if isinstance(connection, Solo):
                connection.tick()
            state = connection.state
            if state and state['round'] != seen_round:
                seen_round = state['round']
                fleet, selected, sent_ready, sent_rematch = [], 'Carrier', False, False
            editable = bool(state and state['phase'] == 'placement' and not state['me']['ready'] and not sent_ready)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False
                if event.type == pygame.KEYDOWN and editable:
                    if event.key == pygame.K_r:
                        vertical = not vertical
                    if event.key in (pygame.K_1, pygame.K_2, pygame.K_3):
                        selected = list(LENGTHS)[event.key-pygame.K_1]
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and state and not connection.fatal:
                    mx, my = event.pos
                    if editable:
                        if buttons['random'].collidepoint(event.pos):
                            fleet = random_fleet()
                        elif buttons['clear'].collidepoint(event.pos):
                            fleet = []
                        elif buttons['ready'].collidepoint(event.pos):
                            if len(fleet) == 3:
                                connection.submit('ready', fleet=[dict(s) for s in fleet])
                                sent_ready = True
                            else:
                                notice, notice_until = 'Place all three ships first.', time.monotonic()+3
                        elif LEFT <= mx < LEFT+360 and TOP <= my < TOP+360:
                            candidate = {'name': selected, 'x': (mx-LEFT)//CELL, 'y': (my-TOP)//CELL, 'vertical': vertical}
                            if can_place(fleet, candidate, ignore=selected):
                                fleet = [s for s in fleet if s['name'] != selected] + [candidate]
                                selected = next((n for n in LENGTHS if not any(s['name'] == n for s in fleet)), selected)
                            else:
                                notice, notice_until = 'Cannot place here: overlap or outside board.', time.monotonic()+3
                    elif state['phase'] == 'battle' and state['my_turn']:
                        if RIGHT <= mx < RIGHT+360 and TOP <= my < TOP+360:
                            x, y = (mx-RIGHT)//CELL, (my-TOP)//CELL
                            if f'{x},{y}' not in state['shots']:
                                connection.submit('attack', x=x, y=y)
                    elif state['phase'] == 'finished' and buttons['rematch'].collidepoint(event.pos) and not sent_rematch:
                        connection.submit('rematch')
                        sent_rematch = True
            screen.fill((9, 28, 42))
            text('BATTLESHIP / LAB', 60, 24, GOLD, title)
            text('YOUR FLEET', LEFT, 106)
            text('TARGET WATERS', RIGHT, 106)
            board(LEFT, {})
            board(RIGHT, state['shots'] if state else {})
            for ship in (state['fleet'] if state and state['me']['ready'] else fleet):
                draw_ship(ship)
            # Draw incoming attack markers on top of the player's ships.
            if state:
                for key, shot in state['incoming'].items():
                    x, y = map(int, key.split(','))
                    color = (244,104,88) if shot['kind'] != 'miss' else (175,208,219)
                    pygame.draw.circle(screen, color, (LEFT+x*CELL+18,TOP+y*CELL+18), 9 if shot['kind'] != 'miss' else 4)
            if editable:
                mx, my = pygame.mouse.get_pos()
                if LEFT <= mx < LEFT+360 and TOP <= my < TOP+360:
                    candidate = {'name':selected, 'x':(mx-LEFT)//CELL, 'y':(my-TOP)//CELL, 'vertical':vertical}
                    color = (100,224,164) if can_place(fleet,candidate,ignore=selected) else (244,104,88)
                    for x,y in cells(candidate):
                        if 0 <= x < SIZE and 0 <= y < SIZE:
                            pygame.draw.rect(screen,color,(LEFT+x*CELL+2,TOP+y*CELL+2,CELL-4,CELL-4),3)
                text(f'1 / 2 / 3: ship    R: rotate    Selected: {selected}',60,610,face=small)
                for key,label in [('random','Random fleet'),('clear','Clear'),('ready','Ready')]:
                    pygame.draw.rect(screen,(39,85,105),buttons[key],border_radius=6)
                    text(label,buttons[key].x+12,buttons[key].y+10)
            if state:
                phase = state['phase']
                status = {'lobby':'Waiting for another player...', 'placement':'Place ships, then press Ready.',
                          'battle':'YOUR TURN — fire on the right.' if state['my_turn'] else 'Enemy turn...',
                          'finished':'YOU WIN!' if state['won'] else 'Enemy wins. Try again!',
                          'disconnected':'Opponent left. Close and reconnect.'}[phase]
                if phase == 'placement' and (state['me']['ready'] or sent_ready):
                    status = 'Fleet locked. Waiting for opponent...'
                text(status,60,70,GOLD)
                me = state['me']
                # Task 1: replace this placeholder with score, hits/shots and accuracy.
                # These snapshot values already include the correct victory bonus.
                text('Battle statistics arrive in Day 10.',60,520,face=small)
                enemy = state['enemy']
                if enemy:
                    text(f"Ships left: you {3-enemy['sunk']} / enemy {3-me['sunk']}   Wins {me['wins']} : {enemy['wins']}",560,520,face=small)
                if phase == 'finished':
                    pygame.draw.rect(screen,(39,85,105),buttons['rematch'],border_radius=6)
                    text('Waiting...' if sent_rematch else 'Play again',572,560)
                    text(f"Rematch votes: {state['rematch_votes']}/2",560,610,face=small)
                if not editable:
                    # Task 2: show the latest three reports; keep this guard and spacing.
                    for i,line in enumerate(state['log'][-1:]):
                        text(line,60,565+i*24,face=small)
            else:
                text('Connecting...',60,70,GOLD)
            if connection.error:
                notice, notice_until = connection.error, time.monotonic()+3
                if state and not state['me']['ready']:
                    sent_ready = False
            if time.monotonic() < notice_until:
                text(notice[:100],60,655,(255,155,130),small)
            text('ESC: exit',850,30,face=small)
            pygame.display.flip()
            if args.smoke:
                running = False
    finally:
        connection.close()
        pygame.quit()


if __name__ == '__main__':
    run()

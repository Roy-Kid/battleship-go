"""Number keys select ships, R rotates, left board places; Space randomizes, Enter starts."""
from pathlib import Path
import random
import sys
import pygame
from board import LENGTHS, cells, can_place, random_fleet, fire, statistics

ASSETS = Path(__file__).resolve().parent / 'assets'
pygame.init()
screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption('Battleship Lab')
font = pygame.font.Font(str(ASSETS / 'font.ttf'), 17)
clock = pygame.time.Clock()
CELL, TOP = 36, 120
LEFT, RIGHT = 60, 560
fleet = []
selected = 'Carrier'
vertical = False
phase = 'placement'
message = '1/2/3: select ship | R: rotate | SPACE: random fleet'
shots = {}
enemy = random_fleet()
incoming = {}
my_turn = True
ai_at = 0

def text(value, x, y):
    screen.blit(font.render(value, True, 'white'), (x, y))


def draw_board(origin, attacks):
    pygame.draw.rect(screen, (18, 62, 82), (origin, TOP, 360, 360))
    for i in range(11):
        pygame.draw.line(screen, (100,150,170), (origin+i*CELL,TOP), (origin+i*CELL,TOP+360))
        pygame.draw.line(screen, (100,150,170), (origin,TOP+i*CELL), (origin+360,TOP+i*CELL))
    for key, result in attacks.items():
        x, y = map(int, key.split(','))
        color = 'tomato' if result['kind'] != 'miss' else 'white'
        pygame.draw.circle(screen, color, (origin+x*CELL+18,TOP+y*CELL+18), 7)


running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and phase == 'placement':
            if event.key == pygame.K_r:
                vertical = not vertical
            if event.key in (pygame.K_1, pygame.K_2, pygame.K_3):
                selected = list(LENGTHS)[event.key-pygame.K_1]
            if event.key == pygame.K_SPACE:
                fleet = random_fleet()
            if event.key == pygame.K_RETURN:
                if len(fleet) == 3:
                    phase = 'battle'
                    message = 'Click the right board to fire.'
                else:
                    message = 'Place all three ships first.'
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos
            if phase == 'placement' and LEFT <= mx < LEFT+360 and TOP <= my < TOP+360:
                candidate = {'name': selected, 'x': (mx-LEFT)//CELL,
                             'y': (my-TOP)//CELL, 'vertical': vertical}
                if can_place(fleet, candidate, ignore=selected):
                    fleet = [s for s in fleet if s['name'] != selected] + [candidate]
                    selected = next((n for n in LENGTHS if not any(s['name']==n for s in fleet)), selected)
                else:
                    message = 'Overlap or outside board. Try another cell.'
            if phase == 'battle' and my_turn and RIGHT <= mx < RIGHT+360 and TOP <= my < TOP+360:
                try:
                    result = fire(enemy, shots, (mx-RIGHT)//CELL, (my-TOP)//CELL)
                    message = result['kind'].upper()
                    if statistics(shots)['sunk'] == 3:
                        phase = 'finished'
                        message = 'YOU WIN! Close the window to play again.'
                    my_turn = False
                    ai_at = pygame.time.get_ticks() + 600
                except ValueError as error:
                    message = str(error)
    if phase == 'battle' and not my_turn and pygame.time.get_ticks() >= ai_at:
        choices = [(x,y) for x in range(10) for y in range(10) if f'{x},{y}' not in incoming]
        fire(fleet, incoming, *random.choice(choices))
        if statistics(incoming)['sunk'] == 3:
            phase = 'finished'
            message = 'COMPUTER WINS. Close the window to try again.'
        else:
            message = 'YOUR TURN'
        my_turn = True
    screen.fill((9,28,42))
    text('YOUR FLEET', LEFT, 80)
    text('TARGET WATERS', RIGHT, 80)
    draw_board(LEFT, {})
    draw_board(RIGHT, shots)
    for s in fleet:
        for x,y in cells(s):
            pygame.draw.rect(screen, (75,180,155), (LEFT+x*CELL+4,TOP+y*CELL+4,CELL-8,CELL-8))
    for key, result in incoming.items():
        x,y = map(int,key.split(','))
        pygame.draw.circle(screen, 'tomato' if result['kind']!='miss' else 'white', (LEFT+x*CELL+18,TOP+y*CELL+18),7)
    if phase == 'placement':
        mx,my = pygame.mouse.get_pos()
        if LEFT <= mx < LEFT+360 and TOP <= my < TOP+360:
            candidate = {'name':selected, 'x':(mx-LEFT)//CELL, 'y':(my-TOP)//CELL, 'vertical':vertical}
            color = 'green' if can_place(fleet,candidate,ignore=selected) else 'red'
            for x,y in cells(candidate):
                if 0 <= x < 10 and 0 <= y < 10:
                    pygame.draw.rect(screen,color,(LEFT+x*CELL+2,TOP+y*CELL+2,CELL-4,CELL-4),3)
        text('Selected: '+selected, LEFT, 525)
        text('ENTER: lock fleet and start', RIGHT, 525)
    if phase != 'placement':
        stats = statistics(shots)
        score = stats['score'] + (100 if phase == 'finished' and stats['sunk']==3 else 0)
        text(f"Score {score} | Hits {stats['hits']}/{stats['shots']} | Accuracy {stats['accuracy']}%", LEFT, 560)
    text(message, LEFT, 30)
    pygame.display.flip()
    if '--smoke' in sys.argv:
        running = False
pygame.quit()

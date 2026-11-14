"""Day 2 scalar comparison for PPT 4. Demonstrate for at most two minutes.
Coordinates are zero-based (column, row). Drawing and placement checks are supplied.
"""
from pathlib import Path
import sys
import pygame
from board import SIZE, LENGTHS, cells, can_place

# Teacher supplied. The visible grid uses the same cell rules as later lessons.
ASSETS = Path(__file__).resolve().parent / 'assets'
CELL, LEFT, TOP = 40, 60, 110
pygame.init()
screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption('Battleship Lab | Data on the board')
font = pygame.font.Font(str(ASSETS / 'font.ttf'), 17)
small = pygame.font.Font(str(ASSETS / 'font.ttf'), 14)
clock = pygame.time.Clock()
water = pygame.image.load(str(ASSETS / 'sea.png')).convert()
water = pygame.transform.scale(water, (400, 400))
ship_image = pygame.image.load(str(ASSETS / 'ship.png')).convert_alpha()

TITLE = '00 Separate column and row'
col, row = 2, 3
selected = 0
notice = 'Click a grid cell to change the data.'
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos
            if LEFT <= mx < LEFT + 400 and TOP <= my < TOP + 400:
                # Teacher supplied. Convert pixels to a board cell.
                clicked = ((mx - LEFT) // CELL, (my - TOP) // CELL)
                col, row = clicked
                notice = 'Separate column and row values changed.'
    position = (col, row)
    records = []
    panel = ['Separate values', f'position = {position}', '', 'First entry selects the column.', 'Second entry selects the row.', '', 'Cell (2, 3) is column 2, row 3.', 'Click (4, 1) and read the new values.']
    # Teacher supplied. Draw records using cells(), the existing board rule.
    screen.fill((9, 28, 42))
    screen.blit(font.render(TITLE, True, (250, 195, 88)), (LEFT, 25))
    screen.blit(water, (LEFT, TOP))
    for i in range(SIZE + 1):
        pygame.draw.line(screen, (135, 185, 200),
                         (LEFT + i * CELL, TOP), (LEFT + i * CELL, TOP + 400))
        pygame.draw.line(screen, (135, 185, 200),
                         (LEFT, TOP + i * CELL), (LEFT + 400, TOP + i * CELL))
    for i in range(SIZE):
        screen.blit(small.render(str(i), True, 'white'), (LEFT + i * CELL + 16, TOP - 25))
        screen.blit(small.render(str(i), True, 'white'), (LEFT - 25, TOP + i * CELL + 12))
    for index, record in enumerate(records):
        length = LENGTHS[record['name']]
        picture = pygame.transform.scale(ship_image, (CELL - 10, length * CELL - 10))
        if not record['vertical']:
            picture = pygame.transform.rotate(picture, 90)
        screen.blit(picture, (LEFT + record['x'] * CELL + 5, TOP + record['y'] * CELL + 5))
        color = (250, 195, 88) if index == selected else (100, 224, 164)
        for col, row in cells(record):
            pygame.draw.rect(screen, color,
                             (LEFT + col * CELL + 2, TOP + row * CELL + 2, CELL - 4, CELL - 4), 2)
    pygame.draw.rect(screen, (255, 255, 255),
                     (LEFT + position[0] * CELL + 1, TOP + position[1] * CELL + 1, CELL - 2, CELL - 2), 3)
    for i, line in enumerate(panel):
        screen.blit(small.render(line, True, (229, 242, 239)), (500, 115 + i * 29))
    screen.blit(font.render(notice, True, (250, 195, 88)), (LEFT, 555))
    screen.blit(small.render('Click a cell | Read its column and row in the data panel', True, 'white'), (LEFT, 595))
    pygame.display.flip()
    clock.tick(60)
    if '--smoke' in sys.argv:
        running = False
pygame.quit()

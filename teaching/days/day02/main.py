"""Day 2 reference: organize ship records in a fleet list.
1/2 selects a ship; arrows update its data; R changes orientation.
"""
from pathlib import Path
import sys
import pygame

# Teacher supplied: window, assets and input handling.
ASSETS = Path(__file__).resolve().parent / 'assets'
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Battleship Lab | Data structures | 1/2: select ship')
clock = pygame.time.Clock()
sea = pygame.image.load(str(ASSETS / 'sea.png'))
sea = pygame.transform.scale(sea, (800, 600))
ship_image = pygame.image.load(str(ASSETS / 'ship.png'))
ship_image = pygame.transform.scale(ship_image, (48, 144))

# Core concept: a list stores ordered ship records; each dictionary has named fields.
# These x/y values are PIXELS. Later board lessons use column/row cell coordinates.
fleet = [
    {'name': 'Scout', 'x': 200, 'y': 180, 'vertical': True},
    {'name': 'Cruiser', 'x': 500, 'y': 300, 'vertical': False},
]
selected = 0
speed = 4
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_1, pygame.K_2):
                selected = event.key - pygame.K_1
            if event.key == pygame.K_r:
                fleet[selected]['vertical'] = not fleet[selected]['vertical']
    # ship refers to the selected dictionary, not a copy of it.
    ship = fleet[selected]
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship['x'] -= speed
    if keys[pygame.K_RIGHT]:
        ship['x'] += speed
    if keys[pygame.K_UP]:
        ship['y'] -= speed
    if keys[pygame.K_DOWN]:
        ship['y'] += speed
    screen.blit(sea, (0, 0))
    # Teacher supplied today; Day 3 explains this repetition in detail.
    for ship in fleet:
        picture = ship_image if ship['vertical'] else pygame.transform.rotate(ship_image, 90)
        ship['x'] = max(0, min(ship['x'], 800-picture.get_width()))
        ship['y'] = max(0, min(ship['y'], 600-picture.get_height()))
        position = (ship['x'], ship['y'])  # A tuple groups x and y in order.
        screen.blit(picture, position)
    pygame.display.flip()
    clock.tick(60)
    if '--smoke' in sys.argv:
        running = False
pygame.quit()

"""Day 2, step 2: group one ship's fields in a dictionary.
Run: python 02_ship_record.py
Focus: named fields, dictionary updates and a position tuple for drawing.
"""
from pathlib import Path
import sys
import pygame

# [Teacher supplied] Keep the same window, assets, controls and boundaries.
ASSETS = Path(__file__).resolve().parent / 'assets'
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Day 2 | 02 Ship dictionary')
clock = pygame.time.Clock()
sea = pygame.image.load(str(ASSETS / 'sea.png'))
sea = pygame.transform.scale(sea, (800, 600))
# The image and the data record have different responsibilities and names.
ship_image = pygame.image.load(str(ASSETS / 'ship.png'))
ship_image = pygame.transform.scale(ship_image, (48, 144))

# [Focus A] String keys describe the fields belonging to one ship.
ship = {'name': 'Scout', 'x': 200, 'y': 180, 'vertical': True}
speed = 4

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            ship['vertical'] = not ship['vertical']

    keys = pygame.key.get_pressed()
    # [Focus B] Change a named field directly; the other fields stay unchanged.
    if keys[pygame.K_LEFT]:
        ship['x'] -= speed
    if keys[pygame.K_RIGHT]:
        ship['x'] += speed
    if keys[pygame.K_UP]:
        ship['y'] -= speed
    if keys[pygame.K_DOWN]:
        ship['y'] += speed

    # [Teacher supplied] The existing controls now read the record's fields.
    picture = ship_image if ship['vertical'] else pygame.transform.rotate(ship_image, 90)
    ship['x'] = max(0, min(ship['x'], 800-picture.get_width()))
    ship['y'] = max(0, min(ship['y'], 600-picture.get_height()))
    screen.blit(sea, (0, 0))
    # [Focus C] A dictionary describes the ship; a tuple describes its position.
    position = (ship['x'], ship['y'])
    screen.blit(picture, position)
    pygame.display.flip()
    clock.tick(60)
    if '--smoke' in sys.argv:
        running = False

pygame.quit()

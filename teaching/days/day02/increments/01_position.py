"""Day 2, step 1: group x and y in a position tuple.
Run: python 01_position.py
Focus: index access and assigning a new tuple when the position changes.
"""
from pathlib import Path
import sys
import pygame

# [Teacher supplied] Window, assets, controls and boundary handling.
ASSETS = Path(__file__).resolve().parent / 'assets'
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Day 2 | 01 Position tuple')
clock = pygame.time.Clock()
sea = pygame.image.load(str(ASSETS / 'sea.png'))
sea = pygame.transform.scale(sea, (800, 600))
ship_image = pygame.image.load(str(ASSETS / 'ship.png'))
ship_image = pygame.transform.scale(ship_image, (48, 144))

# [Focus A] One ordered pair: index 0 is x; index 1 is y.
# Coordinates are pixels measured from the image's top-left corner.
position = (200, 180)
vertical = True
speed = 4

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            vertical = not vertical

    keys = pygame.key.get_pressed()
    # [Focus B] Tuple entries cannot be replaced. Assign a new tuple instead.
    # Read position[0] and position[1] before calculating the new position.
    if keys[pygame.K_LEFT]:
        position = (position[0] - speed, position[1])
    if keys[pygame.K_RIGHT]:
        position = (position[0] + speed, position[1])
    if keys[pygame.K_UP]:
        position = (position[0], position[1] - speed)
    if keys[pygame.K_DOWN]:
        position = (position[0], position[1] + speed)

    # [Teacher supplied] Keep the rotated image inside the window.
    picture = ship_image if vertical else pygame.transform.rotate(ship_image, 90)
    position = (
        max(0, min(position[0], 800-picture.get_width())),
        max(0, min(position[1], 600-picture.get_height())),
    )
    screen.blit(sea, (0, 0))
    # [Focus C] blit receives the whole coordinate pair as one argument.
    screen.blit(picture, position)
    pygame.display.flip()
    clock.tick(60)
    if '--smoke' in sys.argv:
        running = False

pygame.quit()

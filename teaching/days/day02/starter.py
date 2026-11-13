"""Day 2 starting point: separate values, ready to organize into a ship record.
Keyboard and drawing support are supplied. See README.md for the data-structure tasks.
"""
from pathlib import Path
import sys
import pygame

# Teacher supplied: window, assets, keyboard input and boundary handling.
ASSETS = Path(__file__).resolve().parent / "assets"
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Battleship Lab")
clock = pygame.time.Clock()
sea = pygame.image.load(str(ASSETS / "sea.png"))
sea = pygame.transform.scale(sea, (800, 600))
ship = pygame.image.load(str(ASSETS / "ship.png"))
ship = pygame.transform.scale(ship, (48, 144))

# Task 1: group x, y and vertical in one dictionary with named fields.
x, y = 200, 180
speed = 4
vertical = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            vertical = not vertical
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    picture = ship if vertical else pygame.transform.rotate(ship, 90)
    x = max(0, min(x, 800-picture.get_width()))
    y = max(0, min(y, 600-picture.get_height()))
    screen.blit(sea, (0, 0))
    # Task 2: read coordinates from the dictionary; form a position tuple.
    # Task 3: put two records in a list; use the supplied fleet drawing loop.
    screen.blit(picture, (x, y))
    pygame.display.flip()
    clock.tick(60)
    if "--smoke" in sys.argv:
        running = False
pygame.quit()

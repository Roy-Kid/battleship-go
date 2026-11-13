"""Run: python main.py. --smoke is for teacher startup checks."""
from pathlib import Path
import sys
import pygame

# Teacher-supplied asset paths work from any working directory.
ASSETS = Path(__file__).resolve().parent / "assets"
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Battleship Lab")
clock = pygame.time.Clock()
sea = pygame.image.load(str(ASSETS / "sea.png"))
sea = pygame.transform.scale(sea, (800, 600))
ship = pygame.image.load(str(ASSETS / "ship.png"))
ship = pygame.transform.scale(ship, (48, 144))

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
    screen.blit(picture, (x, y))
    pygame.display.flip()
    clock.tick(60)
    if "--smoke" in sys.argv:
        running = False
pygame.quit()

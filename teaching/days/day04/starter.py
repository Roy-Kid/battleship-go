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

CELL = 40
LEFT, TOP = 200, 100
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            col = (event.pos[0] - LEFT) // CELL
            row = (event.pos[1] - TOP) // CELL
            if 0 <= col < 10 and 0 <= row < 10:
                print("Column:", col, "Row:", row)
    screen.blit(sea, (0, 0))
    for i in range(11):
        pygame.draw.line(screen, "white", (LEFT+i*CELL,TOP), (LEFT+i*CELL,TOP+400))
        pygame.draw.line(screen, "white", (LEFT,TOP+i*CELL), (LEFT+400,TOP+i*CELL))
    mx, my = pygame.mouse.get_pos()
    col, row = (mx-LEFT)//CELL, (my-TOP)//CELL
    if 0 <= col < 10 and 0 <= row < 10:
        pygame.draw.rect(screen, "yellow", (LEFT+col*CELL,TOP+row*CELL,CELL,CELL), 3)
    pygame.display.flip()
    clock.tick(60)
    if "--smoke" in sys.argv:
        running = False
pygame.quit()

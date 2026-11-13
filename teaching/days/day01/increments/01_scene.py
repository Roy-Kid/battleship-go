"""Step 1: draw a complete scene.
Run: python 01_scene.py
Focus: variables, position, loading images and drawing order.
"""
from pathlib import Path
import sys
import pygame

# [Teacher supplied] Window, clock and asset paths support this lesson.
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('01 Scene | Change position and drawing order')
clock = pygame.time.Clock()
ASSETS = Path(__file__).resolve().parent / "assets"

# [Focus 1] Loading gets the asset; blit draws it.
sea = pygame.image.load(str(ASSETS / "sea.png"))
sea = pygame.transform.scale(sea, (800, 600))  # Fill the window with sea; scaling is explained in the next step.
ship = pygame.image.load(str(ASSETS / "ship.png"))

# [Focus 2] Variables store position; x increases rightwards, y downwards.
# = assigns a value; (x,y) specifies the top-left corner, not the center.
x = 200
y = 180
background = (15, 60, 85)  # RGB background: red, green, blue, each from 0 to 255.

running = True
while running:
    # [Teacher supplied] Handle input each frame; closing the window ends the loop.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # [Focus 3] Draw sea, then ship; later drawing covers earlier drawing.
    screen.fill(background)
    screen.blit(sea, (0, 0))
    screen.blit(ship, (x, y))
    # Challenge: swap the two lines above. Why does the ship disappear?
    # The sea hides background changes; comment out its drawing line and try again.

    # [Teacher supplied] Refresh and limit speed; --smoke is for automated checks.
    pygame.display.flip()
    clock.tick(60)
    if "--smoke" in sys.argv:
        running = False

pygame.quit()

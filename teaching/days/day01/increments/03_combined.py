"""03 Combined controls | Arrows: move R: rotate +/-: scale Space: reset
Run: python 03_combined.py
Change the focus values, save, close the old window, and run again.
"""
from pathlib import Path
import sys
import pygame

# [Teacher supplied] Keep the same window and exit handling in each experiment.
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('03 Combined controls | Arrows: move R: rotate +/-: scale Space: reset')
clock = pygame.time.Clock()
ASSETS = Path(__file__).resolve().parent / "assets"

original = pygame.image.load(str(ASSETS / "ship.png"))
sea = pygame.image.load(str(ASSETS / "sea.png"))
sea = pygame.transform.scale(sea, (800, 600))
# [Combine A] Store position, angle and scale factor in separate variables.
x, y = 400, 300
angle = 0
scale = 2.0
# This file uses the image center, which stays fixed during rotation and scaling.
# 01_scene.py uses the top-left corner; this version switches to the center.

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # [Combine B] Discrete actions: run once for each key press.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                angle = (angle + 90) % 360
            if event.key in (pygame.K_EQUALS, pygame.K_PLUS, pygame.K_KP_PLUS):
                scale = min(4.0, scale + 0.25)
            if event.key in (pygame.K_MINUS, pygame.K_KP_MINUS):
                scale = max(0.5, scale - 0.25)
            if event.key == pygame.K_SPACE:
                x, y, angle, scale = 400, 300, 0, 2.0

    # [Combine C, optional] Continuous actions: check held arrow keys each frame.
    # Combine rotation and scaling first; add movement as a preview of Day 2.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 4
    if keys[pygame.K_RIGHT]:
        x += 4
    if keys[pygame.K_UP]:
        y -= 4
    if keys[pygame.K_DOWN]:
        y += 4
    # Moving off screen is allowed in this version; Space resets the position.

    # [Combine D] Transform the original image using the current values each frame.
    width = max(1, int(original.get_width() * scale))
    height = max(1, int(original.get_height() * scale))
    scaled = pygame.transform.scale(original, (width, height))
    picture = pygame.transform.rotate(scaled, angle)
    rect = picture.get_rect(center=(x, y))
    # [Combine E] Draw sea, then ship; the supplied loop refreshes the display.
    screen.blit(sea, (0, 0))
    screen.blit(picture, rect)

    # [Supplied loop] Refresh and limit the frame rate; --smoke is for teacher checks.
    pygame.display.flip()
    clock.tick(60)
    if "--smoke" in sys.argv:
        running = False

pygame.quit()

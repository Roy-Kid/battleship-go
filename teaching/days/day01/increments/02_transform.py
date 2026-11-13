"""Step 2: rotate and scale the same image.
Run: python 02_transform.py
Original on the left, result on the right. Change one parameter at a time.
"""
from pathlib import Path
import sys
import pygame

# [Teacher supplied] Window setup and loop.
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('02 Image transforms | Original on left, result on right')
clock = pygame.time.Clock()
ASSETS = Path(__file__).resolve().parent / "assets"
original = pygame.image.load(str(ASSETS / "ship.png"))

# [Focus 1] Change size. The 20x100 original scales proportionally to 60x300.
# Keep angle=0 and change width/height; then try 100x100 and observe the shape.
width = 60
height = 300
# [Focus 2] Angle in degrees: positive is anticlockwise, negative clockwise.
# Try 0, 90, 180, 45, -90; predict before running.
angle = 0

# [Focus 3] Scale, then rotate; store each result in a variable.
# Start from original to avoid quality loss from repeated resizing.
scaled = pygame.transform.scale(original, (width, height))
picture = pygame.transform.rotate(scaled, angle)

# [Teacher supplied] Align centers for comparison; rotation may change width and height.
# Original and result have different positions; position does not change rotation direction.
original_rect = original.get_rect(center=(200, 300))
picture_rect = picture.get_rect(center=(600, 300))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((15, 60, 85))
    screen.blit(original, original_rect)
    screen.blit(picture, picture_rect)

    pygame.display.flip()
    clock.tick(60)
    if "--smoke" in sys.argv:
        running = False

pygame.quit()

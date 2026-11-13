"""Lesson 1: put a ship on the sea.
Run: python starter.py
Save your changes, close the old window, then run again.
--smoke is for teacher startup checks; students can skip it.
"""
# 1. Import tools. import makes a module's features available.
from pathlib import Path  # Standard library: file paths.
import sys                # Standard library: used here for teacher startup checks.
import pygame             # Installed game library: windows, images, keyboard and mouse.

# 2. Prepare the window and assets. Teacher supplied; understand their purpose today.
# __file__ is this source file's path; parent is its containing folder.
# With Path objects, / joins paths rather than dividing numbers.
ASSETS = Path(__file__).resolve().parent / "assets"

pygame.init()  # Initialize Pygame before using its features.

# (800, 600) is a tuple: window width, then height, in pixels.
# screen stores the returned display surface, used for drawing later.
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Battleship Lab")  # The quoted string sets the window title.
clock = pygame.time.Clock()  # Create a clock to limit the frame rate.

# load reads an image and returns a surface; it has not been drawn yet.
# str converts the path to a string Pygame can read.
sea = pygame.image.load(str(ASSETS / "sea.png"))
sea = pygame.transform.scale(sea, (800, 600))  # Scale to the window size.
ship = pygame.image.load(str(ASSETS / "ship.png"))
ship = pygame.transform.scale(ship, (48, 144))  # Ship width: 48; height: 144 pixels.

# 3. Store position and color in variables. Focus your changes here today.
# = assigns the right-hand value to the name on the left.
# Use integers for x and y, not strings such as "200".
# The origin is at the top left: x increases rightwards, y downwards.
x = 100
y = 100

# An RGB color is a tuple: red, green, blue, each from 0 to 255.
# The sea covers the background; comment out its drawing line to test colors.
background = (15, 60, 85)

# 4. Game loop: handle input -> draw -> refresh -> limit speed.
# True / False are booleans; their first letters must be capitalized.
running = True
while running:  # Repeat the indented block while running is True.
    # Fetch pending events; for handles each fetched event in turn.
    # With no events, this for body is skipped but drawing still continues.
    for event in pygame.event.get():
        # if tests a condition; == checks equality, whereas = assigns a value.
        # pygame.QUIT is the event created by clicking the window's close button.
        if event.type == pygame.QUIT:
            running = False  # Finish this iteration, then stop before the next one.

    # Align with for: draw every frame, even without input events.
    screen.fill(background)  # Clear with the background color so the previous frame leaves no trail.
    screen.blit(sea, (0, 0))  # Then draw the sea at the window's top left.
    # Student task: use screen.blit to draw ship at (x, y).
    # Hint: follow the sea drawing line above and use the same indentation.
    # Add the ship drawing statement here before looking at main.py.

    # Display this frame: finish drawing before refreshing.
    pygame.display.flip()
    clock.tick(60)  # Limit to about 60 frames per second; this does not guarantee 60 FPS.

    # Teacher check: --smoke runs a single frame; otherwise the game runs normally.
    if "--smoke" in sys.argv:
        running = False

# 5. This unindented line runs after leaving the while loop.
pygame.quit()  # Release Pygame's window and other resources.

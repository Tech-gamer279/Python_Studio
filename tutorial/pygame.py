"""
==========================================
Pygame Tutorial: Getting Started
==========================================

Pygame is a popular Python library for making games and multimedia applications.

------------------------------------------
1. Install Pygame
------------------------------------------
First, install pygame using pip:

    pip install pygame

------------------------------------------
2. Import Pygame and Initialize
------------------------------------------
    import pygame
    pygame.init()

------------------------------------------
3. Create a Game Window
------------------------------------------
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("My First Game")

------------------------------------------
4. Main Game Loop
------------------------------------------
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip()   # Update the display

    pygame.quit()

------------------------------------------
5. Full Example
------------------------------------------
"""

import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My First Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Fill the screen with black
    pygame.display.flip()   # Update the display

pygame.quit()

"""
------------------------------------------
6. Tips
------------------------------------------
- Use `pygame.draw` functions to draw shapes.
- Load images with `pygame.image.load()`.
- Play sounds with `pygame.mixer.Sound()`.

For more information, see the official docs:
https://www.pygame.org/docs/"""
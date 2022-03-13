# Simple pygame program
# Demo: test Github push
# Import and initialize the pygame library
import pygame
from pygame.locals import *
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

img = pygame.image.load('assets/images/alpaca.png')
img.convert()

seal = pygame.image.load('assets/images/spotted_seal.png')
seal.convert()

rect = img.get_rect()
rect.center = 250, 250
transparent = (0, 0, 0, 0)

seal_rect = seal.get_rect()
seal_rect.center = 250, 250
 # Fill the background with white
screen.fill((255, 255, 255))
screen.blit(img, rect)
pygame.display.update()
# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == KEYDOWN and event.key == pygame.K_BACKSPACE:
            screen.fill((255, 255, 255))
            screen.blit(seal, seal_rect)
            pygame.display.update()

# Done! Time to quit.
pygame.quit()
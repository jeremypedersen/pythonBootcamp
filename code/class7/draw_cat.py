# A simple program to demonstrate mouse events
# in PyGame
# 
# Based on code from Al Sweigart's book: https://inventwithpython.com/pygame/
#
# Author: Jeremy Pedersen
#
# Licensed under the Simplified BSD (2-clause) License
import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Cat Drawing')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(catImg, (200, 150))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
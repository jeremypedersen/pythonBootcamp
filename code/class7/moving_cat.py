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

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'

while True: # The main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx += 5
        if catx > 270:
            catx = 270
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty > 220:
            caty = 220
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx < 10:
            catx = 10
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty < 10:
            caty = 10
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
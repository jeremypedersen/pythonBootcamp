import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Draw Transparent Shapes')

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
TRANSPARENT_BLUE = (0, 0, 255, 50)

# draw on the surface object
DISPLAYSURF.fill(WHITE)
ALPHASURF = DISPLAYSURF.convert_alpha()
pygame.draw.rect(ALPHASURF, TRANSPARENT_BLUE, (200, 150, 100, 50))
DISPLAYSURF.blit(ALPHASURF, (0,0))

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

import sys

import pygame
# from pygame.locals import * 

pygame.init()
clock = pygame.Clock()
pygame.display.set_caption("My game!")

WINDOW_SIZE = (400, 400)

screen = pygame.display.set_mode(WINDOW_SIZE)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            


    pygame.display.update()
    clock.tick(60)
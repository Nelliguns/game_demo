import sys

import pygame
# from pygame.locals import * 

pygame.init()
clock = pygame.Clock()
pygame.display.set_caption("My game!")

WINDOW_SIZE = (400, 400)

screen = pygame.display.set_mode(WINDOW_SIZE)

player_img = pygame.image.load("data/images/00.png").convert()
player_img.set_colorkey((0, 0, 0))

moving_right = False
moving_left = False

player_location = [50, 50]
player_y_momentum = 0

player_rect = pygame.Rect(*player_location, *player_img.get_size())

test_rect = pygame.Rect(100, 100, 100, 50)

while True:
    screen.fill((0, 0, 0))
    screen.blit(player_img, player_location)

    if player_location[1] > WINDOW_SIZE[1] - player_img.get_height():
        player_y_momentum = - player_y_momentum
    else:
        player_y_momentum += 0.2
    player_location[1] += player_y_momentum

    if moving_right:
        player_location[0] += 4
    if moving_left:
        player_location[0] -= 4
    
    player_rect.x, player_rect.y = player_location

    if player_rect.colliderect(test_rect):
        pygame.draw.rect(screen, (255, 0, 0), test_rect)
    else:
        pygame.draw.rect(screen, (0, 0, 255), test_rect)
        


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_a:
                moving_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_a:
                moving_left = False
            


    pygame.display.update()
    clock.tick(60)
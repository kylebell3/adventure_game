import pygame
import time

pygame.init()

pygame.display.set_caption("An Adventure")

screen = pygame.display.set_mode((800,600))


# define colors
purple = (78, 65, 135)
blue = (48, 131, 220)
yellow = (248, 255, 229)
green = (125, 222, 146)
blue_green = (46, 191, 165)
        
# clock
clock = pygame.time.Clock()


sword = False  # sword starts put away


def game_loop():
    # player starting coordinates and size
    player_x = 375
    player_y = 500
    player_w = 50
    player_h = 50
    player_speed = 3
    x = 0       # used to change x value
    y = 0       # used to change y value
    sword_counter = 0

    while True:

        screen.fill(yellow) 
        global sword

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()  # checks what keys are pressed

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
   
            ##########
            # Movement
            ###########
            elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x = -player_speed

                    if event.key == pygame.K_RIGHT:
                        x = player_speed

                    if event.key == pygame.K_DOWN:
                        y = player_speed

                    if event.key == pygame.K_UP:
                        y = -player_speed

                    # attack with sword
                    if event.key == pygame.K_SPACE:
                        sword = True
                        print('what')

            # if a key is lifed while another is still held down     
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_RIGHT):
                    x = 0

                elif (event.key == pygame.K_LEFT):
                    x = 0
                    
                elif (event.key == pygame.K_DOWN):
                    y = 0

                elif (event.key == pygame.K_UP):
                    y = 0

            else:
                x = 0
                y = 0

        #============
        # Boundaries
        #============
        # left/right boundary
        if (player_x >= 800 - player_w):
            if x > 0:
                x = 0

        if (player_x <= 0):
            if x < 0:
                x = 0

        # top/bottom boundary
        if (player_y >= 600 - player_h):
            if y > 0:
                y = 0

        if (player_y <= 0):
            if y < 0:
                y = 0

        # set new position based on movement
        player_x += x  
        player_y += y


        # sword will swing for ~.8 seconds
        if sword_counter >= 50:
            sword = False
            sword_counter = 0

        if sword:
            # draw sword
            pygame.draw.rect(screen, blue_green, [(player_x + 35), (player_y - 55), 9, 60])
            pygame.draw.rect(screen, blue_green, [(player_x + 20), (player_y - 20), 37, 8])
            sword_counter += 1

        pygame.draw.rect(screen, blue, [player_x, player_y, player_w, player_h])


        # pygame.draw.rect(screen, blue_green, [500, 0, 2, 1000]) # line long screen

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
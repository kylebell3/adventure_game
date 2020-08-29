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

while True:
    # player starting coordinates and size
    player_x = 375
    player_y = 500
    player_w = 50
    player_h = 50

    # clock
    clock = pygame.time.Clock()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    


    ##########
    # Movement
    ###########
    
        keys = pygame.key.get_pressed()  # checks what keys are pressed

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                player_x += -5

        #     elif event.key == pygame.K_RIGHT:
        #         player_x += 5

        #     elif event.key == pygame.K_p:
        #         pause = True
        #         paused()

        # # if a key is lifed while another is still held down     
        # if event.type == pygame.KEYUP:
            
        #     if (event.key == pygame.K_RIGHT) and keys[pygame.K_LEFT]:
        #         player_x += -5

        #     elif (event.key == pygame.K_LEFT) and keys[pygame.K_RIGHT]:
        #         player_x += 5 
                
        #     else:
        #         player_x += 0

    print(player_x)
    screen.fill(yellow) 

    pygame.draw.rect(screen, blue, [player_x, player_y, player_w, player_h])

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
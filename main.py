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

def game_loop():

    player_x = 375
    player_y = 500
    player_w = 50
    player_h = 50
    player_speed = 3
    x = 0       # used to change x value
    y = 0       # used to change y value

    while True:
        # player starting coordinates and size

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
                    x = -player_speed

                elif event.key == pygame.K_RIGHT:
                    x = player_speed

                if event.key == pygame.K_DOWN:
                    y = player_speed

                elif event.key == pygame.K_UP:
                    y = -player_speed

            # if a key is lifed while another is still held down     
            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_RIGHT) and keys[pygame.K_LEFT]:
                    x = -player_speed

                elif (event.key == pygame.K_LEFT) and keys[pygame.K_RIGHT]:
                    x = player_speed
                    
                elif (event.key == pygame.K_DOWN) and keys[pygame.K_UP]:
                    y = -player_speed

                elif (event.key == pygame.K_UP) and keys[pygame.K_DOWN]:
                    y = player_speed
                
                else:
                    x = 0
                    y = 0

        player_x += x
        player_y += y

        screen.fill(yellow) 

        pygame.draw.rect(screen, blue, [player_x, player_y, player_w, player_h])

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
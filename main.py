import pygame
import time
import random

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

class Enemy():
    def __init__(self):
        self.x = random.randrange(100, 650)
        self.y = random.randrange(10, 200)
        self.patrol_x = 0
        self.patrol_count = 0


def draw_enemy(x,y):
    pygame.draw.rect(screen, purple, [x, y, 50, 50])


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
    enemy_list = []    # contains all the active enemy objects

    blade_x = (player_x + 35)  # sword blade x position
    blade_y = (player_y - 55)  # sword blade y position
    

    patrol_count = 0      # timer for patrol movement
    patrol_x = 0
    patrol_y = 0

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

                    # spawn enemy
                    if event.key == pygame.K_e:
                        enemy_list.append(Enemy())

                    # quit with "tab"
                    if event.key == pygame.K_TAB:
                        pygame.quit()
                        quit()


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


        # sword will swing for ~.5 seconds
        if sword_counter >= 35:
            sword = False
            sword_counter = 0

        if sword:
            # draw sword
            pygame.draw.rect(screen, blue_green, [(player_x + 35), (player_y - 55), 9, 60])
            pygame.draw.rect(screen, blue_green, [(player_x + 20), (player_y - 20), 37, 8])
            sword_counter += 1


            
        
        
    ##############
    # draw enemies
    ##############
        for e in enemy_list:
            # move enemy
            e.patrol_count += 1
            e.x += e.patrol_x
                        
            if 100 < e.patrol_count <= 200:
                e.patrol_x = 1

            if e.patrol_count > 200 :
                e.patrol_x = -1

            if e.patrol_count >= 300:
                e.patrol_count = 100

            # e.y += 
            draw_enemy(e.x, e.y)

            # kill enemy if hit by sword
            if (( (e.x + 50) >= (player_x + 35)  ) and (e.x <= (player_x + 44))) and ( (e.y + 50) >= (player_y - 60)  ) and (e.y <= (player_y)) and sword == True:
                enemy_list.remove(e)
                # print("DELETED")


        # Draw Player
        pygame.draw.rect(screen, blue, [player_x, player_y, player_w, player_h])


        # pygame.draw.rect(screen, blue_green, [500, 0, 2, 1000]) # line long screen

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
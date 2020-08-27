import pygame
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(yellow)

    pygame.display.update()


pygame.quit()
quit()
import pygame, sys
from settings import *
from level import Level

iconName= 'A Bounce Tales: Hot Air Pursuit'
pygame.display.set_caption(iconName)

# initalising pygame in to the app
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

level = Level()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BG_COLOR)
    level.run()

    pygame.display.update()
    clock.tick(60)
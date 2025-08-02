import pygame
from pygame.locals import *
from sys import exit 

pygame.init()

tela = pygame.display.set_mode((640, 480))
pygame.display.set_caption('game')

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, (0, 255, 0), (320, 240, 40, 50))
    pygame.draw.circle(tela, (0, 0, 255), (200, 100), 40)
    pygame.draw.line(tela, (255, 0, 0), (20, 90), (100, 40), 3)

    pygame.display.update()
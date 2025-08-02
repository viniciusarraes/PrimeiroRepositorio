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

    pygame.draw.rect(tela, (200, 10, 34), (320, 240, 40, 50))

    pygame.display.update()
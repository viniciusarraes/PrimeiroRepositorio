import pygame
from pygame.locals import *
from sys import exit 

pygame.init()

x = 320 - 25
y = 0

tela = pygame.display.set_mode((640, 480))
pygame.display.set_caption('game')
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    tela.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(tela, (0, 255, 0), (x, y, 40, 50))
    if y >= 480:
        y = 0
    y += 1

    pygame.display.update()
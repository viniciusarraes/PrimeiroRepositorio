import pygame
from pygame.locals import *
from sys import exit 

pygame.init()

x = 320
y = 240

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

    if pygame.key.get_pressed()[K_a]:
        x -= 5
    elif pygame.key.get_pressed()[K_d]:
        x += 5
    elif pygame.key.get_pressed()[K_w]:
        y -= 5
    elif pygame.key.get_pressed()[K_s]:
        y += 5

    pygame.draw.rect(tela, (144, 238, 144), (x, y, 40, 40))
    
    pygame.display.update()
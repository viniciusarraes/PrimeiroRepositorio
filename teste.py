import pygame
from pygame.locals import *
from sys import exit 
from random import randint

pygame.init()

x = 320
y = 240

x_ver = randint(20, 235)
y_ver = randint(20, 230)

tela = pygame.display.set_mode((640, 480))
pygame.display.set_caption('game')
clock = pygame.time.Clock()

fonte = pygame.font.SysFont('arial', 40, True, True)

pontos = 0

while True:
    clock.tick(60)
    tela.fill((0,0,0))

    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))

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
        
    ret_sla = pygame.draw.rect(tela, (144, 238, 144), (x, y, 40, 40))
    ret_ver = pygame.draw.rect(tela, (255, 0, 0), (x_ver, y_ver, 40, 40))

    if ret_sla.colliderect(ret_ver):
        x_ver = randint(20, 235)
        y_ver = randint(20, 230)
        pontos += 1
    
    tela.blit(texto_formatado, (230, 430))
    pygame.display.update()
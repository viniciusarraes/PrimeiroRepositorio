import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480
x = largura//2
y = altura//2

x_azul = randint(40, 60)
y_azul = randint(50, 430)

fonte = pygame.font.SysFont('arial', 40, True, True)

pontos = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('snake_game')
relogio = pygame.time.Clock()

while True:
    relogio.tick(35)
    tela.fill((0,0,0))

    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    chave = pygame.key.get_pressed()
    if chave[K_a]:
        x -= 20
    elif chave[K_d]:
        x += 20
    elif chave[K_w]:
        y -= 20
    elif chave[K_s]:
        y += 20
    
    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x, y, 40, 50))
    ret_azul = pygame.draw.rect(tela, (0,0,255), (x_azul, y_azul, 40, 50))

    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos += 1

    tela.blit(texto_formatado, (430, 40))
    
    pygame.display.update()
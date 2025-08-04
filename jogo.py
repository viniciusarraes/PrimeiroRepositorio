import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480

x_cobra = largura//2
y_cobra = altura//2

x_maca = randint(40, 60)
y_maca = randint(50, 430)

fonte = pygame.font.SysFont('arial', 40, True, True)

pontos = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('jogo')
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((255, 255, 255))

    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    chave = pygame.key.get_pressed()
    if chave[K_a]:
        x_cobra -= 20
    elif chave[K_d]:
        x_cobra += 20
    elif chave[K_w]:
        y_cobra -= 20
    elif chave[K_s]:
        y_cobra += 20
    
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))

    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1

    tela.blit(texto_formatado, (430, 40))
    
    pygame.display.update()
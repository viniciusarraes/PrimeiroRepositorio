import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Mover Ponto")

# Cores
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Posição inicial do ponto
x, y = largura // 2, altura // 2
velocidade = 5

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Capturar teclas pressionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade
    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade

    # Atualizar a tela
    tela.fill(branco)
    pygame.draw.circle(tela, vermelho, (x, y), 10)  # Desenha o ponto como um círculo
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # Limita a 60 FPS
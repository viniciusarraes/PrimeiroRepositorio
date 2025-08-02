import pygame

#initializing pygame
pygame.init()

#create a screen (360x480)
screen = pygame.display.set_mode((360, 480))

#name the window
pygame.display.set_caption("main_screen")

#game loop
running = True
while running:
    #quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0,0,0))

    pygame.display.update()

pygame.quit()
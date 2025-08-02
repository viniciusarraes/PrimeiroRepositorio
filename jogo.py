import pygame

#initializing pygame
pygame.init()

#create a screen (360x480)
screen = pygame.display.set_mode((400, 480))

#framerate
clock = pygame.time.Clock()

#defining a square (player)
player_x = 0
player_y = 320 - 30

#ground
ground = pygame.Rect(0, 320, 400, 480 - 320)

#platform


#name the window
pygame.display.set_caption("main_screen")

#game loop
running = True
while running:
    clock.tick(60)
    #quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_a]:
        if player_x > 0:
            player_x -= 3
    elif pressed_key[pygame.K_d]:
        if player_x + 30 < 400:
            player_x += 3
    elif pressed_key[pygame.K_SPACE]:
        if player_y + 30 == 320:
            player_y -= 60
    
    screen.fill((0,0,0))

    #gravity
    if player_y + 30 == 320 or (player_y + 30 == 280 and player_x + 30 >= 250 and player_x <= 250 + 80):
        player_y += 0
    else:
        player_y += 1

    pygame.draw.rect(screen, (139, 69, 19), ground)
    pygame.draw.rect(screen, (128, 0, 128), (player_x, player_y, 30, 30))
    pygame.draw.rect(screen, (139, 69, 19), (250, 280, 80, 10))

    pygame.display.update()

pygame.quit()
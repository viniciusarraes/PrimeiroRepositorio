import pygame

pygame.init()

screen_widht = 800
screen_height = 600
screen = pygame.display.set_mode((screen_widht, screen_height))

pygame.display.set_caption('new_game')

brown = (100, 40, 0)
blue = (0, 0, 255)

player = pygame.Rect(0, 470, 30, 30)
platform = pygame.Rect(50, 400, 200, 20)
ground = pygame.Rect(0, 500, screen_widht, screen_height - 500)

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= 5
    if keys[pygame.K_d]:
        player.x += 5
    if keys[pygame.K_SPACE]:
        player.y -= 5

    if player.colliderect(platform):
        if player.bottom >= platform.top and player.bottom <= platform.bottom and player.right > platform.left and player.left < platform.right:
            player.y = platform.top - player.height
    
    if player.colliderect(platform):
        if player.top <= platform.bottom and player.top >= platform.top and player.right > platform.left and player.left < platform.right:
            player.y = platform.bottom 

    if player.colliderect(ground):
        player.y += 0
    else:
        player.y += 5
    
    screen.fill((0,0,0))
    pygame.draw.rect(screen, blue, player)
    pygame.draw.rect(screen, brown, platform)
    pygame.draw.rect(screen, brown, ground)

    pygame.display.flip()

pygame.quit()
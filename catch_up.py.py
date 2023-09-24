import pygame

window = pygame.display.set_mode( (700,500) )

background = pygame.transform.scale(
    pygame.image.load("background.png") ,
    (700,500)
)


window.blit(background, (0,0))

FPS = 60
clock = pygame.time.Clock()

sprite1 = pygame.transform.scale(
    pygame.image.load("sprite1.png"),
    (100,100)
)
sprite2 = pygame.transform.scale(
    pygame.image.load("sprite2.png"),
    (100,100)
)

x1, y1 = 100,100

x2, y2 = 200,200

game_over = False
while not game_over:
    window.blit(background, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_UP] and y1 > 5:
        y1 -= 5
    elif keys_pressed[pygame.K_DOWN] and y1 < 395:
        y1 += 5
    elif keys_pressed[pygame.K_RIGHT] and x1 < 595:
        x1 += 5
    elif keys_pressed[pygame.K_LEFT] and x1 > 5:
        x1 -= 5

    if keys_pressed[pygame.K_w] and y2 > 5:
        y2 -= 5
    elif keys_pressed[pygame.K_s] and y2 < 395:
        y2 += 5
    elif keys_pressed[pygame.K_d] and x2 < 595:
        x2 += 5
    elif keys_pressed[pygame.K_a] and x2 > 5:
        x2 -= 5

    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    pygame.display.update()
    clock.tick(FPS)


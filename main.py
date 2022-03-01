import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
icon = pygame.image.load("pong.png")

running = True
while running:
    screen.fill((0, 0, 0))
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

    pygame.display.update()
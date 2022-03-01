import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 750))
icon = pygame.image.load("pong.png")
pygame.display.set_icon(icon)
line = pygame.image.load("line.PNG")
lineX = 494
lineY = 20
score_left = 0
scoreL = pygame.font.Font("freesansbold.ttf", 32)
scoreLX = 450
scoreY = 20
scoreRX = 535
score_right = 0
scoreR = pygame.font.Font("freesansbold.ttf", 32)

playerImg = pygame.image.load("player1.PNG")
player1X = 20
player1Y = 450
player1Y_change = 0
player2X = 980
player2Y = 450
player2Y_change = 0


def show_score(x1, y, x2):
    left_score = scoreL.render(str(score_left), True, (255, 255, 255))
    screen.blit(left_score, (x1, y))
    right_score = scoreR.render(str(score_right), True, (255, 255, 255))
    screen.blit(right_score, (x2, y))


def make_line(x, y):
    for i in range(1, 10):
        screen.blit(line, (x, y))
        y += 100


def player(x1, y1, x2, y2):
    screen.blit(playerImg, (x1, y1))
    screen.blit(playerImg, (x2, y2))


running = True
while running:
    screen.fill((0, 0, 0))
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_w:
                player1Y_change = -0.5
            if ev.key == pygame.K_s:
                player1Y_change = 0.5
            if ev.key == pygame.K_UP:
                player2Y_change = -0.5
            if ev.key == pygame.K_DOWN:
                player2Y_change = 0.5
        if ev.type == pygame.KEYUP:
            if ev.key == pygame.K_s or ev.key == pygame.K_w:
                player1Y_change = 0
            if ev.key == pygame.K_UP or ev.key == pygame.K_DOWN:
                player2Y_change = 0

    player1Y += player1Y_change
    player2Y += player2Y_change

    if player1Y <= 0:
        player1Y = 0
    elif player1Y >= 650:
        player1Y = 650
    if player2Y <= 0:
        player2Y = 0
    elif player2Y >= 650:
        player2Y = 650

    player(player1X, player1Y, player2X, player2Y)
    show_score(scoreLX, scoreY, scoreRX)
    make_line(lineX, lineY)
    pygame.display.update()

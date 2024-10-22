import pygame
from paddle import Paddle
from ball import Ball


width = 640 # largura da tela
height = 480 # altura da tela

BACKGROUND_COLOR = (229, 229, 229)


x_p1 = 10
y_p1 = 190
score_p1 = 0

x_p2 = 606
y_p2 = 190
score_p2 = 0

y_speed = 10

radius = 15
x_ball = int(width/2)
y_ball = int(height/2)
x_ball_speed = 3
y_ball_speed = 3

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # if event.type == pygame.KEYDOWN: #or event.type == pygame.KEYUP:
    #     if event.key == pygame.K_w:
    #         y_p1 -= y_speed
    #     if event.key == pygame.K_s:
    #         y_p1 += y_speed
        
    #     if event.key == pygame.K_UP:
    #         y_p2 -= y_speed
    #     if event.key == pygame.K_DOWN:
    #         y_p2 += y_speed
    
    if keys[pygame.K_w]:
        y_p1 -= y_speed
    if keys[pygame.K_s]:
        y_p1 += y_speed

    if keys[pygame.K_UP]:
        y_p2 -= y_speed
    if keys[pygame.K_DOWN]:
        y_p2 += y_speed

    player_1 = Paddle(screen, x_p1, y_p1)
    player_2 = Paddle(screen, x_p2, y_p2)
    ball = Ball(screen, x_ball, y_ball, radius)

    x_ball += x_ball_speed
    y_ball += y_ball_speed

    if pygame.Rect.colliderect(ball.getRect(), player_1.getRect()): 
        x_ball_speed *= -1
        x_ball = player_1.initial_x + 24 + radius
    if pygame.Rect.colliderect(ball.getRect(), player_2.getRect()): 
        x_ball_speed *= -1
        x_ball = player_2.initial_x - radius

    # if x_ball >= x_p2 - radius or x_ball <= x_p1 + 24 + radius: 
    #     x_ball_speed *= -1 

    if y_ball >= height - radius or y_ball <= radius:
        y_ball_speed *= -1
    if x_ball >= width - radius:
        x_ball_speed *= -1
        score_p1 += 1
        print("score_p1", score_p1, "|", "score_p2", score_p2)
    elif x_ball <= radius:
        x_ball_speed *= -1
        score_p2 += 1
        print("score_p1", score_p1, "|", "score_p2", score_p2)
    
    screen.fill(BACKGROUND_COLOR)
    player_1.draw()
    player_2.draw()
    ball.draw()
    #pygame.draw.rect(screen, PADDLE_COLOR, pygame.Rect(10, y_p1, 24, 100))
    #pygame.draw.rect(screen, PADDLE_COLOR, pygame.Rect(606, y_p2, 24, 100))
    #pygame.draw.circle(screen, BALL_COLOR, (x_ball, y_ball), radius)

    font = pygame.font.SysFont(None, 25)
    text = font.render("Player 1: "+ str(score_p1) + " | " + "Player 2: " + str(score_p2), True, (0,0,0))
    screen.blit(text,(0,0))

    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
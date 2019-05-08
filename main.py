import pygame
from pong import *
from enum import Enum
import random

# Window Settings
FPS = 120
WIDTH = 700
HEIGHT = 800
TITLE = 'Pong'

game_run = True
screen_size = WIDTH , HEIGHT

pygame.init()
game_display = pygame.display.set_mode(screen_size)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# Game Settings
paddle_speed = 5
paddle_size = (200, 25)

ball_speed = 3
ball_rotation = 0
ball_size = (25,25)

#====== Game Loop ==

player = Paddle(game_display, 100, 700, paddle_size[0], paddle_size[1])
x, y = player.x, player.y

ball = Ball(game_display, WIDTH/2, HEIGHT/2, ball_size[0], ball_size[1], down = True)
ball_x, ball_y = ball.x, ball.y

while game_run:
    # Event Loop
    # Quit Event X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
        # KeyDown Events
        if event.type == pygame.KEYDOWN:
            # a or left arrow
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.left = True
            # d or right arrow
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.right = True
        # KeyUp Events
        if event.type == pygame.KEYUP:
            # a or left arrow
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.left = False
            # d or right arrow
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.right = False
                
    # get key state from Events Loop and move paddle accordlingly
    if player.left: x -= paddle_speed
    if player.right: x += paddle_speed
    # ball movement
    if not ball.right:
        ball_x -= ball_speed # replace with rand rotation that clamped
    if ball.right:
        ball_x += ball_speed
    if not ball.down:
        ball_y -= ball_speed
    if ball.down:
        ball_y += ball_speed
    
    # collision
    # player paddle with screen
    if x > WIDTH - player.width:
        x = WIDTH - player.width
    if x < 0:
        x = 0
        
    # ball with screen
    if ball_x > WIDTH - ball.width:
        ball_x = WIDTH - ball.width
        ball.right = False
    if ball_x < 0:
        ball_x = 0
        ball.right = True
    if ball_y > HEIGHT - ball.height:
        ball_y = HEIGHT - ball.height
        ball.down = False
    if ball_y < 0:
        ball_y = 0
        ball.down = True
        
    # ball with paddle
    if player.rect_data.colliderect(ball.rect_data):
        ball.down = False
    
    game_display.fill( (0,0,0) )
    
    player.move(x, y)
    player.draw()

    ball.move(ball_x, ball_y)
    ball.draw()
    
    
    # Updates frame
    pygame.display.update()
    clock.tick(FPS)

#==================
    
pygame.display.quit()
pygame.quit()
quit()

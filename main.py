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

player = Paddle(game_display, 100, 700, paddle_size[0], paddle_size[1], paddle_speed)
x, y = player.x, player.y

ball = Ball(game_display, WIDTH/2, HEIGHT/2, ball_size[0], ball_size[1], down = True, speed=ball_speed)
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
    if player.left and x > 0: x -= player.speed
    if player.right and x + player.width < WIDTH : x += player.speed
    # ball movement # replace with rand rotation that clamped
    if not ball.right: ball_x -= ball.speed
    if ball.right: ball_x += ball.speed
    if not ball.down: ball_y -= ball.speed
    if ball.down: ball_y += ball.speed
        
    game_display.fill( (0,0,0) )

    player.move(x, y)
    player.is_collide()
    player.draw()

    ball.move(ball_x, ball_y)
    ball.is_collide(player.rect_data, 0)
    ball.draw()
    
    # Updates frame
    pygame.display.update()
    clock.tick(FPS)

#==================
    
pygame.display.quit()
pygame.quit()
quit()

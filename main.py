import pygame
from pong import *
from enum import Enum

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
left, right, up, down = False, False, False, False

ball_size = (25,25)

#====== Game Loop ==

player = Paddle(game_display, 100, 700, paddle_size[0], paddle_size[1])
x, y = player.x, player.y

ball = Ball(game_display, WIDTH/2, HEIGHT/2, ball_size[0], ball_size[1])
ball_dir = 0

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
                left = True
            # d or right arrow
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                right = True
        # KeyUp Events
        if event.type == pygame.KEYUP:
            # a or left arrow
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                left = False
            # d or right arrow
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                right = False
    # get key state from Events Loop and move paddle accordlingly
    if left: x -= paddle_speed
    if right: x += paddle_speed
    
    # collision
    # player paddle with screen
    if x > WIDTH - player.width:
        x = WIDTH - player.width
    if x < 0:
        x = 0
    # ball with screen

    # ball with paddle
     
    
    
    game_display.fill( (0,0,0) )
    player.move(x, y)
    player.draw()

    ball.draw()
    
    # Updates frame
    pygame.display.update()
    clock.tick(FPS)

#==================
    
pygame.display.quit()
pygame.quit()
quit()

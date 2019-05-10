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

ball_speed = 10
ball_rotation = 0
ball_size = (25,25)

#====== Game Loop ==

player = Paddle(game_display, 100, 700, paddle_size[0], paddle_size[1], speed=paddle_speed)
x, y = player.x, player.y

ball = Ball(game_display, WIDTH/2, HEIGHT/2, ball_size[0], ball_size[1], down = True, speed=ball_speed)
ball_x, ball_y = ball.x, ball.y

ai = AI_Paddle(game_display, 100, 75, paddle_size[0], paddle_size[1], speed=paddle_speed)
ai_x, ai_y = ai.x, ai.y

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
    if not ball.right: ball_x -= ball.dir_x
    if ball.right: ball_x += ball.dir_x
    if not ball.down: ball_y -= ball.dir_y
    if ball.down: ball_y += ball.dir_y
    # AI movement
    ai.track_ball(ball_x)
    if ai.left and ai_x > 0: ai_x -= ai.speed
    if ai.right and ai_x + ai.width < WIDTH : ai_x += player.speed

        
    game_display.fill( (0,0,0) )

    player.move(x, y)
    player.is_collide()
    player.draw()

    ball.move(ball_x, ball_y)
    win = ball.is_collide(player.rect_data, ai.rect_data)
    ball.draw()

    ai.move(ai_x, ai_y)
    ai.is_collide()
    ai.draw()

    if win != None:
        if win:
            text(game_display, "You Win!")
            pygame.time.wait(3000)
            game_run = False
        if not win:
            text(game_display, "You Lose")
            pygame.time.wait(3000)
            game_run = False
    
    # Updates frame
    pygame.display.update()
    clock.tick(FPS)

#==================
    
pygame.display.quit()
pygame.quit()
quit()

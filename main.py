import pygame
from pong import *

FPS = 120
WIDTH = 800
HEIGHT = 600

game_run = True
screen_size = WIDTH , HEIGHT

pygame.init()
game_display = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Pong Clone')
clock = pygame.time.Clock()

paddle_speed = 10

#====== Game Loop ==

player = Paddle(game_display, 100, 100, 100, 100)
x, y

while game_run:
    # Event Loop
    # Quit Event X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
        # KeyDown Events
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                x = player.x - player_speed
                player.move(x, player.y)
            if event.type == pygame.K_RIGHT:
                x = player.x + player_speed
                player.move(x , player.y)
        
    game_display.fill( (0,0,0) )

    player.draw()
    
    # Updates frame
    pygame.display.update()
    clock.tick(FPS)

#==================
    
pygame.display.quit()
pygame.quit()
quit()

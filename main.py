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

#====== Game Loop ==

paddle1 = Paddle(game_display, 100, 100, 100, 100)

while game_run:
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
        
    game_display.fill( (0,0,0) )

    paddle1.draw()
    paddle1.move(500,500)
    
    # Updates frame
    pygame.display.update()
    clock.tick(FPS)

#==================
    
pygame.display.quit()
pygame.quit()
quit()

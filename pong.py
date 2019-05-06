import pygame

class Paddle:
    def __init__(self, screen, x, y, w, h, color = (255,255,255) ):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.color = color
        
        self.rect_data = pygame.Rect(self.x,self.y,self.width,self.height)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect_data)
        
    def move(self, x, y):
        self.rect_data.x = x
        self.rect_data.y  = y
        

import pygame

class Paddle:
    def __init__(self, screen, x, y, w, h, color = (255,255,255),left=False,right=False, speed=5 ):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.color = color
        self.left = left
        self.right = right
        self.speed = speed
        self.scr_WIDTH, self.scr_HEIGHT = pygame.display.get_surface().get_size()
        self.rect_data = pygame.Rect(self.x,self.y,self.width,self.height)
        
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect_data)
        
    def move(self, x, y):
        self.rect_data.x = x
        self.rect_data.y  = y

    def is_collide(self):
        # paddle with screen
        if self.x > self.scr_WIDTH - self.width:
            self.x = self.scr_WIDTH - self.width
            return True
        if self.x < 0:
            self.x = 0
            return True
        return False
    
class Ball(Paddle):
    def __init__(self, screen, x, y, w, h, color = (255,255,255),left=False,right=False,up=False,down=False, speed=3):
        Paddle.__init__(self, screen, x, y, w, h, color, left, right, speed)
        self.up = up
        self.down = down
        
    def move(self, x, y):
        self.rect_data.x = x
        self.rect_data.y  = y

    def is_collide(self, player_rect_data, AI_rect_data):
        # ball with screen
        if self.rect_data.x > self.scr_WIDTH - self.width:
            self.rect_data.x = self.scr_WIDTH - self.width
            self.right = False
        if self.rect_data.x < 0:
            self.rect_data.x = 0
            self.right = True
        if self.rect_data.y > self.scr_HEIGHT - self.height:
            self.rect_data.y = self.scr_HEIGHT - self.height
            self.down = False
        if self.rect_data.y < 0:
            self.rect_data.y = 0
            self.down = True

        # ball with paddle
        if player_rect_data.colliderect(self.rect_data):
            self.down = False
    
class AI_Paddle(Paddle):
    def __init__(self, screen, x, y, w, h, color = (255,255,255),left=False,right=False):
        Paddle.__init__(self, screen, x, y, w, h, color,left,right)
        

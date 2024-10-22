import pygame
 
class Paddle:
    def __init__(self, screen, initial_x, initial_y):
        self.color = (20, 33, 61)
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.screen = screen
        

    def draw(self):
        return pygame.draw.rect(self.screen, self.color, pygame.Rect(self.initial_x, self.initial_y, 24, 100))
    
    def getRect(self):
        return self.draw()
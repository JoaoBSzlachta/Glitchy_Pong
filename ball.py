import pygame
 
class Ball:
    def __init__(self, screen, initial_x, initial_y, radius):
        self.screen = screen 
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.radius = radius
        self.color = (252, 163, 17)
    
    def draw(self):
        return  pygame.draw.circle(self.screen, self.color, (self.initial_x, self.initial_y), self.radius)

    def getRect(self):
        return self.draw()
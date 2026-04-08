#Import + Initialize Libraries
import pygame
pygame.init()

#Generic Object Class
class Object:
    def __init__(self, screen, x, y, width, height, colour, backgroundColour, Text):
        #Screen/Drawing-location
        self.screen = screen
        #Object position
        self.x = x
        self.y = y
        #object size
        self.w = width
        self.h = height
        #object colours
        self.c = colour
        self.bc = backgroundColour
        #Text font
        self.font = pygame.font.SysFont("Arial", self.h)
        self.text = Text
    def update(self):
        #Used by subclasses
        return

#Rectangle Object Class
class Rectangle(Object):
    def update(self):
        #Draw rectangle
        self.rect = pygame.rect.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(self.screen, self.bc, self.rect)

class Text(Object):
    def update(self):
        #Render + Draw text
        self.render = self.font.render(self.text, True, self.c, self.bc)
        self.TextRect = self.render.get_rect(center=(self.x, self.y))
        self.screen.blit(self.render, self.TextRect)
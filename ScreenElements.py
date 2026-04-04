#Import + Initialize Libraries
import pygame
pygame.init()

#Generic Object Class
class Object:
    def __init__(self, screen, x, y, width, height, colour, backgroundColour):
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
    def update(self):
        #Used by subclasses
        return

#Rectangle Object Class
class Rectangle(Object):
    def update(self):
        #Draw rectangle
        self.rect = pygame.rect.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(self.screen, self.bc, self.rect)
#This file is for the rendering of the unique rides and fuel stations
#Import libraries
import pygame
pygame.init()
from ScreenElements import Rectangle
from ScreenElements import Text
from RideData import Ride_data
class Attraction:
    def __init__(self, screen, name, backgroundcolor, width, height, x, y):
        self.screen = screen
        self.name = name
        self.backgroundcolor = backgroundcolor
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.font = pygame.font.Font(None, 30)
        self.rect = Rectangle(self.screen, None, None, None, self.x, self.y, self.width, self.height, 0, None, self.backgroundcolor, None, None)
    def update(self, time):
        self.rect.update()
        self.render = self.font.render(self.name, True, [0, 0, 0], None)
        self.screen.blit(self.render, self.render.get_rect(center=(self.x + self.width/2, self.y + self.height/2)))
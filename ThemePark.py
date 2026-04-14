#This file is for the rendering of the unique rides and fuel stations
#Import libraries
import pygame
pygame.init()
from ScreenElements import Rectangle
from ScreenElements import Text
from RideData import Ride_data
class Attraction:
    def __init__(self, screen, name, backgroundcolor, width, height, x, y, type):
        self.screen = screen
        self.name = name
        self.backgroundcolor = backgroundcolor
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.type = type
        self.visible = False
        self.font = pygame.font.Font(None, 30)
        self.rect = Rectangle(self.screen, None, None, None, self.x, self.y, self.width, self.height, 0, None, self.backgroundcolor, None, None)
        self.waitTime = 0
        self.satisfaction = 75
        self.itemsSold = 20
        self.sales = 100
        self.fixed = False
    def alert(self):
        pass
    def update(self, time):
        if self.type == "Ride":
            self.waitTime = Ride_data[time][self.name]["wait"]
            self.satisfaction = Ride_data[time][self.name]["satisfaction"]
        if self.type == "Concession":
            pass
        self.rect.update()
        self.render = self.font.render(self.name, True, [0, 0, 0], None)
        self.screen.blit(self.render, self.render.get_rect(center=(self.x + self.width/2, self.y + self.height/2)))
        if self.type == "Ride" and not self.fixed:
            if self.waitTime > 30 or self.satisfaction < 75:
                self.alert()
        elif self.type == "Concession" and not self.fixed:
            if self.itemsSold < 20:
                self.alert()
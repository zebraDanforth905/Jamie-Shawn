#This file is for the rendering of the unique rides and fuel stations
#Import libraries
import pygame
pygame.init()
from ScreenElements import Rectangle
from ScreenElements import Text
from RideData import Ride_data
from RideData import CONCESSIONS
class Attraction:
    def __init__(self, screen, name, backgroundcolor, width, height, x, y, type):
        #Define Attributes
        self.screen = screen
        self.name = name
        self.backgroundcolor = backgroundcolor
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.type = type
        self.visible = False
        self.font = pygame.font.Font(None, round(self.width/5))
        self.rect = Rectangle(self.screen, True, "Fix", None, self.x, self.y, self.width, self.height, 0, None, self.backgroundcolor, None, None)

        if self.type == 'Ride':
            self.waitTime = Ride_data[0][self.name]["wait"]
            self.satisfaction = Ride_data[0][self.name]["satisfaction"]
        elif self.type == "Concession":
            self.itemsSold = CONCESSIONS[0][self.name]["items"]
            self.sales = CONCESSIONS[0][self.name]["sales"]
        self.fixed = False
        self.OnFix = False
        self.alerting = False
        self.alertImage = pygame.image.load("warningSign.png")
        self.alertImage = pygame.transform.scale(self.alertImage, (75, 75))
        self.alertImageRect = pygame.rect.Rect(self.x, self.y, 75, 75)
        self.timeOfAlert = 1000
    def update(self, time):
        if self.type == "Ride":
            self.waitTime = Ride_data[time][self.name]["wait"]
            self.satisfaction = Ride_data[time][self.name]["satisfaction"]
        elif self.type == "Concession":
            self.itemsSold = CONCESSIONS[time][self.name]["items"]
            self.sales = CONCESSIONS[time][self.name]["sales"]
        
        self.OnFix = self.rect.update()
        
        if self.OnFix == True and self.alerting == True:
            self.alerting = False
            self.fixed = True

        if time != self.timeOfAlert:
            self.fixed = False

        if self.alerting:
            self.screen.blit(self.alertImage, self.alertImageRect)
        self.render = self.font.render(self.name, True, [0, 0, 0], None)
        self.screen.blit(self.render, self.render.get_rect(center=(self.x + self.width/2, self.y + self.height/2)))
        if self.type == "Ride" and not self.fixed:
            if self.waitTime > 30 or self.satisfaction < 75:
                self.alerting = True
                self.timeOfAlert = time
        elif self.type == "Concession" and not self.fixed:
            if self.itemsSold < 20:
                self.alerting = True
                self.timeOfAlert = time
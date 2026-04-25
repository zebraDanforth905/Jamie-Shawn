#This file is for the rendering of the unique rides and fuel stations
#Import libraries
import pygame
pygame.init()
from ScreenElements import Rectangle
from ScreenElements import Text
from RideData import Ride_Data
from RideData import Concessions
class Attraction:
    def __init__(self, screen, name, backgroundcolor, width, height, x, y, type):
        self.screen = screen
        #Define size + coords
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        #Define Attributes
        self.name = name
        self.type = type
        self.visible = False
        self.backgroundcolor = backgroundcolor
        #Define visible components
        self.font = pygame.font.Font(None, round(self.width/6 - len(self.name)/5))
        self.statsFont = pygame.font.Font(None, round(self.width/7))
        self.rect = Rectangle(self.screen, True, "Fix", None, self.x, self.y, self.width, self.height, 0, None, self.backgroundcolor, None, None)
        #Set starting values
        if self.type == 'Ride':
            self.waitTime = Ride_Data[0][self.name]["wait"]
            self.satisfaction = Ride_Data[0][self.name]["satisfaction"]
        elif self.type == "Concession":
            self.itemsSold = Concessions[0][self.name]["items"]
            self.sales = Concessions[0][self.name]["sales"]
        #Define alert system vars
        self.fixed = False
        self.OnFix = False
        self.alerting = False
        self.alertImage = pygame.image.load("warningSign.png")
        self.alertImage = pygame.transform.scale(self.alertImage, (75, 75))
        self.alertImageRect = pygame.rect.Rect(self.x, self.y-30, 75, 75)
        self.timeOfAlert = 1000
    def update(self, time):
        #Change values
        if self.type == "Ride":
            self.waitTime = Ride_Data[time][self.name]["wait"]
            self.satisfaction = Ride_Data[time][self.name]["satisfaction"]
        elif self.type == "Concession":
            self.itemsSold = Concessions[time][self.name]["items"]
            self.sales = Concessions[time][self.name]["sales"]
        
        #Render rect + Check for fixes + sustain fixes
        self.OnFix = self.rect.update()
        if self.OnFix == True and self.alerting == True:
            self.alerting = False
            self.fixed = True
        if time != self.timeOfAlert:
            self.fixed = False

        #display alert image
        if self.alerting:
            self.screen.blit(self.alertImage, self.alertImageRect)
        #Render text
        self.render = self.font.render(self.name, True, [0, 0, 0], None)
        if self.type == 'Ride':
            self.renderWaitTime = self.statsFont.render(f"Wait Time: {self.waitTime}m", True, [0,0,0], None)
            self.renderLikability = self.statsFont.render(f"Satisfaction: {self.satisfaction}%", True, [0,0,0], None)
            self.screen.blit(self.renderWaitTime, self.render.get_rect(center=(self.x + self.width/2, self.y + self.height/2 + 21)))
            self.screen.blit(self.renderLikability, self.render.get_rect(center=(self.x + self.width/2, self.y + self.height/2 + 42)))
        elif self.type == "Concession":
            self.renderitemsSold = self.statsFont.render(f"Items Sold: {self.itemsSold}", True, [0,0,0], None)
            self.renderSales = self.statsFont.render(f"Sales: ${self.sales}", True, [0,0,0], None)
            self.screen.blit(self.renderitemsSold, self.render.get_rect(center=(self.x + self.width/2, self.y + self.height/2 + 21)))
            self.screen.blit(self.renderSales, self.render.get_rect(center=(self.x + self.width/2, self.y + self.height/2 + 42)))
        self.screen.blit(self.render, self.render.get_rect(center=(self.x + self.width/2, self.y + self.height/2)))
        #Check for any alerts
        if self.type == "Ride" and not self.fixed:
            if self.waitTime > 30 or self.satisfaction < 75:
                self.alerting = True
                self.timeOfAlert = time
        elif self.type == "Concession" and not self.fixed:
            if self.itemsSold < 20:
                self.alerting = True
                self.timeOfAlert = time
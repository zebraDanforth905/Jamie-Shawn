#i dont want to destroy the main file so i created a test file

import pygame
import random


pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]
BLUE = [0, 0, 255]
BACKGROUNDCOLOUR = [115, 147, 179]

speed = 1



class PathfindingCharacter:
    def __init__(self, color):
        self.x = random.randint(170, 470)
        self.y = random.randint(150, 200)
        self.x_destination = self.x
        self.y_destination = self.y
        self.currently_moving_to_attraction = False
        self.currently_moving_to_corner = False
        self.moving = False
        self.radius = 4
        self.color = color
        self.clone_yourself = False
        self.path = []
        self.quadrantOrder = ["Top-Left", "Bottom-Left", "Bottom-Right", "Top-Right"]
    
    def draw_circle(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    
    def find_attraction_to_goto(self, data, locations):
        pass

    def get_quadrant(self, x=0, y=0):
        if x <= 640 and y >= 360:
            return "Bottom-Left"
        elif x > 640 and y >= 360:
            return "Bottom-Right"
        elif x <= 640 and y < 360:
            return "Top-Left"
        elif x > 640 and y < 360:
            return "Top-Right"

    def moveToQuadrant(self, quadrant="Bottom-Left"):
        if quadrant == "Bottom-Left":
            self.x_destination = random.randint(170, 470)
            self.y_destination = random.randint(530, 560)
        elif quadrant == "Bottom-Right":
            self.x_destination = random.randint(710, 1120)
            self.y_destination = random.randint(530, 560)
        elif quadrant == "Top-Right":
            self.x_destination = random.randint(710, 1120)
            self.y_destination = random.randint(150, 200)
        elif quadrant == "Top-Left":
            self.x_destination = random.randint(170, 470)
            self.y_destination = random.randint(150, 200)
    
    def move(self):
        self.moving = True
        if self.x < self.x_destination:
            self.x += 1
        elif self.x > self.x_destination:
            self.x -= 1
        if self.y < self.y_destination:
            self.y += 1
        elif self.y > self.y_destination:
            self.y -= 1
        
        if self.x >= self.x_destination-1 and self.x <= self.x_destination+1 and self.y >= self.y_destination-1 and self.y <= self.y_destination+1:
            if len(self.path) == 1:
                self.x_destination = self.path[0].entrance[0]
                self.y_destination = self.path[0].entrance[1]
                if self.x >= self.x_destination-1 and self.x <= self.x_destination+1 and self.y >= self.y_destination-1 and self.y <= self.y_destination+1:
                    self.x = self.path[0].rect.rect.centerx
                    self.y = self.path[0].rect.rect.centery
                    self.x_destination = self.path[0].exit[0]
                    self.y_destination = self.path[0].exit[1]
                    self.path.pop(0)
            elif len(self.path) > 1:
                self.moveToQuadrant(self.path[0])
                self.path.pop(0)
            else:
                self.moving = False
                

    def get_path(self, destination):
        self.path = []
        #Top left = 0, Bottom left = 1, Bottom right = 2, top right = 3
        currentQuadrant = self.get_quadrant(self.x, self.y)
        currentQuadrantNum = self.quadrantOrder.index(currentQuadrant)
        finalQuadrant = self.quadrantOrder.index(self.get_quadrant(destination.x, destination.y))
        if currentQuadrantNum + 1 < finalQuadrant:
            for i in range(currentQuadrantNum, finalQuadrant+1):
                self.path.append(self.quadrantOrder[i])
        elif currentQuadrantNum + 1 > finalQuadrant:
            for i in range(currentQuadrantNum, finalQuadrant-1, -1):
                self.path.append(self.quadrantOrder[i])
        self.path.append(destination)

        self.moveToQuadrant(self.path[0])
        self.path.pop(0)
        self.moving = True
        return self.path
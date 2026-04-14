#Import + Initialize Libraries
import pygame
pygame.init()
pygame.font.init()

#Generic Object Class
class Object:
    def __init__(self, screen, clickable, clickingType, x, y, width, height, borderWidth, colour, backgroundColour, Font, Text):
        #Screen/Drawing-location
        self.screen = screen
        #Object position
        self.x = x
        self.y = y
        #object size
        self.w = width
        self.h = height
        self.bw = borderWidth
        #object colours
        self.c = colour
        self.bc = backgroundColour
        #Text font
        self.font = pygame.font.Font(None, self.h)
        self.text = Text
        #Attributes
        self.clickable = clickable
        self.clicking = False
        self.clickingType = clickingType
    def update(self):
        #Used by subclasses
        return
    def click(self, hitBox):
        #Get User Mouse
        mouse = pygame.mouse
        #Check if clicking
        if hitBox.collidepoint(mouse.get_pos()) and self.clicking:
            #Output Desired Result
            print(True)
            if self.clickingType == None:
                pass

#Rectangle Object Class
class Rectangle(Object):
    def update(self):
        #Draw rectangle
        self.rect = pygame.rect.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(self.screen, self.bc, self.rect, self.bw)
        if self.clickable:
            self.click(self.rect)
        self.clicking = False

class Text(Object):
    def update(self):
        #Render + Draw text
        self.render = self.font.render(self.text, True, self.c, self.bc)
        self.TextRect = self.render.get_rect(center=(self.x, self.y))
        self.screen.blit(self.render, self.TextRect)
        if self.clickable:
            self.click(self.TextRect)
        self.clicking = False
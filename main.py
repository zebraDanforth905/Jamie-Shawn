#Import + Initialize Libraries
import pygame
pygame.init()
from ScreenElements import Rectangle
from ScreenElements import Text

#Set FPS
Clock = pygame.time.Clock()
FPS = 60

#Set screen dimensions + game title
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ride Rush")

#Define colours
WHITE = [255,255,255]
RED = [255,0,0]
GREEN = [0,255,0]
BLUE = [0,0,255]
BLACK = [0,0,0]
YELLOW = [255,255,0]
PURPLE = [255,0,255]
ORANGE = [255,180,0]
BACKGROUNDCOLOUR = [115, 147, 179]

#Define the different screens/visual-segments of the game
MenuScreen = []

SettingsScreen = []

SimulationScreen = []

#Define the screen currently being displayed
CurrentScreen = MenuScreen

#Game loop
isRunning = True
while isRunning:
    #Render objects
    screen.fill(BACKGROUNDCOLOUR)
    for obj in CurrentScreen:
        obj.update()
    #Get quit input + others
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isRunning = False
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            # print(pygame.mouse.get_pos())
            if ev.button == 1:
                for obj in CurrentScreen:
                    obj.clicking = True
    
    #Display frame
    pygame.display.update()
    Clock.tick(FPS)

#Exit the game
pygame.quit()
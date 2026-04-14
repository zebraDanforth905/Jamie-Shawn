#Import + Initialize Libraries
import pygame
pygame.init()
from ScreenElements import Rectangle
from ScreenElements import Text
from RideData import Ride_data

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
PURPLE = [155,0,155]
ORANGE = [255,180,0]
BACKGROUNDCOLOUR = [115, 147, 179]
MENUBUTTONCOLOUR = [178, 0, 0]

#Define the different screens/visual-segments of the game
#Menu
Title = Text(screen, False, None, WIDTH/2, 100, None, 80, None,  BLACK, None, "comic sans ms", "Ride Rush")
PlayButton = Rectangle(screen, True, None, WIDTH/2 - 195, 300, 400, 100, 0, None, MENUBUTTONCOLOUR, None, None)
PlayText = Text(screen, False, None, WIDTH/2, 350, None, 100, 0, BLACK, None, None, "Play")

MenuScreen = [Title, PlayButton, PlayText]

SettingsScreen = []

SimulationScreen = []

#Define the screen currently being displayed
CurrentScreen = MenuScreen

#Define hour system
currentHour = 0
FinalHour = 11
secondsPerHour = 10
HourTimer = 0

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
            print(pygame.mouse.get_pos())
            if ev.button == 1:
                #Check if left-clicking + alert every object in the current screen that the user is clicking
                for obj in CurrentScreen:
                    obj.clicking = True
    
    #Display frame
    pygame.display.update()
    Clock.tick(FPS)
    #Update Hour Simulation
    #if statement Goes here:
    HourTimer += Clock.get_time()/1000
    #print(HourTimer)
    if HourTimer >= secondsPerHour:
        HourTimer = 0
        currentHour += 1
    #Note: The code above is unfinished

#Exit the game
pygame.quit()
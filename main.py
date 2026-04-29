#Import + Initialize Libraries
import pygame
pygame.init()
from ScreenElements import Rectangle
from ScreenElements import Text
from ThemePark import Attraction

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
LIGHTBLUE = [173, 216, 230]
BLACK = [0,0,0]
GREY = [142,142,142]
DARKGREY = [100, 100, 100]
YELLOW = [255,255,0]
PURPLE = [155,0,155]
MAGENTA = [255,0,255]
PINK = [222, 49, 99]
ORANGE = [255,180,0]
BACKGROUNDCOLOUR = [115, 147, 179]
MENUBUTTONCOLOUR = [178, 0, 0]

#Define Attractions
MainEntrance = Attraction(screen, "Main Entrance", GREY, 450, 100, 100, 0, "Entrance")
GrandExit = Attraction(screen, "Grand Exit", GREY, 450, 100, 700, 0, "Exit")
NebulaSpinner = Attraction(screen, "Nebula Spinner", PURPLE, 100, 200, 10, 110, "Ride")
RocketSlingshot = Attraction(screen, "Rocket Slingshot", GREEN, 100, 200, 10, 328, "Ride")
TitanCoaster = Attraction(screen, "Titan Coaster", RED, 140, 150, 558, 110, "Ride")
PixelArcade = Attraction(screen, "Pixel Arcade", MAGENTA, 140, 150, 558, 278, "Ride")
SplashingMountain = Attraction(screen, "Splashing Mountain", BLUE, 100, 200, 1175, 105, "Ride")
LazyRiver = Attraction(screen, "Lazy River", LIGHTBLUE, 100, 200, 1175, 328, "Ride")
QuantumCafe = Attraction(screen, "Quantum Cafe", PURPLE, 230, 95, 107, 546, "Concession")
PixelPopcorn = Attraction(screen, "Pixel Popcorn", PINK, 230, 95, 355, 546, "Concession")
SugarShack = Attraction(screen, "The Sugar Shack", WHITE, 230, 95, 660, 546, "Concession")
HydrationStation = Attraction(screen, "Hydration Station", BLUE, 230, 95, 935, 546, "Concession")
Attractions = [NebulaSpinner, QuantumCafe, MainEntrance, GrandExit, RocketSlingshot, TitanCoaster, PixelArcade, PixelPopcorn, SplashingMountain, LazyRiver, SugarShack, HydrationStation]

#Define the different screens/visual-segments of the game

SettingsScreen = []

simulationClock = Text(screen, False, None, None, WIDTH/2 - 20, 30, 0, 30, 0, BLACK, None, "comic sans ms", "10:00")
OpenSign = Rectangle(screen, None, None, None, WIDTH/2 - 50, 40, 60, 30, 0, None, GREEN, None, None)
OpenSignText = Text(screen, None, None, None, WIDTH/2 - 20, 55, 0, 20, 0, WHITE, None, None, "Open")

ExitToMenuText = Text(screen, None, None, None, 1230, 31, 60, 20, 0, BLACK, None, None, "Exit")
ConfirmBackground = Rectangle(screen, None, None, None, 707, 111, 450, 400, 0, None, DARKGREY, None, None, visible=False)
ExitToMenu = Rectangle(screen, True, "OpenPopup", ConfirmBackground, 1200, 11, 60, 40, 0, None, RED, None, None)
SimulationScreen = [simulationClock, OpenSign, OpenSignText, ExitToMenu, ExitToMenuText, ConfirmBackground]

Title = Text(screen, False, None, None, WIDTH/2, 100, None, 80, None,  BLACK, None, "comic sans ms", "Ride Rush")
PlayButton = Rectangle(screen, True, "Play", SimulationScreen, WIDTH/2 - 195, 300, 400, 100, 0, None, MENUBUTTONCOLOUR, None, None)
PlayText = Text(screen, False, None, None, WIDTH/2, 350, None, 100, 0, BLACK, None, None, "Play")

MenuScreen = [Title, PlayButton, PlayText]

ControlsTitle = Text(screen, False, None, None, WIDTH/2, 100, None, 80, None,  BLACK, None, "comic sans ms", "Controls/Tutorial")
CloseAlerts = Text(screen, False, None, None, WIDTH/2, 300, None, 50, None, BLACK, None, "comic sans ms", "To close alerts, simply left-click on the coloured object holding the alert.")
ContinueButton = Rectangle(screen, True, "Continue", MenuScreen, 800, 550, 400, 100, 0, None, MENUBUTTONCOLOUR, None, None)
ContinueText = Text(screen, None, None, None, 1000, 600, 0, 50, 0, BLACK, None, "comic sans ms", "Continue")
ControlsScreen = [ControlsTitle, CloseAlerts, ContinueButton, ContinueText]

#Define the screen currently being displayed
CurrentScreen = ControlsScreen
InSimulation = False
FinishedSimulation = False

#Define hour system
currentHour = 0
FinalHour = 11
secondsPerHour = 10
HourTimer = 0

#Define sounds
finishSound = pygame.mixer.Sound("FinishSound.mp3")

#Game loop
isRunning = True
while isRunning:
    #Render objects
    screen.fill(BACKGROUNDCOLOUR)
    for obj in CurrentScreen:
        obj.update()
    #Render attractions
    for attraction in Attractions:
        if attraction.visible == True:
            attraction.update(currentHour)
    #Update visual clock display
    simulationClock.text = f"{10+currentHour}:00"
    #Get quit input + click inputs
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isRunning = False
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                print(pygame.mouse.get_pos())
                #Check if left-clicking + alert every object in the current screen that the user is clicking
                for obj in CurrentScreen:
                    obj.clicking = True
                    #SwitchScreens
                    if obj.clickingType == "Play":
                        if(obj.update()):
                            CurrentScreen = SimulationScreen
                            for attraction in Attractions:
                                attraction.visible = True
                            InSimulation = True
                    elif obj.clickingType == "Continue":
                        if(obj.update()):
                            CurrentScreen = MenuScreen
                    elif obj.clickingType == "OpenPopup":
                        if (obj.update()):
                            obj.clickScreen.visible = True
                #Alert attractions that the user is clicking
                for i in Attractions:
                    i.rect.clicking = True
    
    #Display frame
    pygame.display.update()
    Clock.tick(FPS)
    #Update Hour Simulation
    if InSimulation:
        HourTimer += (Clock.get_time()/1000)
    if HourTimer >= secondsPerHour and currentHour < 11:
        HourTimer = 0
        currentHour += 1
    elif currentHour == 11:
        OpenSign.bc = RED
        OpenSignText.text = "Closed"

#Exit the game
pygame.quit()
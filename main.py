#Import + Initialize Libraries
import pygame
pygame.init()
from ScreenElements import Rectangle
from ScreenElements import Text
from RideData import Ride_data
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
NebulaSpinner = Attraction(screen, "Nebula Spinner", PURPLE, 80, 200, 20, 110, "Ride")
RocketSlingshot = Attraction(screen, "Rocket Slingshot", WHITE, 80, 200, 20, 328, "Ride")
TitanCoaster = Attraction(screen, "Titan Coaster", RED, 140, 150, 558, 110, "Ride")
PixelArcade = Attraction(screen, "Pixel Arcade", MAGENTA, 140, 150, 558, 278, "Ride")
SplashingMountain = Attraction(screen, "Splashing Mountain", BLUE, 80, 200, 1165, 105, "Ride")
LazyRiver = Attraction(screen, "Lazy River", LIGHTBLUE, 80, 200, 1165, 328, "Ride")
QuantumCafe = Attraction(screen, "Quantum Cafe", BLUE, 230, 75, 107, 546, "Concession")
PixelPopcorn = Attraction(screen, "Pixel Popcorn", PINK, 230, 75, 355, 546, "Concession")
SugarShack = Attraction(screen, "The Sugar Shack", WHITE, 230, 75, 660, 546, "Concession")
HydrationStation = Attraction(screen, "Hydration Station", BLUE, 230, 75, 935, 546, "Concession")
Attractions = [NebulaSpinner, QuantumCafe, MainEntrance, GrandExit, RocketSlingshot, TitanCoaster, PixelArcade, PixelPopcorn, SplashingMountain, LazyRiver, SugarShack, HydrationStation]

#Define the different screens/visual-segments of the game

SettingsScreen = []

simulationClock = Text(screen, False, None, None, 30, 30, 0, 30, 0, BLACK, None, "comic sans ms", "10:00")
SimulationScreen = [simulationClock]

Title = Text(screen, False, None, None, WIDTH/2, 100, None, 80, None,  BLACK, None, "comic sans ms", "Ride Rush")
PlayButton = Rectangle(screen, True, "Play", SimulationScreen, WIDTH/2 - 195, 300, 400, 100, 0, None, MENUBUTTONCOLOUR, None, None)
PlayText = Text(screen, False, None, None, WIDTH/2, 350, None, 100, 0, BLACK, None, None, "Play")

MenuScreen = [Title, PlayButton, PlayText]

ControlsTitle = Text(screen, False, None, None, WIDTH/2, 100, None, 80, None,  BLACK, None, "comic sans ms", "Controls/Tutorial")
CloseAlerts = Text(screen, False, None, None, WIDTH/2, 300, None, 50, None, BLACK, None, "comic sans ms", "To close alerts, simply left-click on the coloured object holding the alert.")
ContinueButton = Rectangle(screen, True, "Continue", MenuScreen, 800, 550, 400, 100, 0, None, MENUBUTTONCOLOUR, None, None)
ControlsScreen = [ControlsTitle, CloseAlerts, ContinueButton]

#Define the screen currently being displayed
CurrentScreen = ControlsScreen
InSimulation = False

#Define hour system
currentHour = 0
FinalHour = 11
secondsPerHour = 0.5
HourTimer = 0

finishSound = pygame.mixer.Sound("FinishSound.mp3")

#Game loop
isRunning = True
while isRunning:
    #Render objects
    screen.fill(BACKGROUNDCOLOUR)
    for obj in CurrentScreen:
        obj.update()
    for attraction in Attractions:
        if attraction.visible == True:
            attraction.update(currentHour)
    simulationClock.text = f"{10+currentHour}:00"
    #Get quit input + others
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isRunning = False
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            #print(pygame.mouse.get_pos())
            if ev.button == 1:
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
                    if obj.clickingType == "Continue":
                        if(obj.update()):
                            
                            CurrentScreen = MenuScreen
                for i in Attractions:
                    i.rect.clicking = True
    
    #Display frame
    pygame.display.update()
    Clock.tick(FPS)
    #Update Hour Simulation
    #if statement Goes here:
    if InSimulation:
        HourTimer += (Clock.get_time()/20000)#20000 is 10 sec = 1h
    if HourTimer >= secondsPerHour and currentHour < 11:
        HourTimer = 0
        currentHour += 1
    # elif currentHour >= 11:
    #     finishSound.play(loops=-1)

#Exit the game
pygame.quit()
#Import + Initialize Libraries
import pygame
import random
import copy
pygame.init()
from ScreenElements import Rectangle
from ScreenElements import Text
from ThemePark import Attraction
from pathfindtestfile import PathfindingCharacter
from RideData import Ride_Data
from RideData import Concessions
TempRideDataRides = copy.deepcopy(Ride_Data)
TempRideDataConcessions = copy.deepcopy(Concessions)

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
MainEntrance = Attraction(screen, "Main Entrance", GREY, 450, 100, 100, 0, "Entrance", "image/GrandExit.png")
GrandExit = Attraction(screen, "Grand Exit", GREY, 450, 100, 700, 0, "Exit", "image/GrandExit.png")
NebulaSpinner = Attraction(screen, "Nebula Spinner", PURPLE, 150, 200, 10, 110, "Ride", "image/nebulaSpinner.png", [158, 161])
RocketSlingshot = Attraction(screen, "Rocket Slingshot", GREEN, 150, 200, 10, 328, "Ride", "image/RocketSlingshot.png", [159, 379])
TitanCoaster = Attraction(screen, "Titan Coaster", RED, 140, 150, 558, 110, "Ride", "image/TitanCoaster.png", [558, 159])
PixelArcade = Attraction(screen, "Pixel Arcade", MAGENTA, 140, 150, 558, 278, "Ride", "image/PixelArcade.png", [558, 322])
SplashingMountain = Attraction(screen, "Splashing Mountain", BLUE, 150, 200, 1125, 105, "Ride", "image/SplashingMountain.png", [1125, 166])
LazyRiver = Attraction(screen, "Lazy River", LIGHTBLUE, 150, 200, 1125, 328, "Ride", "image/LazyRiver.png", [1125, 384])
QuantumCafe = Attraction(screen, "Quantum Cafe", PURPLE, 230, 120, 107, 571, "Concession", "image/QuantumCafe.png", [194, 572])
PixelPopcorn = Attraction(screen, "Pixel Popcorn", PINK, 230, 120, 355, 571, "Concession", "image/PixelPopcorn.png", [405, 570])
SugarShack = Attraction(screen, "The Sugar Shack", WHITE, 230, 120, 660, 571, "Concession", "image/SugarShack.png", [716, 571])
HydrationStation = Attraction(screen, "Hydration Station", BLUE, 230, 120, 935, 571, "Concession", "image/HydrationStation.png", [1014, 571])
Attractions = [NebulaSpinner, QuantumCafe, MainEntrance, GrandExit, RocketSlingshot, TitanCoaster, PixelArcade, PixelPopcorn, SplashingMountain, LazyRiver, SugarShack, HydrationStation]
Waypoints = [NebulaSpinner, QuantumCafe, RocketSlingshot, TitanCoaster, PixelArcade, PixelPopcorn, SplashingMountain, LazyRiver, SugarShack, HydrationStation]

#Define the different screens/visual-segments of the game

SettingsTitle = Text(screen=screen, x=WIDTH/2, y=75, height=100, colour=BLACK, backgroundColour=None, Text="Settings")
BackToMenu = Rectangle(screen, True, "Continue", None, 800, 550, 400, 100, 0, None, MENUBUTTONCOLOUR, None, None)
BackToMenuText = Text(screen, None, None, None, 1000, 600, 0, 50, 0, BLACK, None, "comic sans ms", "Back")
RandomText = Text(screen=screen, x=170, y=300, height=50, colour=BLACK, backgroundColour=None, Text="Random Events: ")
RandomToggle = Rectangle(screen=screen, clickable=True, clickingType="ToggleRandom", x=325, y=275, width=75, height=50, backgroundColour=RED, colour=None, visible=True)

SettingsScreen = [SettingsTitle, RandomText, BackToMenu, BackToMenuText, RandomToggle]

simulationClock = Text(screen, False, None, None, WIDTH/2 - 20, 30, 0, 30, 0, BLACK, None, "comic sans ms", "10:00")
OpenSign = Rectangle(screen, None, None, None, WIDTH/2 - 50, 40, 60, 30, 0, None, GREEN, None, None)
OpenSignText = Text(screen, None, None, None, WIDTH/2 - 20, 55, 0, 20, 0, WHITE, None, None, "Open")
ExitToMenuText = Text(screen, None, None, None, 1230, 31, 60, 20, 0, BLACK, None, None, "Exit")
ConfirmBackground = Rectangle(screen, None, None, None, 707, 111, 450, 400, 0, None, DARKGREY, None, None, visible=False)
ConfirmExitButton = Rectangle(screen, True, "Exit", None, 728, 277, 408, 100, 0, None, GREEN, None, None, visible=False)
ConfirmExitText = Text(screen, None, None, None, 932, 327, 408, 50, 0, BLACK, None, None, "Confirm", visible=False)
DenyExitText = Text(screen, None, None, None, 932, 450, 408, 50, 0, BLACK, None, None, "Deny", visible=False)
ConfirmBackgroundText = Text(screen, None, None, None, 932, 200, 408, 100, 0, WHITE, None, None, "Exit", visible=False)
DenyExitButton = Rectangle(screen, True, "ClosePopup", [ConfirmBackground, ConfirmBackgroundText, ConfirmExitButton, ConfirmExitText, DenyExitText], 728, 400, 408, 100, 0, None, RED, None, None, visible=False)
DenyExitButton.clickScreen.append(DenyExitButton)
ExitToMenu = Rectangle(screen, True, "OpenPopup", [ConfirmBackground, ConfirmBackgroundText, ConfirmExitButton, ConfirmExitText, DenyExitButton, DenyExitText], 1200, 11, 60, 40, 0, None, RED, None, None)

SimulationScreen = [simulationClock, OpenSign, OpenSignText, ExitToMenu, ExitToMenuText, ConfirmBackground, ConfirmBackgroundText, ConfirmExitButton, ConfirmExitText, DenyExitButton, DenyExitText]

Title = Text(screen, False, None, None, WIDTH/2, 100, None, 80, None,  BLACK, None, "comic sans ms", "Ride Rush")
PlayButton = Rectangle(screen, True, "Play", SimulationScreen, WIDTH/2 - 195, 300, 400, 100, 0, None, MENUBUTTONCOLOUR, None, None)
PlayText = Text(screen, False, None, None, WIDTH/2, 350, None, 100, 0, BLACK, None, None, "Play")
TutorialButton = Rectangle(screen, True, "Continue", None, WIDTH/2 - 195, 450, 400, 100, 0, None, MENUBUTTONCOLOUR, None, None)
TutorialButtonText = Text(screen, None, None, None, WIDTH/2, 500, 400, 100, 0, BLACK, None, None, "Tutorial")
SettingsButton = Rectangle(screen=screen, clickable=True, clickingType="Continue", clickScreen=SettingsScreen, x=WIDTH/2 - 195, y=600, width=400, height=100, borderWidth=0, backgroundColour=MENUBUTTONCOLOUR)
SettingsText = Text(screen=screen, x=WIDTH/2, y=650, width=0, height=100, borderWidth=0, colour=BLACK, backgroundColour=None, Text="Settings")

MenuScreen = [Title, PlayButton, PlayText, TutorialButton, TutorialButtonText, SettingsButton, SettingsText]
ConfirmExitButton.clickScreen = MenuScreen
BackToMenu.clickScreen = MenuScreen

ControlsTitle = Text(screen, False, None, None, WIDTH/2, 100, None, 80, None,  BLACK, None, "comic sans ms", "Controls/Tutorial")
CloseAlerts = Text(screen, False, None, None, WIDTH/2, 300, None, 50, None, BLACK, None, "comic sans ms", "To close alerts, simply left-click on the coloured object holding the alert.")
AlertsExplain = Text(screen, False, None, None, WIDTH/2, 350, None, 40, None, BLACK, None, "comic sans ms", "Alerts only happen when the satisfaction/waiting time/items sold falls below an amount.")
SettingsTip = Text(screen, False, None, None, WIDTH/2, 400, None, 50, None, BLACK, None, "comic sans ms", "There are many additional features in the settings.")
RedDotNotice = Text(screen, False, None, None, WIDTH/2, 450, None, 50, None, BLACK, None, "comic sans ms", "Red dots represent people navigating the park.")
ContinueButton = Rectangle(screen, True, "Continue", MenuScreen, 800, 550, 400, 100, 0, None, MENUBUTTONCOLOUR, None, None)
showTutOnStart = "ShowTutorialOnStart.txt"
DoNotShowAgainButton = Rectangle(screen, True, "Edit", showTutOnStart, 800, 550, 400, 100, 0, None, MENUBUTTONCOLOUR, None, None)
DoNotShowAgainText = Text(screen, None, None, None, 1000, 600, 0, 50, 0, BLACK, None, "comic sans ms", "Do Not Show Again")
ControlsScreen = [ControlsTitle, CloseAlerts, ContinueButton, DoNotShowAgainButton, DoNotShowAgainText, AlertsExplain, SettingsTip]
TutorialButton.clickScreen = ControlsScreen

StatsTitle = Text(screen, False, None, None, WIDTH/2, 100, None, 80, None,  BLACK, None, "comic sans ms", "Statistics Report")
PercentageFixed = Text(screen=screen, x=WIDTH/2, y=200, height=50, colour=BLACK, Text="You fixed _ % of alerts.")
StatsScreen = [StatsTitle, PercentageFixed]
rawStats = []
formattedStats = []
fixedAmount = 0
totalAlerts = 0

#Make pathfinding dot
characters = [PathfindingCharacter() for i in range(100)]

#Define the screen currently being displayed
showTutOnStartFile = open(showTutOnStart, "r")
if showTutOnStartFile.readline() == "True":
    CurrentScreen = ControlsScreen
else:
    CurrentScreen = MenuScreen
InSimulation = False
FinishedSimulation = False
RandomEvents = False

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
    screen.fill(BACKGROUNDCOLOUR)
    #random red dot moving
    if InSimulation:
        for character in characters:
            character.draw_circle()
            character.update_movement()
            if character.moving_or_not() == False:
                random_destination = random.choice(Waypoints)
                character.move_to_destination(random_destination.entrance[0], random_destination.entrance[1], pygame.rect.Rect(random_destination.x, random_destination.y, random_destination.width, random_destination.height).center)
            if character.clone_yourself:
                should_i_clone_myself = random.randint(1,1000)
                if should_i_clone_myself == 1:
                    characters.append(PathfindingCharacter())
                    characters.remove(random.choice(characters))
                    characters.remove(random.choice(characters))

    #Render attractions
    for attraction in Attractions:
        if attraction.visible == True:
            attraction.update(currentHour, [TempRideDataRides, TempRideDataConcessions])
    #Render objects
    for obj in CurrentScreen:
        obj.update()
    #Update visual clock display
    simulationClock.text = f"{10+currentHour}:00"
    #Get quit input + click inputs
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isRunning = False
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                #print(pygame.mouse.get_pos())
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
                            ConfirmBackground.visible = False 
                            ConfirmBackgroundText.visible = False
                            ConfirmExitButton.visible = False
                            ConfirmExitText.visible = False
                            DenyExitButton.visible = False
                            DenyExitText.visible = False
                            OpenSign.bc = GREEN
                            OpenSignText.c = WHITE
                            for attraction in Attractions:
                                attraction.CTAButton.visible = False
                                attraction.CTAButtonText.visible = False
                                attraction.CTAFix.visible = False
                                attraction.CTAFixText.visible = False
                                attraction.CTAPopup.visible = False
                            currentHour = 0
                            HourTimer = 0
                            if RandomEvents:
                                for i in TempRideDataRides:
                                    if list.index(TempRideDataRides, i) == 0:
                                        for v in i.keys():
                                            i[v]["wait"] = int(random.randint(0, 750)/10)
                                            i[v]["satisfaction"] = random.randint(65, 100)
                                    else:
                                        for v in i.keys():
                                            i[v]["wait"] = int(TempRideDataRides[list.index(TempRideDataRides, i)-1][v]["wait"]+random.randint(-150, 150)/10)
                                            if i[v]["wait"] < 0:
                                                i[v]["wait"] = 0
                                            i[v]["satisfaction"] = TempRideDataRides[list.index(TempRideDataRides, i)-1][v]["satisfaction"]+random.randint(-15, 15)
                                            if i[v]["satisfaction"] < 0:
                                                i[v]["satisfaction"] = 0
                                            elif i[v]["satisfaction"] > 100:
                                                i[v]["satisfaction"] = 100
                                for i in TempRideDataConcessions:
                                    if list.index(TempRideDataConcessions, i) == 0:
                                        for v in i.keys():
                                            i[v]["items"] = int(random.randint(13, 78))
                                            if i[v]["items"] < 0:
                                                i[v]["items"] = 0
                                            #i[v]["sales"] = random.randint(i[v]["items"], (i[v]["items"])*6)
                                    else:
                                        for v in i.keys():
                                            i[v]["items"] = int(TempRideDataConcessions[list.index(TempRideDataConcessions, i)-1][v]["items"]+random.randint(-150, 150)/10)
                                            if i[v]["items"] < 0:
                                                i[v]["items"] = 0
                                            #i[v]["sales"] = random.randint(i[v]["items"], (i[v]["items"])*6)

                            else:
                                TempRideDataRides = copy.deepcopy(Ride_Data)
                                TempRideDataConcessions = copy.deepcopy(Concessions)
                    elif obj.clickingType == "Exit":
                        if(obj.update()):
                            CurrentScreen = MenuScreen
                            for attraction in Attractions:
                                attraction.visible = False
                                attraction.alerting = False
                            InSimulation = False
                    elif obj.clickingType == "Continue":
                        if(obj.update()):
                            CurrentScreen = obj.clickScreen
                    elif obj.clickingType == "OpenPopup":
                        if (obj.update()):
                            for object in obj.clickScreen:
                                object.visible = True
                    elif obj.clickingType == "ClosePopup":
                        if (obj.update()):
                            for object in obj.clickScreen:
                                object.visible = False
                    elif obj.clickingType == "Edit":
                        if (obj.update()):
                            pass
                    elif obj.clickingType == "ToggleRandom":
                        if (obj.update()):
                            if RandomEvents:
                                obj.bc = RED
                                RandomEvents = False
                            else:
                                RandomEvents = True
                                obj.bc = GREEN
                            
                #Alert attractions that the user is clicking
                for i in Attractions:
                    i.rect.clicking = True
                    i.CTAButton.clicking = True
                    i.CTAFix.clicking = True
    
    #Display frame
    pygame.display.update()
    Clock.tick(FPS)
    #Update Hour Simulation
    if InSimulation:
        HourTimer += (Clock.get_time()/1000)
    if HourTimer >= secondsPerHour and currentHour < 11:
        HourTimer = 0
        currentHour += 1
    elif currentHour == 11 and InSimulation == True:
        OpenSign.bc = RED
        OpenSignText.text = "Closed"
        HourTimer += (Clock.get_time()/1000)
        if HourTimer >= secondsPerHour:
            InSimulation = False
            CurrentScreen = StatsScreen
            for attraction in Attractions:
                attraction.visible = False
                attraction.alerting = False
                rawStats.append(attraction.getStats())
                for i in rawStats:
                    totalAlerts += i[0]
                    fixedAmount += i[1]
            PercentageFixed.text = f"You fixed {fixedAmount/totalAlerts*100} % of alerts."

#Exit the game
pygame.quit()
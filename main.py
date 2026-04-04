import pygame
pygame.init()

Clock = pygame.time.Clock()
FPS = 60

WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ride Rush")

WHITE = [255,255,255]
RED = [255,0,0]
GREEN = [0,255,0]
BLUE = [0,0,255]
BLACK = [0,0,0]
YELLOW = [255,255,0]
PURPLE = [255,0,255]
ORANGE = [255,180,0]
BACKGROUNDCOLOUR = [115, 147, 179]

MenuScreen = []

SettingsScreen = []

SimulationScreen = []

CurrentScreen = []

isRunning = True
while isRunning:
    screen.fill(BACKGROUNDCOLOUR)
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isRunning = False
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
    pygame.display.update()
    Clock.tick(FPS)

pygame.quit()
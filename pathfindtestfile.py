#i dont want to destroy the main file so i created a test file

import pygame
import random


pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]



class PathfindingCharacter:
    def __init__(self):
        self.x = random.randint(170, 470)
        self.y = random.randint(150, 200)
        self.x_destination = 0
        self.y_destination = 0
        self.currently_moving = False
        self.radius = 4
        self.clone_yourself = False
    
    def draw_circle(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)
    
    def move_to_bottom_left(self):
        if self.currently_moving == False:
            self.x_destination = random.randint(170, 470)
            self.y_destination = random.randint(530, 560)
            self.currently_moving = True


    def move_to_bottom_right(self):
        if self.currently_moving == False:
            self.x_destination = random.randint(710, 1120)
            self.y_destination = random.randint(530, 560)
            self.currently_moving = True


    def move_to_top_left(self):
        if self.currently_moving == False:
            self.x_destination = random.randint(170, 470)
            self.y_destination = random.randint(150, 200)
            self.currently_moving = True
    
    def move_to_destination(self, x_place_to_go, y_place_to_go, center=None):
        self.currently_moving = True
        self.x_destination = x_place_to_go
        self.y_destination = y_place_to_go
        self.center_destination = center


    def update_movement(self):


        if self.currently_moving:

            if self.x < self.x_destination:
                self.x += 1
            if self.x > self.x_destination:
                self.x -= 1

            if self.y < self.y_destination:
                self.y += 1
            if self.y > self.y_destination:
                self.y -= 1


            if self.x == self.x_destination and self.y == self.y_destination:
                self.currently_moving = False
                self.clone_yourself = True
                if self.x_destination != self.center_destination[0] or self.y_destination != self.center_destination[1]:
                    self.currently_moving = True
                    self.x_destination = self.center_destination[0]
                    self.y_destination = self.center_destination[1] 

        
    def moving_or_not(self):
        return self.currently_moving
    

        

# path = [
#     (100, 100),  # Top Left
#     (500, 100),   # corner to the right of top left

#     (500, 300),
#     (780, 300),
#     (780, 100),    # to the left of top right

#     (1150, 100),  # Top Right
#     (1150, 600),  # Bottom Right
#     (100, 600),    # Bottom Left
#     (100, 100)
# ]



# characters = [PathfindingCharacter() for i in range(20)]

# running = True

# while running:

#     screen.fill(WHITE)

#     pygame.draw.lines(screen, BLACK, False, path, 6)

#     for character in characters:
#         character.draw_circle()
#         character.move_to_another_spot()

#     pygame.display.flip()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False


#     clock.tick(60)

# pygame.quit()
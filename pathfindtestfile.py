#i dont want to destroy the main file so i created a test file

import pygame
import random


pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]
BACKGROUNDCOLOUR = [115, 147, 179]

speed = 1



class PathfindingCharacter:
    def __init__(self):
        self.x = random.randint(170, 470)
        self.y = random.randint(150, 200)
        self.x_destination = 0
        self.y_destination = 0
        self.currently_moving_to_attraction = False
        self.currently_moving_to_corner = False
        self.moving = False
        self.radius = 4
        self.clone_yourself = False
        self.path = []
        self.quadrantOrder = ["Top-Left", "Bottom-Left", "Bottom-Right", "Top-Right"]
    
    def draw_circle(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)
    
    def get_quadrant(self, x=0, y=0):
        if x <= 640 and y >= 360:
            return "Bottom-Left"
        elif x > 640 and y >= 360:
            return "Bottom-Right"
        elif x <= 640 and y < 360:
            return "Top-Left"
        elif x > 640 and y < 360:
            return "Top-Right"

    # def is_it_in_bottom_left(self, x, y):
    #     if x <= 640 and y >= 360:
    #         return True
    #     else:
    #         return False
    
    # def is_it_in_bottom_right(self, x, y):
    #     if x >= 640 and y >= 360:
    #         return True
    #     else:
    #         return False
        
    # def is_it_in_top_left(self, x, y):
    #     if x <= 640 and y <= 360:
    #         return True
    #     else:
    #         return False

    # def is_it_in_top_right(self, x, y):
    #     if x >= 640 and y <= 360:
    #         return True
    #     else:
    #         return False

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

        # for i in self.path:
        #     if self.path.index(i) < len(self.path) - 1:
        #         self.moveToQuadrant(i)
        #     else:
                # self.x_destination = destination.entrance[0]
                # self.y_destination = destination.entrance[1]
        #         self.move()
        self.moveToQuadrant(self.path[0])
        self.path.pop(0)
        self.moving = True
        return self.path
        

        
        

    def move_to_bottom_left(self):
        if self.is_it_in_top_left(self.x, self.y) or self.is_it_in_bottom_left(self.x, self.y) or self.is_it_in_bottom_right(self.x, self.y):
            if self.currently_moving_to_attraction == False and self.currently_moving_to_corner == False:
                self.x_destination = random.randint(170, 470)
                self.y_destination = random.randint(530, 560)
                self.currently_moving_to_corner = True
        if self.is_it_in_top_right(self.x, self.y):
            if self.currently_moving_to_attraction == False and self.currently_moving_to_corner == False:
                self.move_to_bottom_right()
                it_isnt_in_place = True
                while it_isnt_in_place:
                    if self.x == self.x_destination and self.y == self.y_destination:
                        it_isnt_in_place = False
                        self.x_destination = random.randint(170, 470)
                        self.y_destination = random.randint(530, 560)
                        self.currently_moving_to_corner = True

    

    def move_to_bottom_right(self):
        if self.is_it_in_bottom_left(self.x,self.y) or self.is_it_in_bottom_right(self.x, self.y) or self.is_it_in_top_right(self.x, self.y):
            if self.currently_moving_to_attraction == False and self.currently_moving_to_corner == False:
                self.x_destination = random.randint(710, 1120)
                self.y_destination = random.randint(530, 560)
                self.currently_moving_to_corner = True
        if self.is_it_in_top_left(self.x, self.y):
            if self.currently_moving_to_attraction == False and self.currently_moving_to_corner == False:
                self.move_to_bottom_left()
                it_isnt_in_place = True
                while it_isnt_in_place:
                    if self.x == self.x_destination and self.y == self.y_destination:
                        it_isnt_in_place = False
                        self.x_destination = random.randint(710, 1120)
                        self.y_destination = random.randint(530, 560)
                        self.currently_moving_to_corner = True
        

    def move_to_top_left(self):
        if self.is_it_in_top_left(self.x, self.y) or self.is_it_in_bottom_left(self.x, self.y):
            if self.currently_moving_to_attraction == False and self.currently_moving_to_corner == False:
                self.x_destination = random.randint(170, 470)
                self.y_destination = random.randint(150, 200)
                self.currently_moving_to_corner = True
        if self.is_it_in_bottom_right(self.x, self.y):
            if self.currently_moving_to_attraction == False and self.currently_moving_to_corner == False:
                self.move_to_bottom_left()
                it_isnt_in_place = True
                while it_isnt_in_place:
                    if self.x == self.x_destination and self.y == self.y_destination:
                        it_isnt_in_place = False
                        self.x_destination = random.randint(170, 470)
                        self.y_destination = random.randint(150, 200)
                        self.currently_moving_to_corner = True
        if self.is_it_in_top_right(self.x, self.y):
            if self.currently_moving_to_attraction == False and self.currently_moving_to_corner == False:
                self.move_to_bottom_right()
                it_isnt_in_place = True
                while it_isnt_in_place:
                    if self.x == self.x_destination and self.y == self.y_destination:
                        it_isnt_in_place = False
                        self.move_to_top_left()


        
    def move_to_top_right(self):
        if self.is_it_in_top_right(self.x, self.y) or self.is_it_in_bottom_right(self.x, self.y):
            if self.currently_moving_to_attraction == False and self.currently_moving_to_corner == False:
                self.x_destination = random.randint(710, 1120)
                self.y_destination = random.randint(150, 200)
                self.currently_moving_to_corner = True
        if self.is_it_in_bottom_left(self.x, self.y):
            if self.currently_moving_to_attraction == False and self.currently_moving_to_corner == False:
                self.move_to_bottom_right()
                it_isnt_in_place = True
                while it_isnt_in_place:
                    if self.x == self.x_destination and self.y == self.y_destination:
                        it_isnt_in_place = False
                        self.x_destination = random.randint(710, 1120)
                        self.y_destination = random.randint(150, 200)
                        self.currently_moving_to_corner = True
        if self.is_it_in_top_left(self.x, self.y):
            if self.currently_moving_to_attraction == False and self.currently_moving_to_corner == False:
                self.move_to_bottom_left()
                it_isnt_in_place = True
                while it_isnt_in_place:
                    if self.x == self.x_destination and self.y == self.y_destination:
                        it_isnt_in_place = False
                        self.move_to_top_right()




    
    def move_to_destination(self, x_place_to_go, y_place_to_go, center=None):
        self.currently_moving_to_attraction = True
        self.x_destination = x_place_to_go
        self.y_destination = y_place_to_go
        self.center_destination = center



    def update_movement_to_corner(self):
        if self.currently_moving_to_corner:

            if self.x < self.x_destination:
                self.x += speed
            if self.x > self.x_destination:
                self.x -= speed

            if self.y < self.y_destination:
                self.y += speed
            if self.y > self.y_destination:
                self.y -= speed


            if self.x == self.x_destination and self.y == self.y_destination:
                self.currently_moving_to_corner = False

    def update_movement_to_attraction(self):


        if self.currently_moving_to_attraction:

            if self.x < self.x_destination:
                self.x += 1
            if self.x > self.x_destination:
                self.x -= 1

            if self.y < self.y_destination:
                self.y += 1
            if self.y > self.y_destination:
                self.y -= 1


            if self.x == self.x_destination and self.y == self.y_destination:
                self.currently_moving_to_attraction = False
                self.clone_yourself = True
                if self.x_destination != self.center_destination[0] or self.y_destination != self.center_destination[1]:
                    self.currently_moving_to_attraction = True
                    self.x_destination = self.center_destination[0]
                    self.y_destination = self.center_destination[1] 

        
    def moving_or_not(self):
        if self.currently_moving_to_corner == False and self.currently_moving_to_attraction == False:
            return False
        else:
            return True
    

        

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
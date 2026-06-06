#i dont want to destroy the main file so i created a test file

import pygame
import random


pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]

speed = 1



class PathfindingCharacter:
    def __init__(self):
        self.x = random.randint(170, 470)
        self.y = random.randint(150, 200)
        self.x_destination = 0
        self.y_destination = 0
        self.currently_moving_to_attraction = False
        self.currently_moving_to_corner = False
        self.radius = 4
        self.clone_yourself = False
    
    def draw_circle(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)
    

    def is_it_in_bottom_left(self, x, y):
        if x <= 640 and y >= 360:
            return True
        else:
            return False
    
    def is_it_in_bottom_right(self, x, y):
        if x >= 640 and y >= 360:
            return True
        else:
            return False
        
    def is_it_in_top_left(self, x, y):
        if x <= 640 and y <= 360:
            return True
        else:
            return False

    def is_it_in_top_right(self, x, y):
        if x >= 640 and y <= 360:
            return True
        else:
            return False
        

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
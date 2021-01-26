import pygame
import math
import constants


class Player(constants.Var):

    def __init__(self, x, y, color, radius):
        super().__init__(x, y, color, radius)
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.speed = 0.3
        self.slow = 40
        self.mass = 10
        self.pellets = []

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def c_point(self):
        return f"Circle at X: {self.x}, Y: {self.y}"

    def v_point(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        position_str = 'X: ' + str(self.mouse_x).ljust(4) + ' Y: ' + str(self.mouse_y).ljust(4)
        return f"Mouse at {position_str}"

    def move(self):
        vector_x = self.mouse_x - self.x
        vector_y = self.mouse_y - self.y
        magnitude = math.sqrt(vector_x**2+vector_y**2)
        if magnitude > 0.1:
            vector_x = vector_x/magnitude * (self.speed-(self.speed/(self.radius/self.mass)))  # *(0,3-(40/10))
            vector_y = vector_y/magnitude * (self.speed-(self.speed/(self.radius/self.mass)))  # oko 50% usporava
            self.x += vector_x
            self.y += vector_y

    def eat_food(self):
        self.radius += 0.26
        self.mass += 0.26

    def check_collision(self, pellets):
        index = 0
        food_eaten = False
        for food in pellets:

            distance = math.sqrt((self.x-food.x) ** 2 + (self.y - food.y) ** 2)
            if distance < self.radius:
                Player.eat_food(self)
                food_eaten = True

                break
            index += 1
        if food_eaten:
            pellets.pop(index)

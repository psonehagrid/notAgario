import pygame
import constants


class Food(constants.Var):
    def __init__(self, x, y, color, radius):
        super().__init__(x, y, color, radius)
        self.pellets = []

    def food_draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def add_food(self):
        pass

    def delete_food(self):
        pass

import pygame
import constants


class Food(constants.Var):
    def __init__(self, x, y, color, radius):
        super().__init__(x, y, color, radius)

    def food_draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)



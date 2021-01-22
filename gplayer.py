import pygame
import math


class Player:
    def __init__(self, x, y, circle_color, circle_radius):
        self.x = x
        self.y = y
        self.circle_radius = circle_radius
        self.circle_color = circle_color
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.speed = 0.1

    def draw(self, window):
        pygame.draw.circle(window, self.circle_color, (self.x, self.y), self.circle_radius)

    def c_point(self):
        print(f"Circle at X: {self.x}, Y: {self.y}")

    def v_point(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        position_str = 'X: ' + str(self.mouse_x).ljust(4) + ' Y: ' + str(self.mouse_y).ljust(4)
        print(f"Mouse at {position_str}")

    def move(self):
        vector_x = self.mouse_x - self.x
        vector_y = self.mouse_y - self.y
        magnitude = math.sqrt(vector_x**2+vector_y**2)
        if magnitude > 0.1:
            vector_x = vector_x/magnitude * self.speed
            vector_y = vector_y/magnitude * self.speed
            self.x += vector_x
            self.y += vector_y

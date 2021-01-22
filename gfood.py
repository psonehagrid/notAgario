import pygame


class Food:
    def __init__(self, fdx, fdy, fd_color, fd_radius):
        self.fdx = fdx
        self.fdy = fdy
        self.fd_color = fd_color
        self.fd_radius = fd_radius

    def food_draw(self, window):
        pygame.draw.circle(window, self.fd_color, (self.fdx, self.fdy), self.fd_radius)

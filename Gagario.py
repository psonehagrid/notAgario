import pygame
import random
import math


screen_width, screen_height = 700, 700
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game")


class Player:
    def __init__(self, x, y, circle_color, circle_radius):
        self.x = x
        self.y = y
        self.circle_radius = circle_radius
        self.circle_color = circle_color
        self.mousex, self.mousey = pygame.mouse.get_pos()
        self.speed = 0.1


    def draw(self, window):
        pygame.draw.circle(window, self.circle_color, (self.x, self.y), self.circle_radius)

    def c_point(self):
        print(f"Circle at X: {self.x}, Y: {self.y}")

    def v_point(self):
        self.mousex, self.mousey = pygame.mouse.get_pos()
        positionStr = 'X: ' + str(self.mousex).rjust(4) + ' Y: ' + str(self.mousey).rjust(4)
        print(f"Mouse at {positionStr}")

    def move(self):
        vectx = self.mousex - self.x
        vecty = self.mousey - self.y
        magnitude = math.sqrt(vectx**2+vecty**2)
        if magnitude > 0.1:
            vectx = vectx/magnitude * self.speed
            vecty = vecty/magnitude * self.speed
            self.x += vectx
            self.y += vecty


def constant_display(window, player):
    window.fill(pygame.Color("white"))
    player.draw(window)
    pygame.display.update()


def main():
    run = True
    p = Player(random.randint(35, screen_width-40),
               random.randint(35, screen_height-40),
               pygame.Color(
                   random.randint(0, 200),
                   random.randint(0, 200),
                   random.randint(0, 200)
               ), 40)
    event = pygame.event.poll()
    while run:
        if event.type == pygame.MOUSEMOTION:
            p.c_point()
            p.v_point()
            p.move()
        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False
                pygame.quit()

        constant_display(window, p)


main()


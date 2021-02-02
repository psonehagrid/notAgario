from pygame.locals import *
import time
import gplayer
import random
import pygame
import gfood
import sys


class Play:
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 720
        self.pellets = Play.food_gen(self, [])
        self.max_pellets = int()
        self.title = "Gagario"
        self.window = pygame.display.set_mode((self.screen_width, self.screen_height), RESIZABLE)
        self.p = gplayer.Player(random.randint(35, self.screen_width - 40),
                                random.randint(35, self.screen_height - 40),
                                pygame.Color(random.randint(0, 200),
                                             random.randint(0, 200),
                                             random.randint(0, 200)), 40)

    def food_gen(self, pellets):
        i = 0
        self.max_pellets = 100
        while i < self.max_pellets:
            pellets.append(gfood.Food(random.randint(10, self.screen_width-10),
                                      random.randint(10, self.screen_height-10),
                                      pygame.Color(random.randint(0, 200),
                                                   random.randint(0, 200),
                                                   random.randint(0, 200)),
                                      10))
            i += 1
        return pellets

    def constant_display(self, player, pellets):
        self.window.fill(pygame.Color("black"))
        for i in pellets:
            i.food_draw(self.window)
        player.draw(self.window)
        pygame.display.update()

    def main(self):
        run = True
        event = pygame.event.poll()
        while run:
            start = time.time()
            self.p.check_collision(self.pellets)
            if event.type == pygame.MOUSEMOTION:
                self.p.c_point()
                self.p.v_point()
                self.p.move()
            for event in pygame.event.get():
                if event.type == VIDEORESIZE:
                    self.window = pygame.display.set_mode((self.window.get_width(), self.window.get_height()), pygame.RESIZABLE)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                    sys.exit()

            Play.constant_display(self, self.p, self.pellets)
            try:
                end = time.time()
                fps = int(round(1 / (end - start)))
                pygame.display.set_caption(self.title + ": " + str(fps))
            except ZeroDivisionError:
                pass


if __name__ == '__main__':
    game_on = Play()
    game_on.main()


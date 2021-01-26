import gplayer
import random
import pygame
import gfood
import sys

screen_width, screen_height = 1280, 720
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game")


def food_gen(pellets):
    max_pellets = 200
    i = 0
    while i < max_pellets:
        pellets.append(gfood.Food(random.randint(10, screen_width-10),
                                  random.randint(10, screen_height-10),
                                  pygame.Color(random.randint(0, 200),
                                               random.randint(0, 200),
                                               random.randint(0, 200)),
                                  10))
        i += 1
    return pellets


pellets = food_gen([])


def constant_display(window, player, pellets):
    window.fill(pygame.Color("black"))
    for i in pellets:
        i.food_draw(window)
    player.draw(window)
    pygame.display.update()


def main():
    run = True
    p = gplayer.Player(random.randint(35, screen_width-40),
                       random.randint(35, screen_height-40),
                       pygame.Color(
                       random.randint(0, 200),
                       random.randint(0, 200),
                       random.randint(0, 200)
                       ), 40)
    event = pygame.event.poll()
    while run:
        p.check_collision(pellets)
        if event.type == pygame.MOUSEMOTION:
            p.c_point()
            p.v_point()
            p.move()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        constant_display(window, p, pellets)


main()
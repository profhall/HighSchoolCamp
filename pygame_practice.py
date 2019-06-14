"""
title: pygame_practice
author: Elizabeth
date: 2019-06-14 09:47
"""

import pygame

pygame.init()

size = (500, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("First Pygame")
BLACK = (0, 0, 0)
BROWN = (160,82,45)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BEIGE = (245, 228, 203)
PURPLE = (149, 0, 255)
PLUM = (188,143,143)

PI = 3.141592653
done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    screen.fill(WHITE)
    pygame.draw.ellipse(screen, BROWN, [95, 90, 80, 80])
    pygame.draw.ellipse(screen, BEIGE, [100, 100, 70, 100])
    pygame.draw.rect(screen, BEIGE, [123, 190, 25, 35])
    pygame.draw.ellipse(screen, BLACK, [100, 100, 70, 100], 1)
    pygame.draw.ellipse(screen, BROWN, [100, 80, 25, 25])
    pygame.draw.ellipse(screen, BROWN, [145, 80, 25, 25])

    pygame.draw.ellipse(screen, WHITE, [112, 125, 15, 10])
    pygame.draw.ellipse(screen, WHITE, [140, 125, 15, 10])
    pygame.draw.ellipse(screen, BLUE, [117, 127, 7, 7])
    pygame.draw.ellipse(screen, BLUE, [144, 127, 7, 7])
    pygame.draw.ellipse(screen, BLACK, [118, 128, 5, 5])
    pygame.draw.ellipse(screen, BLACK, [145, 128, 5, 5])

    pygame.draw.arc(screen, BLACK, [130, 140, 10, 10], PI, 0)
    pygame.draw.arc(screen, BLACK, [120, 160, 33, 15], PI, 0)
    pygame.draw.arc(screen, BLACK, [120, 160, 33, 23], PI, 0)

    # shirt
    pygame.draw.ellipse(screen, PLUM, [87, 210, 100, 200])
    pygame.draw.rect(screen, PLUM, [87, 310, 100, 100])

    # left arm
    pygame.draw.line(screen, BEIGE, [100, 250], [48, 330], 20)
    pygame.draw.line(screen, BEIGE, [100, 360], [48, 330], 20)
    pygame.draw.line(screen, PLUM, [100, 250], [48, 330], 20)

    # right arm
    pygame.draw.line(screen, BEIGE, [175, 250], [220, 330], 20)
    pygame.draw.line(screen, BEIGE, [190, 360], [220, 330], 20)
    pygame.draw.line(screen, PLUM, [175, 250], [220, 330], 20)

    # TODO: WORK GOES HERE

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

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

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10

ball_pos = 0


def draw_stick_figure(screen, x, y):
    pygame.draw.ellipse(screen, RED, [20, 200 + ball_pos, 40, 40])
    pygame.draw.ellipse(screen, BROWN, [95 + x, 90 + y, 80, 80])
    pygame.draw.ellipse(screen, BEIGE, [100 + x, 100 + y, 70, 100])
    pygame.draw.rect(screen, BEIGE, [123 + x, 190 + y, 25, 35])
    pygame.draw.ellipse(screen, BLACK, [100 + x, 100 + y, 70, 100], 1)
    pygame.draw.ellipse(screen, BROWN, [100 + x, 80 + y, 25, 25])
    pygame.draw.ellipse(screen, BROWN, [145 + x, 80 + y, 25, 25])

    pygame.draw.ellipse(screen, WHITE, [112 + x, 125 + y, 15, 10])
    pygame.draw.ellipse(screen, WHITE, [140 + x, 125 + y, 15, 10])
    pygame.draw.ellipse(screen, BLUE, [117 + x, 127 + y, 7, 7])
    pygame.draw.ellipse(screen, BLUE, [144 + x, 127 + y, 7, 7])
    pygame.draw.ellipse(screen, BLACK, [118 + x, 128 + y, 5, 5])
    pygame.draw.ellipse(screen, BLACK, [145 + x, 128 + y, 5, 5])

    pygame.draw.arc(screen, BLACK, [130 + x, 140 + y, 10, 10], PI, 0)
    pygame.draw.arc(screen, BLACK, [120 + x, 160 + y, 33, 15], PI, 0)
    pygame.draw.arc(screen, BLACK, [120 + x, 160 + y, 33, 23], PI, 0)

    # shirt
    pygame.draw.ellipse(screen, PLUM, [87 + x, 210 + y, 100, 200])
    pygame.draw.rect(screen, PLUM, [87 + x, 310 + y, 100, 100])

    # left arm
    pygame.draw.line(screen, BEIGE, [100 + x, 250 + y], [48 + x, 330 + y], 20)
    # pygame.draw.line(screen, BEIGE, [100 + x, 360 + y], [48 + x, 330 + y], 20)
    pygame.draw.line(screen, PLUM, [100 + x, 250 + y], [48 + x, 330 + y], 20)

    # right arm
    pygame.draw.line(screen, BEIGE, [175 + x, 250 + y], [220 + x, 330 + y], 20)
    # pygame.draw.line(screen, BEIGE, [190 + x, 360], [220 + x, 330 + y], 20)
    pygame.draw.line(screen, PLUM, [175 + x, 250 + y], [220 + x, 330 + y], 20)

    # pygame.draw.line(screen, BLUE, [100 + x, 100, 100, 100])


while not done:
    ball_pos += 1
    # User did something
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_speed = -3
    if keys[pygame.K_RIGHT]:
        x_speed = 3
    if keys[pygame.K_UP]:
        y_speed = -3
    if keys[pygame.K_DOWN]:
        y_speed = 3

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Move the object according to the speed vector.
    x_coord += x_speed
    y_coord += y_speed

    # Reset x_speed and y_speed for the next frame
    x_speed = 0
    y_speed = 0

    screen.fill(WHITE)

    draw_stick_figure(screen, x_coord, y_coord)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

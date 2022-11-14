import time

import pygame
import numpy as np


def get_color(x, y, h, m, s):
    phi = np.arctan2(x, -y)
    r = 255 * (0.25 + phi/2/np.pi - h/24)
    g = 255 * (0 + phi/2/np.pi - m/60)
    b = 255 * (0.5 + phi/2/np.pi - s/60)
    return np.array([int(r)%256, int(g)%256, int(b)%256])


width = 200
height = 200

pygame.init()

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Clock - RGB discs")

pixel_data = np.zeros((width, height, 3))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    t = time.time_ns()
    hours = t%(10**9 * 60 * 60 * 24) / (1e+9 * 60 * 60)
    minutes = t%(10**9 * 60 * 60) / (1e+9 * 60)
    seconds = t%(10**9 * 60) / 1e+9
    for x in range(width):
        for y in range(height):
            pixel_data[x, y] = get_color(x - width/2, y - height/2, hours, minutes, seconds)
    pygame.surfarray.blit_array(screen, pixel_data)
    pygame.display.update()

import pygame as pg
from level1 import *
from prince import *

win_w = 640
win_h = 400
fps = 60

pg.init()
window = pg.display.set_mode((win_w, win_h))
clock = pg.time.Clock()

group = pg.sprite.Group()
Level_1(0, 0, group)
Prince(100, 70, group)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    buttons_pressed = pg.key.get_pressed()
    window.fill((0, 0, 0))
    group.draw(window)

    pg.display.flip()
    time_delta = clock.tick(fps) / 1000.0
    group.update(time_delta, buttons_pressed)

pg.quit()
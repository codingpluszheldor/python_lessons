import pygame as pg
from player import *
from platforma import *
from backgroud import *

win_w = 384
win_h = 272
fps = 60

pg.init()
window = pg.display.set_mode((win_w, win_h))
clock = pg.time.Clock()
sprites_timer = pg.sprite.Group()
Player(win_w // 2, win_h // 4, sprites_timer)
Platforma(win_w // 2, win_h // 2, sprites_timer)
bg = Background()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    buttons_pressed = pg.key.get_pressed()
    window.fill((0, 0, 0))
    bg.draw(window)
    sprites_timer.draw(window)

    pg.display.flip()
    clock.tick(fps)

    sprites_timer.update(buttons_pressed)

pg.quit()

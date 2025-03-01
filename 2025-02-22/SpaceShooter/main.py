import pygame as pg
from helper import *
from background import *
from planet import *
from starts import *
from player import *

pg.init()
window = pg.display.set_mode((win_w, win_h))
clock = pg.time.Clock()

sprites = pg.sprite.Group()
Background("assets/background/layered/bg-back.png", sprites)
Stars(0, win_h // 2, "assets/background/layered/bg-stars.png", sprites)
Stars(win_w, win_h // 2, "assets/background/layered/bg-stars.png",
       sprites, True)
Planet(0, win_h // 2, "assets/background/layered/bg-planet.png", sprites)
Planet(win_w, win_h // 2, "assets/background/layered/bg-planet.png",
       sprites, True)
player = Player(win_w // 2, win_h // 2)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    buttons_pressed = pg.key.get_pressed()
    sprites.draw(window)
    player.draw(window)

    pg.display.flip()
    clock.tick(fps)
    sprites.update()
    player.update(buttons_pressed)

pg.quit()
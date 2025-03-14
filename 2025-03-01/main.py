import pygame as pg
import random
from helper import *
from background import *
from planet import *
from starts import *
from player import *
from bullet import *
from enemy import *

pg.init()
window = pg.display.set_mode((win_w, win_h))
clock = pg.time.Clock()

sprites = pg.sprite.Group()
sprites_timer = pg.sprite.Group()
Background("assets/background/layered/bg-back.png", sprites)
Stars(0, win_h // 2, "assets/background/layered/bg-stars.png", sprites)
Stars(win_w, win_h // 2, "assets/background/layered/bg-stars.png",
       sprites, True)
Planet(0, win_h // 2, "assets/background/layered/bg-planet.png", sprites)
Planet(win_w, win_h // 2, "assets/background/layered/bg-planet.png",
       sprites, True)
player = Player(win_w // 2, win_h // 2)
bullets = []
enemys = []
time_delta = 0
shoot_timer = 0
enemy_timer = 0
enemy_show = random.randint(1, 4)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    buttons_pressed = pg.key.get_pressed()
    if buttons_pressed[pg.K_SPACE] and shoot_timer > 0.3:
        shoot_timer = 0
        bullets.append(Bullet(player.rect.centerx, player.rect.centery, sprites_timer))

    if enemy_timer > enemy_show:
        enemy_timer = 0
        enemy_show = random.randint(1, 4)
        y = random.randint(60, win_h - 60)
        enemys.append(Enemy(win_w, y, sprites_timer))

    sprites.draw(window)
    sprites_timer.draw(window)
    player.draw(window)

    pg.display.flip()
    time_delta = clock.tick(fps) / 1000.0
    shoot_timer += time_delta
    enemy_timer += time_delta

    sprites.update()
    player.update(buttons_pressed)
    for bullet in bullets:
        bullet.update(time_delta)
    for enemy in enemys:
        enemy.update(time_delta)

    # for bullet in bullets:
    #     for enemy in enemys:

pg.quit()
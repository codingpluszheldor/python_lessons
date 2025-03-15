#
# https://ansimuz.itch.io/warped-space-shooter
#
import pygame as pg
import random
from background import *
from helper import *
from planet import *
from stars import *
from player import *
from bullet import *
from enemy import *
from explosion import *
from flash import *
from asteroid import *

pg.init()
window = pg.display.set_mode((win_w, win_h))
clock = pg.time.Clock()

sprites = pg.sprite.Group()
sprites_timer = pg.sprite.Group()
bg = Background("assets/background/layered/bg-back.png", sprites)
stars1 = Stars(0 , win_h / 2, "assets/background/layered/bg-stars.png", sprites)
stars2 = Stars(win_w, win_h / 2, "assets/background/layered/bg-stars.png", sprites)
planet1 = Planet(0, win_h / 2, "assets/background/layered/bg-planet.png", sprites)
planet2 = Planet(win_w, win_h / 2, "assets/background/layered/bg-planet.png", sprites, True)
player = Player(win_w / 2, win_h / 2)
bullets = []
enemys = []
asteroids = []
time_delta = 0
shoot_timer = 0
enemy_timer = 0
asteroid_timer = 0
enemy_show = random.randint(1, 4)
asteroid_show = random.randint(3, 8)

# BaseAsteroid(win_w - 10, win_h + 100, "assets/asteroids/asteroid.png", sprites_timer)
# BaseAsteroid(win_w + 10, win_h, "assets/asteroids/asteroid.png", sprites_timer)

pg.mixer.music.load('assets/music/exports/space-asteroids.wav')
pg.mixer.music.play(-1)

sound_explosion = pg.mixer.Sound('assets/Sound FX/explosion.wav')
sound_shot = pg.mixer.Sound('assets/Sound FX/shot 1.wav')

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    buttons_pressed = pg.key.get_pressed()
    if buttons_pressed[pg.K_SPACE] and shoot_timer > 0.3:
        shoot_timer = 0
        Flash(player.rect.centerx, player.rect.centery, sprites_timer)
        bullets.append(Bullet(player.rect.centerx, player.rect.centery, sprites_timer))
        sound_shot.play()

    if enemy_timer > enemy_show:
        enemy_timer = 0
        enemy_show = random.randint(1, 4)
        y = random.randint(60, win_h - 60)
        enemys.append(Enemy(win_w, y, sprites_timer))

    if asteroid_timer > asteroid_show:
        asteroid_timer = 0
        asteroid_show = random.randint(3, 8)
        x = random.randint(win_w / 2, win_w)
        y = random.randint(60, 120)
        size = random.randint(1, 100)
        if size < 50:
            asteroids.append(BigAsteroid(x, win_h + y, sprites_timer))
        else:
            asteroids.append(SmallAsteroid(x, win_h + y, sprites_timer))

    sprites.draw(window)
    sprites_timer.draw(window)
    player.draw(window)

    pg.display.flip()
    time_delta = clock.tick(fps) / 1000.0
    shoot_timer += time_delta
    enemy_timer += time_delta
    asteroid_timer += time_delta

    sprites.update()
    sprites_timer.update(time_delta)
    player.update(buttons_pressed)

    # for bullet in bullets:
    #     bullet.update(time_delta)
    #
    # for enemy in enemys:
    #     enemy.update(time_delta)

    bullets_copy = bullets[:]
    for bullet in bullets_copy:
        is_break = False
        for enemy in enemys:
            if bullet.rect.colliderect(enemy.rect):
                Explosion(enemy.rect.centerx, enemy.rect.centery, sprites_timer)
                sound_explosion.play()
                enemy.kill()
                enemys.remove(enemy)
                is_break = True
                break
        if is_break:
            bullet.kill()
            bullets.remove(bullet)

    bullets_copy = bullets[:]
    for bullet in bullets:
        is_break = False
        for asteroid in asteroids:
            if bullet.rect.colliderect(asteroid):
                Explosion(asteroid.rect.centerx, bullet.rect.centery, sprites_timer)
                sound_explosion.play()
                asteroid.set_damage()
                is_break = True
                if asteroid.is_died:
                    asteroids.remove(asteroid)
                break
        if is_break:
            bullet.kill()
            bullets.remove(bullet)

pg.quit()
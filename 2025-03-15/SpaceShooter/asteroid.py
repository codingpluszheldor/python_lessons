import pygame as pg
from helper import *


class BaseAsteroid(pg.sprite.Sprite):
    def __init__(self, start_x, start_y, filename, group):
        pg.sprite.Sprite.__init__(self)
        image = pg.image.load(filename).convert_alpha()
        self.image = pg.transform.scale(image, (image.get_width() * 2, image.get_height() * 2))
        self.image_base = self.image
        self.rect = self.image.get_rect()
        self.rect.centerx = start_x
        self.rect.centery = start_y
        self.x = self.rect.centerx
        self.y = self.rect.centery
        self.x_speed = 0.1
        self.y_speed = 0.2
        self.rotate_speed = 2
        self.angle = 0
        self.animation_timer = 0
        self.hp = 1
        self.is_died = False
        self.add(group)

    def update(self, time_delta):
        self.animation_timer += time_delta
        if self.animation_timer > 0.1:
            self.animation_timer = 0
            self.angle += self.rotate_speed
            self.image = pg.transform.rotate(self.image_base, self.angle)
            self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

        self.x -= self.x_speed
        self.y -= self.y_speed
        self.rect.centerx = int(self.x)
        self.rect.centery = int(self.y)

        if self.is_died:
            self.kill()

    def set_damage(self):
        self.hp -= 1
        if self.hp < 1:
            self.x = -1000
            self.is_died = True


class BigAsteroid(BaseAsteroid):
    def __init__(self, start_x, start_y, group):
        super().__init__(start_x, start_y, "assets/asteroids/asteroid.png", group)
        self.hp = 5


class SmallAsteroid(BaseAsteroid):
    def __init__(self, start_x, start_y, group):
        super().__init__(start_x, start_y, "assets/asteroids/asteroid-small.png", group)
        self.hp = 2
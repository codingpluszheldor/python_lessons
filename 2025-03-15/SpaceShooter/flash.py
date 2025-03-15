import pygame as pg
from helper import *


class Flash(pg.sprite.Sprite):
    def __init__(self, start_x, start_y, group):
        pg.sprite.Sprite.__init__(self)
        image = pg.image.load(f"assets/flash/flash.png").convert_alpha()
        self.image = pg.transform.scale(image, (image.get_width() * 2, image.get_height() * 2))
        self.rect = self.image.get_rect()
        self.rect.centerx = start_x + 35
        self.rect.centery = start_y
        self.animation_timer = 0
        self.add(group)

    def update(self, time_delta):
        self.animation_timer += time_delta
        if self.animation_timer > 0.1:
            self.animation_timer = 0
            self.kill()


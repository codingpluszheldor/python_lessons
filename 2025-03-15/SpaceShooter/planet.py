import pygame as pg
from helper import *


class Planet(pg.sprite.Sprite):
    def __init__(self, start_x, start_y, file_name, group, flip=False):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(file_name).convert_alpha()
        if flip:
            self.image = pg.transform.flip(self.image, True, True)
        self.image = pg.transform.scale(self.image,
                                        (self.image.get_width() * 2, self.image.get_height() * 2))
        self.rect = self.image.get_rect()
        self.rect.centerx = start_x
        self.rect.centery = start_y
        self.x = self.rect.centerx
        self.speed = 0.3
        self.add(group)


    def update(self):
        self.x -= self.speed
        self.rect.centerx = int(self.x)
        if self.rect.centerx < - self.image.get_width() / 2:
            self.rect.centerx = win_w + self.image.get_width() / 2
            self.x = self.rect.centerx
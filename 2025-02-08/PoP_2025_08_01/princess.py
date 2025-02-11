import pygame as pg
from helpers import *

class Princess(pg.sprite.Sprite):
    def __init__(self, x, y, group):
        pg.sprite.Sprite.__init__(self)
        self.win_w = win_w
        self.win_h = win_h
        self.images = {}
        self.rects = {}
        for i in range(801, 818):
            image = pg.image.load(f"assets/PRINCESS/TURN/res{i}.png").convert_alpha()
            w = image.get_width()
            h = image.get_height()
            image = pg.transform.scale(image, (w * 2, h * 2))
            self.images[i-801] = image
            rect = image.get_rect()
            rect.centerx = x
            rect.centery = y
            self.rects[i-801] = rect
        self.current_frame = 0
        self.animation_len = len(self.images)
        self.animation_speed = 8
        self.animation_timer = 0
        self.image = self.images[0]
        self.rect = self.rects[0]
        self.add(group)

    def update(self, time_delta):
        self.animation_timer += time_delta
        if self.animation_timer >= 1.0 / self.animation_speed:
            self.current_frame = (self.current_frame + 1) % self.animation_len
            self.animation_timer -= 1.0 / self.animation_speed
        self.image = self.images[0]
        self.rect = self.rects[0]


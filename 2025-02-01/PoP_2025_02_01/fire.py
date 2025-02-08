import pygame as pg
from helpers import *

class Fire(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.win_w = win_w
        self.win_h = win_h
        self.images = {}
        self.rects = {}
        for i in range(9):
            image = pg.image.load(f"assets/INTRO/FIRE/res15{i+1}.png").convert_alpha()
            w = image.get_width()
            h = image.get_height()
            image = pg.transform.scale(image, (w * 2, h * 2))
            self.images[i] = image
            rect = image.get_rect()
            rect.centerx = x
            rect.centery = y
            self.rects[i] = rect
        self.current_frame = 0
        self.animation_len = len(self.images)
        self.animation_speed = 9
        self.animation_timer = 0

    def update(self, time_delta):
        self.animation_timer += time_delta
        if self.animation_timer >= 1.0 / self.animation_speed:
            self.current_frame = (self.current_frame + 1) % self.animation_len
            self.animation_timer -= 1.0 / self.animation_speed

    def draw(self, window):
        window.blit(self.images[self.current_frame], self.rects[self.current_frame])


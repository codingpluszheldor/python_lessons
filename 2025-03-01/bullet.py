import pygame as pg
from helper import *

class Bullet(pg.sprite.Sprite):
    def __init__(self, start_x, start_y, group):
        pg.sprite.Sprite.__init__(self)
        self.images = []
        self.rects = []
        for i in range(2):
            image = pg.image.load(f"assets/shoot/shoot{i+1}.png").convert_alpha()
            w = image.get_width() * 2
            h = image.get_height() * 2
            image = pg.transform.scale(image,(w, h))
            rect = image.get_rect()
            self.images.append(image)
            self.rects.append(rect)
        self.image = self.images[0]
        self.rect = self.rects[0]
        self.rect.centerx = start_x
        self.rect.centery = start_y
        self.x = self.rect.centerx
        self.y = self.rect.centery
        self.speed = 7
        self.animation_timer = 0
        self.current_frame = 0
        self.add(group)


    def update(self, time_delta):
        self.animation_timer += time_delta
        if self.animation_timer > 0.2:
            self.current_frame = 0 if self.current_frame == 1 else 1
            self.image = self.images[self.current_frame]
            self.rect = self.rects[self.current_frame]
            self.animation_timer = 0

        self.x += self.speed
        self.rect.centerx = int(self.x)
        self.rect.centery = self.y
        if self.rect.x > win_w:
            self.kill()

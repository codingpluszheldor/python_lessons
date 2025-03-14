import pygame as pg
from helper import *

class Enemy(pg.sprite.Sprite):
    def __init__(self, start_x, start_y, group):
        pg.sprite.Sprite.__init__(self)
        self.images = []
        self.rects = []
        for i in range(5):
            image = pg.image.load(f"assets/enemy/sprites/enemy{i+1}.png").convert_alpha()
            w = image.get_width() * 2
            h = image.get_height() * 2
            image = pg.transform.scale(image,(w, h))
            rect = image.get_rect()
            self.images.append(image)
            self.rects.append(rect)

        self.current_frame = 0
        self.animation_len = len(self.images)
        self.animation_speed = 9
        self.animation_timer = 0
        self.speed = 1.5
        self.image = self.images[0]
        self.rect = self.rects[0]
        self.rect.centerx = start_x
        self.rect.centery = start_y
        self.x = self.rect.centerx
        self.y = self.rect.centery
        self.add(group)

    def update(self, time_delta):
        self.x -= self.speed
        self.rect.centerx = int(self.x)
        self.rect.centery = int(self.y)
        if self.rect.centerx < 0:
            self.kill()
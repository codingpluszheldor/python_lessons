import pygame as pg
from helper import *

class Enemy(pg.sprite.Sprite):
    def __init__(self, start_x, start_y, group):
        pg.sprite.Sprite.__init__(self)
        self.images = []
        self.rects = []
        for i in range(5):
            image = pg.image.load(f"assets/enemy/sprites/enemy{i+1}.png").convert_alpha()
            w = image.get_width()
            h = image.get_height()
            image = pg.transform.scale(image, (w * 2, h * 2))
            self.images.append(image)
            rect = image.get_rect()
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
        self.animation_timer += time_delta
        if self.animation_timer >= 1.0 / self.animation_speed:
            self.current_frame = (self.current_frame + 1) % self.animation_len
            self.animation_timer -= 1.0 / self.animation_speed
        self.image = self.images[self.current_frame]
        self.rect = self.rects[self.current_frame]
        self.x -= self.speed
        self.rect.centerx = int(self.x)
        self.rect.centery = self.y
        if self.rect.centerx < 0:
            self.kill()

    def kill(self):
        self.x = -100
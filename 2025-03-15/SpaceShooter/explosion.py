import pygame as pg
from helper import *

class Explosion(pg.sprite.Sprite):
    def __init__(self, start_x, start_y, group):
        pg.sprite.Sprite.__init__(self)
        self.images = []
        self.rects = []
        for i in range(5):
            image = pg.image.load(f"assets/explosion/sprites/explosion{i+1}.png").convert_alpha()
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
        self.image = self.images[0]
        self.rect = self.rects[0]
        self.rect.centerx = start_x
        self.rect.centery = start_y
        self.x = start_x
        self.y = start_y
        self.set_for_kill = False
        self.add(group)


    def update(self, time_delta):
        self.animation_timer += time_delta
        if self.animation_timer >= 1.0 / self.animation_speed:
            self.current_frame = (self.current_frame + 1) % self.animation_len
            self.animation_timer -= 1.0 / self.animation_speed
        self.image = self.images[self.current_frame]
        self.rect.centerx = self.x
        self.rect.centery = self.y
        if self.current_frame == self.animation_len - 1:
            self.set_for_kill = True
        elif self.set_for_kill == True and self.current_frame == 0:
            self.kill()
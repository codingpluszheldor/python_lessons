import pygame as pg
from helper import *


class Bullet(pg.sprite.Sprite):
    def __init__(self, start_x, start_y, group):
        pg.sprite.Sprite.__init__(self)
        self.images = []
        self.rects = []
        for i in range(2):
            image = pg.image.load(f"assets/shoot/shoot{i + 1}.png").convert_alpha()
            image = pg.transform.scale(image, (image.get_width() * 2, image.get_height() * 2))
            self.images.append(image)
            self.rects.append(image.get_rect())
        self.image = self.images[0]
        self.rect = self.rects[0]
        self.rect.centerx = start_x + 40
        self.rect.centery = start_y
        self.x = self.rect.centerx
        self.y = self.rect.centery
        self.speed = 7
        self.animation_timer = 0
        self.current_frame = 0
        self.add(group)

    # def draw(self, window):
    #     window.blit(self.image, self.rect)

    def update(self, time_delta):
        self.animation_timer += time_delta
        if self.animation_timer > 0.2:
            self.current_frame = 0 if self.current_frame == 1 else 1
            # if self.current_frame == 0:
            #     self.current_frame = 1
            # else:
            #     self.current_frame = 0
            self.image = self.images[self.current_frame]
            self.rect = self.rects[self.current_frame]
            self.animation_timer = 0

        self.x += self.speed
        self.rect.centerx = int(self.x)
        self.rect.centery = self.y
        if self.rect.x > win_w:
            self.kill()

    def kill(self):
        self.x = 1000

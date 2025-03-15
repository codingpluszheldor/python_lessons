import pygame as pg
from helper import *


class Player(pg.sprite.Sprite):
    def __init__(self, start_x, start_y):
        pg.sprite.Sprite.__init__(self)
        self.images = []
        self.rects = []
        for i in range(3):
            image = pg.image.load(f"assets/player/sprites/player{i+1}.png").convert_alpha()
            image = pg.transform.scale(image,(image.get_width() * 2, image.get_height() * 2))
            self.images.append(image)
            self.rects.append(image.get_rect())
        self.image = self.images[0]
        self.rect = self.rects[0]
        self.rect.centerx = start_x
        self.rect.centery = start_y
        self.speed = 5
        self.x = start_x
        self.y = start_y

    def draw(self, window):
        window.blit(self.image, self.rect)

    def update(self, buttons_pressed):
        if buttons_pressed[pg.K_RIGHT]:
            self.image = self.images[0]
            self.rect = self.rects[0]
            if self.x + self.speed < win_w - self.image.get_width() / 2:
                self.x += self.speed
        if buttons_pressed[pg.K_LEFT]:
            self.image = self.images[0]
            self.rect = self.rects[0]
            if self.x - self.speed > 0 + self.image.get_width() / 2:
                self.x -= self.speed
        if buttons_pressed[pg.K_UP]:
            self.image = self.images[2]
            self.rect = self.rects[2]
            if self.y - self.speed > 0 + self.image.get_height() / 2:
                self.y -= self.speed
        if buttons_pressed[pg.K_DOWN]:
            self.image = self.images[1]
            self.rect = self.rects[1]
            if self.y + self.speed < win_h - self.image.get_height() / 2:
                self.y += self.speed
        self.rect.centerx = self.x
        self.rect.centery = self.y

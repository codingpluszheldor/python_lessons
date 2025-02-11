import pygame as pg
from helpers import *

class StateVizir(enum.Enum):
    intro_walk = 0
    intro_idle = 0
class Vizir(pg.sprite.Sprite):
    def __init__(self, x, y, group):
        pg.sprite.Sprite.__init__(self)
        self.win_w = win_w
        self.win_h = win_h
        self.images = {}
        self.rects = {}
        self.images_walk = {}
        self.rects_walk = {}
        self.state = StateVizir.intro_walk
        self.x = x
        for i in range(851, 889):
            image = pg.image.load(f"assets/VIZIR/res{i}.png").convert_alpha()
            w = image.get_width()
            h = image.get_height()
            image = pg.transform.scale(image, (w * 2, h * 2))
            self.images[i-851] = image
            rect = image.get_rect()
            rect.centerx = x
            rect.centery = y
            self.rects[i-851] = rect
            if i >= 851 and i <= 857:
                self.images_walk[i-851] = image
                self.rects_walk[i-851] = rect

        self.current_frame = 0
        self.animation_len = len(self.images_walk)
        self.animation_speed = 5
        self.animation_timer = 0
        self.image = self.images_walk[0]
        self.rect = self.rects_walk[0]
        self.add(group)

    def update(self, time_delta):
        self.animation_timer += time_delta
        if self.animation_timer >= 1.0 / self.animation_speed:
            self.current_frame = (self.current_frame + 1) % self.animation_len
            self.animation_timer -= 1.0 / self.animation_speed
            self.x -= 4.5

        if self.state == StateVizir.intro_walk:
            # self.x -= 0.5
            if self.x < 400:
                self.x = 400
                self.current_frame = 0
                self.state = StateVizir.intro_idle
        elif self.state == StateVizir.intro_idle:
            self.current_frame = 0

        self.image = self.images_walk[self.current_frame]
        self.rects_walk[self.current_frame].centerx = self.x
        self.rect = self.rects_walk[self.current_frame]



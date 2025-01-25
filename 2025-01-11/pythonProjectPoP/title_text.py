import pygame as pg
from helpers import *

class TitleText(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.images = {}
        self.rects = {}
        for i in range(3):
            image = pg.image.load(f"assets/TITLE/res5{i+2}.png").convert_alpha()
            w = image.get_width()
            h = image.get_height()
            image = pg.transform.scale(image, (w * 2, h * 2))
            self.images[i] = image
            rect = image.get_rect()
            rect.centerx = win_w // 2
            rect.centery = win_h // 2 + 77
            self.rects[i] = rect

    def draw(self, window, state=0):
        window.blit(self.images[state], self.rects[state])

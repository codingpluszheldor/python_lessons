import pygame as pg
from helpers import *

class Title(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.win_w = win_w
        self.win_h = win_h
        self.images = {}
        self.rects = {}
        for i in range(2):
            image = pg.image.load(f"assets/TITLE/res{5-i}1.png").convert_alpha()
            image = pg.transform.scale(image, (win_w, win_h))
            self.images[i] = image
            rect = image.get_rect()
            rect.x = 0
            rect.y = 0
            self.rects[i] = rect

    def draw(self, window, state=0):
        window.blit(self.images[state], self.rects[state])
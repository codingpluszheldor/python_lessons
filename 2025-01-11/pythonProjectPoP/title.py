import pygame as pg
from helpers import *

class Title(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.win_w = win_w
        self.win_h = win_h
        self.image = pg.image.load("assets/TITLE/res51.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (win_w, win_h))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def draw(self, window):
        window.blit(self.image, self.rect)
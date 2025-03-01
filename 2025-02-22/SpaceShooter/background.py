import pygame as pg
from helper import *

class Background(pg.sprite.Sprite):
    def __init__(self, file_name, group):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(file_name).convert_alpha()
        self.image = pg.transform.scale(self.image, (win_w, win_h))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.add(group)
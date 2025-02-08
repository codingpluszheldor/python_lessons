import pygame as pg
from helpers import *

class Intro(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.win_w = win_w
        self.win_h = win_h
        self.image_bedroom = pg.image.load(f"assets/INTRO/res951.png").convert_alpha()
        self.image_bedroom = pg.transform.scale(self.image_bedroom, (win_w, win_h))
        self.rect_bedroom = self.image_bedroom.get_rect()
        self.rect_bedroom.x = 0
        self.rect_bedroom.y = 0
        self.image_bed = pg.image.load(f"assets/INTRO/res981.png").convert_alpha()
        self.image_bed = pg.transform.scale(self.image_bed,
                                            (self.image_bed.get_width() * 2,
                                             self.image_bed.get_height() * 2))
        self.rect_bed = self.image_bed.get_rect()
        self.rect_bed.x = 0
        self.rect_bed.y = 285

    def draw(self, window):
        window.blit(self.image_bedroom, self.rect_bedroom)
        window.blit(self.image_bed, self.rect_bed)
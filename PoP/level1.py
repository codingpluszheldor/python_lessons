import pygame as pg

class Level_1(pg.sprite.Sprite):
    def __init__(self, start_x, start_y, group):
        pg.sprite.Sprite.__init__(self)
        self.full_image = pg.image.load("assets/LEVELS/level1.bmp")
        self.image = self.full_image.subsurface(pg.Rect(320, 190, 320, 190))
        self.image = pg.transform.scale(self.image, (640, 380))
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.add(group)
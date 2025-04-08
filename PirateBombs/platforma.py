import pygame as pg

class Platforma(pg.sprite.Sprite):
    def __init__(self, start_x, start_y, group):
        pg.sprite.Sprite.__init__(self)
        self.full_image = pg.image.load(f"assets/8-Tile-Sets/Tile-Sets (64-64).png").convert_alpha()
        self.image = self.full_image.subsurface(pg.Rect(256, 256, 64, 16))
        self.rect = self.image.get_rect()
        self.rect.centerx = start_x
        self.rect.centery = start_y
        self.add(group)

    def update(self, buttons_pressed):
        pass
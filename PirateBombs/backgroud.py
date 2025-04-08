import pygame as pg

class Background(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.full_image = pg.image.load(f"assets/8-Tile-Sets/Tile-Sets (64-64).png").convert_alpha()
        self.brick = self.full_image.subsurface(pg.Rect(192, 0, 192, 192))
        self.oven = self.full_image.subsurface(pg.Rect(0, 0, 192, 192))
        self.rect = self.brick.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.oven_rect = self.oven.get_rect()
        self.oven_rect.x = 0
        self.oven_rect.y = 0

    def draw(self, window):
        w = self.brick.get_width()
        h = self.brick.get_height()
        for x in range(4):
            for y in range(2):
                window.blit(self.brick,
                            (self.rect.x + w * x, self.rect.y + h * y))
        window.blit(self.oven, self.oven_rect)
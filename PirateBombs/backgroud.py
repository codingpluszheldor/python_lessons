import pygame as pg

class Background(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.full_image = pg.image.load(f"assets/8-Tile-Sets/Tile-Sets (64-64).png").convert_alpha()
        self.two_bricks = self.full_image.subsurface(pg.Rect(0, 0, 384, 192))
        self.two_bricks_rect = self.two_bricks.get_rect()
        self.two_bricks_rect.x = 0
        self.two_bricks_rect.y = 0
        self.brick = self.full_image.subsurface(pg.Rect(128, 192, 128, 128))
        self.brick_rect = self.brick.get_rect()
        self.brick_rect.x = 0
        self.brick_rect.y = 0
        self.oven = self.full_image.subsurface(pg.Rect(0, 0, 192, 192))
        self.oven_rect = self.oven.get_rect()
        self.oven_rect.x = 0
        self.oven_rect.y = 0

    def draw(self, window):
        self.two_bricks_rect.x = -128 + 16
        self.two_bricks_rect.y = 0
        window.blit(self.two_bricks, self.two_bricks_rect)
        self.oven_rect.x = 0
        self.oven_rect.y = 192
        window.blit(self.oven, self.oven_rect)
        self.oven_rect.x = 192
        self.oven_rect.y = 192
        window.blit(self.oven, self.oven_rect)
        self.brick_rect.x = 192 + 64
        self.brick_rect.y = 0
        window.blit(self.brick, self.brick_rect)
        self.brick_rect.x = 192 + 64
        self.brick_rect.y = 64
        window.blit(self.brick, self.brick_rect)
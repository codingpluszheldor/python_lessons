import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, start_x, start_y, group):
        pg.sprite.Sprite.__init__(self)
        self.images = []
        self.rects = []
        for i in range(26):
            image = pg.image.load(f"assets/1-Player-Bomb Guy/1-Idle/{i + 1}.png").convert_alpha()
            self.images.append(image)
            self.rects.append(image.get_rect())
        self.image = self.images[0]
        self.rect = self.rects[0]
        self.rect.centerx = start_x
        self.rect.centery = start_y
        self.speed = 5
        self.add(group)

    def update(self, buttons_pressed):
        if buttons_pressed[pg.K_RIGHT]:
            self.rect.centerx += self.speed
        if buttons_pressed[pg.K_LEFT]:
            self.rect.centerx -= self.speed
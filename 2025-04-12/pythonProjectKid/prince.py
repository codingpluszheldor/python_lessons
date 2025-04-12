import pygame as pg

class Prince(pg.sprite.Sprite):
    def __init__(self, start_x, start_y, group):
        pg.sprite.Sprite.__init__(self)
        self.images_run_left = []
        self.rects_run_left = []
        for i in range(401, 415):
            image = pg.image.load(f"assets/KID/res{i}.png").convert_alpha()
            image = pg.transform.scale(image, (image.get_width() * 2,
                                                   image.get_height() * 2))
            self.images_run_left.append(image)
            self.rects_run_left.append(image.get_rect())

        self.image = self.images_run_left[0]
        self.rect = self.rects_run_left[0]
        self.rect.centerx = start_x
        self.rect.centery = start_y
        self.add(group)
import pygame as pg

class Prince(pg.sprite.Sprite):
    def __init__(self, start_x, start_y, group):
        pg.sprite.Sprite.__init__(self)
        self.images_run_left = []
        self.rects_run_left = []
        self.image_idle = pg.image.load(f"assets/KID/res401.png").convert_alpha()
        self.image_idle = pg.transform.scale(self.image_idle,
                                             (self.image_idle.get_width() * 2,
                                             self.image_idle.get_height() * 2))
        self.rect_idle = self.image_idle.get_rect()

        for i in range(405, 414):
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
        self.animation_timer = 0.0
        self.animation_speed = 14
        self.animation_len = len(self.images_run_left)
        self.current_frame = 0
        self.x = start_x
        self.y = start_y

    def update(self, time_delta, buttons_pressed):
        if buttons_pressed[pg.K_LEFT]:
            self.animation_timer += time_delta
            if self.animation_timer >= 1.0 / self.animation_speed:
                self.current_frame = (self.current_frame + 1) % self.animation_len
                self.animation_timer -= 1.0 / self.animation_speed
            self.image = self.images_run_left[self.current_frame]
            self.rect = self.rects_run_left[self.current_frame]
            self.rect.centerx = self.x
            self.rect.centery = self.y
        else:
            self.animation_timer = 0
            self.current_frame = 0
            self.image = self.image_idle
            self.rect = self.rect_idle
            self.rect.centerx = self.x
            self.rect.centery = self.y

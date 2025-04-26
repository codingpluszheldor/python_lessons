import pygame as pg
import enum


def load_assets_image(file_name, flip=False):
    image = pg.image.load(file_name).convert_alpha()
    image = pg.transform.scale(image,(image.get_width() * 2,
                                          image.get_height() * 2))
    if flip:
        image = pg.transform.flip(image, True, False)

    rect = image.get_rect()
    return image, rect

# Направление
class Direction(enum.Enum):
    left = 0,
    right = 1

class Prince(pg.sprite.Sprite):
    def __init__(self, start_x, start_y, group):
        pg.sprite.Sprite.__init__(self)
        self.images_run_left = []
        self.rects_run_left = []
        self.images_run_right = []
        self.rects_run_right = []
        self.image_idle = pg.image.load(f"assets/KID/res401.png").convert_alpha()
        self.image_idle_left = pg.transform.scale(self.image_idle,
                                             (self.image_idle.get_width() * 2,
                                             self.image_idle.get_height() * 2))
        self.rect_idle_left = self.image_idle_left.get_rect()
        self.image_idle_right = pg.transform.flip(self.image_idle_left, True, False)
        self.rect_idle_right = self.image_idle_right.get_rect()
        # Падение
        self.image_fall_left, self.rect_fall_left = load_assets_image("assets/KID/res516.png")
        self.image_fall_right, self.rect_fall_right = (
            load_assets_image("assets/KID/res516.png", True))

        for i in range(405, 414):
            image = pg.image.load(f"assets/KID/res{i}.png").convert_alpha()
            image = pg.transform.scale(image, (image.get_width() * 2,
                                                   image.get_height() * 2))
            self.images_run_left.append(image)
            self.rects_run_left.append(image.get_rect())
            image_run_right = pg.transform.flip(image, True, False)
            self.images_run_right.append(image_run_right)
            self.rects_run_right.append(image_run_right.get_rect())

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
        self.direction = Direction.left
        self.speed_x = 2


    def count_animation_frame(self, images, rects, animation_len, time_delta):
        self.animation_timer += time_delta
        if self.animation_timer >= 1.0 / self.animation_speed:
            self.current_frame = (self.current_frame + 1) % animation_len
            self.animation_timer -= 1.0 / self.animation_speed
        self.image = images[self.current_frame]
        self.rect = rects[self.current_frame]
        self.rect.centerx = self.x
        self.rect.centery = self.y


    def update(self, time_delta, buttons_pressed):
        if buttons_pressed[pg.K_LEFT]:
            self.direction = Direction.left
            self.x -= self.speed_x
            self.count_animation_frame(self.images_run_left,
                                       self.rects_run_left,
                                       self.animation_len, time_delta)
        elif buttons_pressed[pg.K_RIGHT]:
            self.direction = Direction.right
            self.x += self.speed_x
            self.count_animation_frame(self.images_run_right,
                                       self.rects_run_right,
                                       self.animation_len, time_delta)
        else:
            self.animation_timer = 0
            self.current_frame = 0
            if self.direction == Direction.left:
                self.image = self.image_idle_left
                self.rect = self.rect_idle_left
            else:
                self.image = self.image_idle_right
                self.rect = self.rect_idle_right
            self.rect.centerx = self.x
            self.rect.centery = self.y
        print(f"x={self.x}")
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
        self.group = group
        self.is_jump = False

    def update(self, buttons_pressed):
        platforma = self.group.sprites()[1]
        if buttons_pressed[pg.K_RIGHT]:
            self.rect.centerx += self.speed
        if buttons_pressed[pg.K_LEFT]:
            self.rect.centerx -= self.speed

        if buttons_pressed[pg.K_UP] and self.is_jump == False:
            self.rect.centery -= self.speed * 15
            self.is_jump = True
        else:
            if self.rect.colliderect(platforma.rect):
                print("colliderect")
                self.is_jump = False
            else:
                self.rect.centery += self.speed
                if self.rect.y + self.image.get_height() > 192:
                    self.rect.y = 192 - self.image.get_height()
                    self.is_jump = False
import pygame as pg
from helpers import *
from title import *
from title_text import *

pg.init()
window = pg.display.set_mode((win_w, win_h))
clock = pg.time.Clock()

# Создание спрайтов
title = Title()
title_text = TitleText()
# Загрузка звуков
sound_title = pg.mixer.Sound("assets/SOUNDS/101_-_Prince_of_Persia_-_DOS_-_Prologue_A.wav")
sound_title.play()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    buttons_pressed = pg.key.get_pressed()
    title.draw(window)
    title_text.draw(window, 0)
    pg.display.flip()

pg.quit()
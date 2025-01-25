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
# Задание состояний
state = StateIntro.intro_0
intro_text_cnt = 0
intro_title_cnt = 0
timer_event = pg.USEREVENT
pg.time.set_timer(timer_event, 2000)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == timer_event:
            if state == StateIntro.intro_0:
                timer_event = pg.USEREVENT + 1
                pg.time.set_timer(timer_event, 5000)
                state = StateIntro.intro_1
            elif state == StateIntro.intro_1:
                timer_event = pg.USEREVENT + 2
                pg.time.set_timer(timer_event, 2000)
                state = StateIntro.intro_2
            elif state == StateIntro.intro_2:
                timer_event = pg.USEREVENT + 3
                pg.time.set_timer(timer_event, 5000)
                state = StateIntro.intro_3
                intro_text_cnt += 1
            elif state == StateIntro.intro_3:
                timer_event = pg.USEREVENT + 4
                pg.time.set_timer(timer_event, 2000)
                state = StateIntro.intro_4
            elif state == StateIntro.intro_4:
                timer_event = pg.USEREVENT + 5
                pg.time.set_timer(timer_event, 8000)
                state = StateIntro.intro_5
                intro_text_cnt += 1
            elif state == StateIntro.intro_5:
                sound_title.stop()
                state = StateIntro.intro_6
                intro_title_cnt += 1
                intro_text_cnt += 1

    buttons_pressed = pg.key.get_pressed()
    title.draw(window, intro_title_cnt)
    if state.value < StateIntro.intro_7.value:
        if (state == StateIntro.intro_1 or
            state == StateIntro.intro_3 or
            state == StateIntro.intro_5 or state == StateIntro.intro_6):
            title_text.draw(window, intro_text_cnt)
    pg.display.flip()

pg.quit()
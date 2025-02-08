import pygame as pg
from helpers import *
from title import *
from title_text import *
from intro import *
from fire import *

pg.init()
window = pg.display.set_mode((win_w, win_h))
clock = pg.time.Clock()

# Создание спрайтов
title = Title()
title_text = TitleText()
intro = Intro()
fire = Fire(win_w // 2, win_h // 2)
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
                timer_event = pg.USEREVENT
                pg.time.set_timer(timer_event, 500)
                state = StateIntro.intro_1
            elif state == StateIntro.intro_1:
                timer_event = pg.USEREVENT
                pg.time.set_timer(timer_event, 200)
                state = StateIntro.intro_2
            elif state == StateIntro.intro_2:
                timer_event = pg.USEREVENT
                pg.time.set_timer(timer_event, 500)
                state = StateIntro.intro_3
                intro_text_cnt += 1
            elif state == StateIntro.intro_3:
                timer_event = pg.USEREVENT
                pg.time.set_timer(timer_event, 200)
                state = StateIntro.intro_4
            elif state == StateIntro.intro_4:
                timer_event = pg.USEREVENT
                pg.time.set_timer(timer_event, 800)
                state = StateIntro.intro_5
                intro_text_cnt += 1
            elif state == StateIntro.intro_5:
                sound_title.stop()
                timer_event = pg.USEREVENT
                pg.time.set_timer(timer_event, 100)
                state = StateIntro.intro_6
                intro_text_cnt += 1
                intro_title_cnt += 1
            elif state == StateIntro.intro_6:
                state = StateIntro.intro_7
                intro_text_cnt += 1
                timer_event = pg.USEREVENT
                pg.time.set_timer(timer_event, 100)
            elif state == StateIntro.intro_7:
                state = StateIntro.intro_8
                intro_text_cnt += 1
                timer_event = pg.USEREVENT
                pg.time.set_timer(timer_event, 100)
            elif state == StateIntro.intro_8:
                state = StateIntro.intro_9
                timer_event = pg.USEREVENT
                pg.time.set_timer(timer_event, 100)


    buttons_pressed = pg.key.get_pressed()
    window.fill((0, 0, 0))
    if state.value < StateIntro.intro_9.value:
        title.draw(window, intro_title_cnt)
        if (state == StateIntro.intro_1 or
            state == StateIntro.intro_3 or
            state == StateIntro.intro_5 or
            state == StateIntro.intro_6 or
            state == StateIntro.intro_7 or state == StateIntro.intro_8):
            title_text.draw(window, intro_text_cnt)
    elif state == StateIntro.intro_9:
        intro.draw(window)
    fire.draw(window)


    pg.display.flip()
    time_delta = clock.tick(fps) / 1000.0
    fire.update(time_delta)

pg.quit()
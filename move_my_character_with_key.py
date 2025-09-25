from pico2d import *

open_canvas(800,600)

bg=load_image('TUK_GROUND.png')
character=load_image('korea_player_left.png')
c_idle=load_image('player_idle_left.png')

x,y=400,300

def bg_n_face():
    global x, y
    face_frame = 0
    clear_canvas()
    bg.clip_draw(0, 0, 1280, 1024, 400, 300, 800, 600)
    character.clip_draw(0, 0, 100, 100, x, y)
    update_canvas()

while True:
    bg_n_face()
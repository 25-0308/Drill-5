from pico2d import *

open_canvas(800,600)

bg=load_image('TUK_GROUND.png')
character=load_image('korea_player_left.png')
c_idle=load_image('player_idle_left.png')

x,y=400,300
running = True

def handle_events():
    global x, y
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                if x > 50:
                    x -= 10
            elif event.key == SDLK_RIGHT:
                if x < 750:
                    x += 10
            elif event.key == SDLK_UP:
                if y < 550:
                    y += 10
            elif event.key == SDLK_DOWN:
                if y > 80:
                    y -= 10
            elif event.key == SDLK_ESCAPE:
                running = False

def bg_n_face():
    global x, y
    face_frame = 0
    clear_canvas()
    bg.clip_draw(0, 0, 1280, 1024, 400, 300, 800, 600)
    character.clip_draw(0, 0, 100, 100, x, y)
    print(x, y)
    update_canvas()

while True:
    bg_n_face()
    handle_events()
    if not running:
        break
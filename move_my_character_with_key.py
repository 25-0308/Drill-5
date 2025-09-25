from pico2d import *

open_canvas(800,600)

bg=load_image('TUK_GROUND.png')
character=load_image('korea_player_left.png')
c_idle=load_image('player_idle_left.png')
c_run=load_image('player_run_left.png')
c_updown=load_image('player_updown.png')

x,y=400,300
running = True
idle_bool=True

def handle_events():
    global x, y
    global running
    global idle_bool
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                if x > 50:
                    idle_bool = False
                    x -= 10
            elif event.key == SDLK_RIGHT:
                if x < 750:
                    idle_bool = False
                    x += 10
            elif event.key == SDLK_UP:
                if y < 550:
                    idle_bool = False
                    y += 10
            elif event.key == SDLK_DOWN:
                if y > 70:
                    idle_bool = False
                    y -= 10
            elif event.key == SDLK_ESCAPE:
                running = False

def handle_animation():
    global x, y
    clear_canvas()
    bg.clip_draw(0, 0, 1280, 1024, 400, 300, 800, 600)
    character.clip_draw(0, 0, 100, 100, x, y)
    if idle_bool:
        idle()
    update_canvas()

def idle():
    global x, y
    idle_frame = 0
    for i in range(6):
        c_idle.clip_draw(idle_frame*93, 0, 92, 33, x, y-50)
        idle_frame = (idle_frame + 1) % 6
        delay(0.05)
        update_canvas()

while True:
    handle_animation()

    handle_events()
    if not running:
        break
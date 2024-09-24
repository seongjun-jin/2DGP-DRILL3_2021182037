from pico2d import *

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')

def run_circle():
    clear_canvas_now()
    boy.draw_now(400,300)
    delay(5)

def run_Rectangle():
    
    pass

while True:
    run_circle()
    run_Rectangle()
    break
    

close_canvas()

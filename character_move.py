from pico2d import *
import math

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')

def run_circle():
    r, cx, cy = 300, 800//2, 600//2
    
    for degree in range(0, 360, 5):
        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
        
        clear_canvas_now()
        boy.draw_now(x,y)
        delay(0.01)
def run_top():
    print("TOP")
    pass

def run_right():
    print("RIGHT")
    pass

def run_left():
    print("LEFT")
    pass

def run_bottom():
    print("BOTTOM")
    pass

def run_Rectangle():
    run_top()
    run_right()
    run_bottom()
    run_left()
    

while True:
    #run_circle()
    run_Rectangle()
    break
    

close_canvas()

from pico2d import *
import math

open_canvas()

boy = load_image('character.png')
grass = load_image('grass.png')

def draw_boy(x,y):
    clear_canvas_now()
    boy.draw_now(x,y)
    delay(0.01)

def run_circle():
    r, cx, cy = 300, 800//2, 600//2
    
    for degree in range(0, 360, 5):
        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
        draw_boy(x,y)
        
def run_top():
    for x in range(0, 800, 10):
        draw_boy(x,550)
    
def run_right():
    for y in range(550, 0, -10):
        draw_boy(790, y)

def run_bottom():
    for x in range(800, 0, -10):
        draw_boy(x,10)

def run_left():
    for y in range(0, 550, 10):
        draw_boy(10, y)

def run_Rectangle():
    run_top()
    run_right()
    run_bottom()
    run_left()
    
def run_trileft():
    for z in range(0, 400, 10):
        x = z
        y = z
        draw_boy(x,y)
            
def run_triright():
    for z in range(0, 400, 10):
        x = 400 + z
        y = 400 -z
        draw_boy(x,y)

def run_triangle():
    run_bottom()
    run_trileft()
    run_triright()
    
while True:
    run_circle()
    run_Rectangle()
    run_triangle()
    break
    

close_canvas()

from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 0
rec = True;
cir = False;

while(True):
        while(rec == True):
            while(x < 800):
                clear_canvas_now()
                grass.draw_now(400, 30)
                character.draw_now(x, 90)
                x = x + 5
                delay(0.01)

            if(x == 800):
                while(y < 500):
                    clear_canvas_now()
                    grass.draw_now(400, 30)
                    character.draw_now(800, 90 + y)
                    y = y + 5
                    delay(0.01)
                
            if(y == 500):
                while(x > 0):
                    clear_canvas_now()
                    grass.draw_now(400, 30)
                    character.draw_now(x, 90 + y)
                    x = x - 5
                    delay(0.01)
                
            if(x == 0):
                while(y > 0):
                    clear_canvas_now()
                    grass.draw_now(400, 30)
                    character.draw_now(x, 90 + y)
                    y = y - 5
                    delay(0.01)
                    rec = False
                    cir = True

        while(cir == True):
                while(x < 360):
                    clear_canvas_now()
                    grass.draw_now(400, 30)
                    character.draw_now(200 * math.sin(x) + 400, 200 * math.cos(x) + 90)
                    x = x + 5
                    delay(0.01)
                    rec = True
                    cir = False
               
close_canvas()

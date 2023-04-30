from vpython import *

back  = canvas(title = "Pascasls law", width=1200, height = 600)

container1 = cylinder(pos = vec(-5,0,0), axis = vec(0,10,0), radius = 4, opacity = 0.3, color = color.white)
water1  = cylinder(pos = vec(-5,0,0), axis = vec(0,7,0), radius = 4, color = color.blue)

container2 = cylinder(pos = vec(5,0,0), axis = vec(0,10,0), radius = 4, opacity = 0.3, color = color.white)
water2  = cylinder(pos = vec(5,0,0), axis = vec(0,0,0), radius = 4, color = color.blue)

pipee = cylinder( pos = vec(5,4,0), axis = water1.pos - water2.pos, radius = .2)

deltaY = 0
water1_height = 7
water2_height = 0

def reset_sim():
    global deltaY, water1_height, water2_height
    deltaY = 0
    water1_height = 7
    water2_height = 0

   

def start_sim():
    global deltaY
    deltaY = 0.1

def stop_sim():
    global deltaY
    deltaY = 0
    


start_button = button(bind=start_sim, text='Start',  height=40, width=80)
stop_button = button(bind=stop_sim, text='Stop',  height=40, width=80, color=color.red, background=color.white, right=100)
reset_button = button(bind=reset_sim, text ="Reset", height =40, width = 80, color=color.green,background=color.white,right = 200 )

while True:
    rate(10)

    water1_height = water1_height - deltaY
    water2_height = water2_height + deltaY

    if water1_height <= water2_height :
        deltaY = 0
       # water1_height = 0
        

    water1.axis = vec(0,water1_height,0)
    water2.axis = vec(0,water2_height,0)
    

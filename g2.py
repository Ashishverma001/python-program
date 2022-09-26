from tokenize import cookie_re
from turtle import color
import pgzrun

HEIGTH = 500 
WEIDTH = 1000

C = Actor('duck',(100,100))
w = Actor('rabbit',(400,400))


def draw():
    screen.blit('big', poss=(0,0))
    C.draw()
    w.draw()
    screen.draw.text("A duck story",(10,10),color="red")
    screen.draw.text(f"score: {score}",(900,10),color="red")
    cake.draw


def update(): 
    if keyboard.W:
        C.x -= speed
    elif keyboard.S:
        C.x += speed
    elif keyboard.A:
        C.y -= speed
    elif keyboard.D:
        C.y += speed
    else:
        C.angle = 0
         
      
    pgzrun.go()
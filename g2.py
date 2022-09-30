import pgzrun
from  random import randint

HEIGTH = 750
WEIDTH = 900

C = Actor('duck',(100,100))
w = Actor('rabbit',(400,400))
cake = Actor('cake',(randint(100,800),randint(100,500)))
score = 0# variable(global)
speed = 5 

def draw():
    # screen.fill('purpule')
    screen.blit('big', pos=(0,0))
    C.draw()
    w.draw()
    screen.draw.text("Tekken : Amimal Fight",(10,10),color="red")
    screen.draw.text(f"score: {score}",(700,10),color="black")
    cake.draw


def update(): 
    global score
    if keyboard.W:
        C.y -= 4
    elif keyboard.S:
        C.y += 4
    elif keyboard.A:
        C.x -= 4
    elif keyboard.D:
        C.x += 4

    if keyboard.up:
        w.y -= 3 
    elif keyboard.down:
        w.y += 3 
    elif keyboard.left:
        w.x -= 3
    elif keyboard.right:
        w.x += 3
    
    if C.colliderect(cake):
        score += 1
        cake.pos = (randint(100,800),randint(100,500))
         
      
pgzrun.go()
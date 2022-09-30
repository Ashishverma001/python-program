import pgzrun

width = 1000 
heigth = 500 

p = Actor('rabbit',(100,100))
e = Actor("duck",(500,200))

p.speed = 3
e.speed = 2 
gameover = False

def player_movement():
    if keyboard.W:
        p.y -= p.speed
    elif keyboard.S:
        p.y += p.speed
    elif keyboard.A:
        p.x -= p.speed
    elif keyboard.D:
        p.x += p.speed

    # Handling the Border of the player
    if p.x < 0 : 
        p.x = width
    if p.x > width:
        p.x = 0 
    if p.y > heigth:
        p.y = 0
    if p.y < 0 :
        p.y = heigth

def enemy_movement(): 
    if p.y > e.y:
        e.y += e.speed 
    if p.y <= e.y:
        e.y -= e.speed 
    if p.x > e.x:
        e.x += e.speed 
    if p.x <= e.x:
        e.x -= e.speed 

def check_collision():
    global gameover
    if e.colliderect(p):
        p.image = 'cake'
        gameover = True

def draw():
    if not gameover:
        screen.clear()
        e.draw()
        p.draw()
    else:
        screen.fill("crimson")
        screen.draw.text("Game Over",center = (width//2,heigth//2),color = 'white',fontsize = 100)

def update():
    player_movement()
    enemy_movement()
    check_collision()

           
pgzrun.go()

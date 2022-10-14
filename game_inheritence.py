import pgzrun 

width = 800 
heigth = 500 

# all the calss logic
class player(Actor):
    
    # override the default constructor
    def __init__(self, image, speed):
        pos = ri(0, width), ri(0, heigth)
       

    def move(self):
        if keyboard.W:
         self.y -= self.speed
        elif keyboard.S:
         self.y += self.speed
        elif keyboard.A:
         self.x -= self.speed
         self.angle = +10
        elif keyboard.D:
         self.x += self.speed
         self.angle = -10
        else:
            self.angle = 0
    
    def check_boundry(self):
        if self.x < 0 : 
          self.x = width
        if self.x > width:
          self.x = 0 
        if self.y > heigth:
         self.y = 0
        if self.y < 0 :
          self.y = heigth

    
# main game code 

p = player('ironman',3)
print(dir(p))
def draw():
    screen.fill('black')
    p.draw()

def update():
    p.move()
    p.check_boundry()

pgzrun.go()
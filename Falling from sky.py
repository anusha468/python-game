'''
FALLING FROM SKY GAME
use left button to move player left 
use right button to move player right
space bar to make player jump
eat the cake to collect 10 points each
avoid doreamon to lose points and lives
'''
import turtle
import random
import playsound
import time

score=0
lives=3
GROUND_LEVEL = -250
GRAVITY = -0.8

images=["doraemon.gif","Z.gif","cake.gif","bg.gif"]
for image in images:
    turtle.register_shape(image)

wn=turtle.Screen()
wn.title("FALLING FROM SKY")
wn.bgpic("bg.gif")
wn.setup(width=1366,height=768)
wn.tracer(0)#shuts off screen update

#player
player=turtle.Turtle() #turtle is module  #Turtle is class
player.speed(0)#animation speed
player.shape("Z.gif")
player.penup()
player.goto(0,-250)
player.direction="stop"
player.speed(0)
player.shape("Z.gif")
player.height=20
player.penup()
player.dy = 0 #speed top and bottom
player.dx = 0 #speed left and right
player.state = "ready"
player.goto(-140, GROUND_LEVEL + player.height / 2)

cakes=[]

#cake
for _ in range(20):
    cake=turtle.Turtle() #turtle is module  #Turtle is class
    cake.speed(0)
    cake.shape("cake.gif")
    cake.penup()
    cake.goto(-100,250)
    cake.speed=random.randint(2,5)
    cakes.append(cake)
    
doreamons=[]

#bad guy
for _ in range(20):
    doreamon=turtle.Turtle() #turtle is module  #Turtle is class
    doreamon.speed(0)
    doreamon.shape("doraemon.gif")
    doreamon.penup()
    doreamon.goto(100,250)
    doreamon.speed=random.randint(2,5)
    doreamons.append(doreamon)

#make pen        
pen=turtle.Turtle()
pen.speed(0)
pen.ht()
pen.shape("square")
pen.color("blue")
pen.penup()
pen.goto(30,150)
pen.write("FALLING FROM SKY GAME",align="center",font=("Arial", 40, "bold"))
pen.goto(0,-80)
pen.color("black")
pen.write("""
--> = move right
<-- = move left
space bar = jump
Eat cakes to collect 10 points 
Avoid doreamons to lose points and lives""",align="center",font=("Courier", 20, "bold italic"))
pen.goto(20,-220)
pen.color("red")
pen.write("Let's Play",align="center",font=("Helvetica", 50, "bold italic"))
time.sleep(5)
pen.clear()
pen.goto(0,300)
pen.color("blue")
pen.write("Score={}  Lives={}".format(score,lives),align="center",font=("Helvetica", 25, "bold italic"))

def jump():
    if player.state == "ready":
        player.dy = 12
        player.state = "jumping"
    
wn.listen()
wn.onkeypress(jump, "space")


def right():
    player.direction="right"
    
def left():
    player.direction="left"
    
def move_player():
    if player.direction=="left":
        x=player.xcor()
        x-=3
        player.setx(x)
    
    if player.direction=="right":
        x=player.xcor()
        x+=3
        player.setx(x)
    
    # Check for border collisions
    if player.xcor() < -390:
        player.setx(-390)
        
    elif player.xcor() > 390:
        player.setx(390)

#keyboard binding
wn.listen()
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")
        
def cake_out():#cake out of screen
    y=cake.ycor() 
    global score,lives
    if y<-300:
        x=random.randint(-300,300)
        y=random.randint(400,800)
        cake.goto(x,y)
    
    if cake.distance(player)<50: #collision
        playsound.playsound("Slurp+3.mp3",False)
        x=random.randint(-300,300)
        y=random.randint(400,800)
        cake.goto(x,y)
        score+=10
        pen.undo()
        pen.write("Score={}  Lives={}".format(score,lives),align="center",font=("Helvetica", 25, "bold italic"))
    


def doreamon_out():
    y=doreamon.ycor()
    global score,lives
    if y<-300:  
        x=random.randint(-300,300)
        y=random.randint(400,800)
        doreamon.goto(x,y)
            
    if doreamon.distance(player)<50:
        playsound.playsound("Scream+3.mp3",False)
        x=random.randint(-300,300)
        y=random.randint(400,800)
        doreamon.goto(x,y)
        score-=10
        lives-=1
        pen.undo()
        pen.write("Score={}  Lives={}".format(score,lives),align="center",font=("Helvetica", 35, "bold italic"))

#playbg music
playsound.playsound("funny.mp3",False)



#main game loop
while True:  
    # Gravity
    player.dy += GRAVITY #gracity will reduce dy
    
    # Move the player
    y = player.ycor()
    y += player.dy
    player.sety(y)
    
    # Deal with the ground
    if player.ycor() < GROUND_LEVEL + player.height / 2:
        player.sety(GROUND_LEVEL + player.height / 2)
        player.dy = 0
        player.state = "ready"
    wn.update()  
    
    
       
    #move player
    move_player()
   

    #move cake
    for cake in cakes:
        cake.sety(cake.ycor()-cake.speed)
        
    #check off the screen
        cake_out()
            
    #bad  guy   
    for doreamon in doreamons:
        doreamon.sety(doreamon.ycor()-doreamon.speed)
        y=doreamon.ycor()
            
        doreamon_out()
      
    
    if lives<=0:
        time.sleep(1.5)
        pen.clear()
        pen.color("orange")
        wn.clear()
        wn.bgpic("bgg.gif")
        pen.goto(0,-150)
        pen.write("Game over!",align="center",font=("Arial",60,"bold"))
        pen.goto(0,-300)
        pen.write("Your score:{}".format(score),align="center",font=("Arial",55,"bold"))
        time.sleep(2)  
        exit()

wn.mainloop()
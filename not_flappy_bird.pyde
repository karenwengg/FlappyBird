import random
yspeed = 0
PipeX1= 400
PipeX2 = 600
PipeX3 = 800

opening1 = random.randint(100, 400)
opening2 = random.randint(100, 400)
opening3 = random.randint(100, 400)

score = 0
highscore = 0
flycounter = 0
BirdY= 100
x = 100
#Mode 1 = Instruction screen
#Mde 2 = Flappy bird game board
#Mode 3 = Game over screen
mode = 1


def setup():
    size(600,600)
    frameRate(60)
    
def draw():
    global BirdY,mode, flycounter
    if mode == 1:
        background(0,255,255)
        fill(0,255,0)
        stroke(124,252,0)
        rect(0,590,600,10)
        stroke(124,252,0)
        fill(0,240,0)
        fill(0,0,0)
        textSize(30)
        text("Welcome to Flappybird!",135,50)
        text("------------------------",100,70)
        textSize(30)
        text("Instructions:",210,100)
        textSize(25)
        text("Try to navigate the bird through the pipes",50,140)
        textSize(18)
        text("To fly up, press the spacebar, the up arrow or click the mouse",35,170)
        text("If you don't click or press anything, the bird will fall",80,200)
        textSize(15)
        text("The game will end if the bird hits the pipe, goes too high or hits the ground",25,230)
        textSize(20)
        text("Your score increases for every pipe you fly through", 50,265)
        text("Try to get the highest score!",155,300)
        textSize(25)
        text("Click the mouse or spacebar to start", 85, 370)
    
    if mode == 2:
        background(0,255,255)
        fill(255,255,0)
        if flycounter == 0:
            BirdY += 3
        else:
            BirdY -= 3
            flycounter -= 1
            
        ellipse(x,BirdY,30,30)
        stroke(0,0,0)
        pipes()
        ifhit()
        scoreboard()
        # print (BirdY, "BIRDD")
        if BirdY>575 or BirdY< 0: #does it go off screen or hit the ground
           mode = 3
        
    if mode == 3:
        background(0,255,255)
        pipes()
        scoreboard()
        ifhit()
        textSize(30)
        fill(255,0,0)
        text("GAME OVER",200,300)
        textSize(20)
        text("Press r to play again",185,325)
        

        
def pipes(): 
    global PipeX1, PipeX2, PipeX3, opening1, opening2, opening3
 
    fill(0,255,0)
    rect(PipeX1,0,50,opening1)
    rect(PipeX2,0,50,opening2)
    rect(PipeX3,0,50,opening3)

    rect(PipeX1,opening1+100,50,600)
    rect(PipeX2,opening2+100,50,600)
    rect(PipeX3,opening3+100,50,600)
    fill(0,240,0)
    rect(0,590,600,10)
    
    if PipeX1 >0:
        PipeX1 -= 1 
    if PipeX1 == 0:
        PipeX1 = 600
        opening1 = random.randint(100, 400)
    if PipeX2 >0:
        PipeX2 -= 1 
    if PipeX2 == 0:
        PipeX2 = 600
        opening2 = random.randint(100, 400)
    if PipeX3 >0:
        PipeX3 -= 1 
    if PipeX3 == 0:
        PipeX3 = 600
        opening3 = random.randint(100, 400)
    print(PipeX1, "PIPPEEE 1111")
    print(PipeX2, "PIPPEEE 2222")
    print(PipeX3, "PIPPEEE 3333")

def mousePressed():
    global mode, BirdY, flycounter
    if mode == 1:
        mode = 2
    elif mode == 2:
        flycounter = 15
    
def keyPressed():     
    global BirdY, mode, PipeX1, PipeX2, PipeX3, opening1, opening2, opening3, score, flycounter
    if key == ' ' and mode == 1:
        BirdY = 100
        mode = 2
        PipeX1= 400
        PipeX2 = 600
        PipeX3 = 800
        opening1 = random.randint(100, 400)
        opening2 = random.randint(100, 400)
        opening3 = random.randint(100, 400)
    elif (key == ' ' or "UP") and mode == 2:
        flycounter = 15
    if key == "r":
        mode = 1
        score = 0

def ifhit():
    global BirdY, PipeX1, PipeX2, PipeX3,mode,opening1, opening2,opening3
    if (x+20 == PipeX1):
        if BirdY < opening1 or BirdY > opening1+100:
            mode = 3
    if (x+20 == PipeX2):
        if BirdY < opening2 or BirdY > opening2+100:
            mode = 3
    if (x+20 == PipeX3):
        if BirdY < opening3 or BirdY > opening3+100:
            mode = 3
            
    if x > PipeX1 and x < PipeX1+50 and (BirdY < opening1+15 or BirdY > opening1+85):
        mode = 3
    if x > PipeX2 and x < PipeX2+50 and (BirdY < opening2+15 or BirdY > opening2+85):
        mode = 3
    if x > PipeX3 and x < PipeX3+50 and (BirdY < opening3+15 or BirdY > opening3+85):
        mode = 3
        
def scoreboard():
    global score, highscore
    if (x == PipeX1+51 or x == PipeX2+51 or x == PipeX3+51) and mode ==2:
        score += 1
    if score>highscore:
        highscore = score
        
    fill(255)
    if mode == 2:
        text("score:", 75, 75)
        text(score, 170, 75)
    elif mode == 3:
        text("Score:", 225, 400)
        text(score, 290, 400)
        text("highscore:", 225, 450)
        text(highscore, 330, 450)

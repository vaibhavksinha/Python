#1st python game PONG
from tkinter import CENTER
import turtle

sc = turtle.Screen()
sc.title("Ping Pong")
sc.bgcolor("gray")
sc.setup(width=1000,height=500)
sc.tracer(0)

# Score
sc_1=0
sc_2=0

# paddle 1()
bat_1=turtle.Turtle()
bat_1.speed(0)
bat_1.shape("square")
bat_1.color("black")
bat_1.shapesize(stretch_wid=5,stretch_len=1)
bat_1.penup()
bat_1.goto(-470,0)

# paddle 2()
bat_2=turtle.Turtle()
bat_2.speed(0)
bat_2.shape("square")
bat_2.color("black")
bat_2.shapesize(stretch_wid=5,stretch_len=1)
bat_2.penup()
bat_2.goto(470,0)

#ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx=0.15 
ball.dy=-0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,210)
pen.write("Player 1 = 0  Player 2 = 0", align="center", font=("Courier" ,20 ,"normal"))

# Pen1
pen1 = turtle.Turtle()
pen1.speed(0)
pen1.color("yellow")
pen1.penup()
pen1.hideturtle()


#function
def bat_1_up():
    y=bat_1.ycor()
    y+=25
    bat_1.sety(y)

def bat_1_down():
    y=bat_1.ycor()
    y-=25
    bat_1.sety(y)

def bat_2_up():
    y=bat_2.ycor()
    y+=25
    bat_2.sety(y)

def bat_2_down():
    y=bat_2.ycor()
    y-=25
    bat_2.sety(y)

def game_pause():
    if game_play() == 1:
        return
    pen1.goto(0,100)
    ball.dx=0
    ball.dy=-0
    pen1.write("GAME PAUSED press 'P' to continue", align="center", font=("Courier" ,25 ,"bold italic",))   

def game_play():
    ball.dx=0.15
    ball.dy=-0.15
   
# key binding
sc.listen()
sc.onkeypress(bat_1_up,"w")
sc.onkeypress(bat_1_down,"s")
sc.onkeypress(bat_2_up,"Up")
sc.onkeypress(bat_2_down,"Down")
sc.onkeypress(game_pause,"space")
sc.onkeypress(game_play,"p")

#main game loop
while True:
    sc.update()

    #moveing the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor()>240:
        ball.sety(240)
        ball.dy*=-1
        
        

    if ball.ycor()<-240:
        ball.sety(-240)
        ball.dy*=-1

    if ball.xcor()>490:
        ball.goto(0,0)
        ball.dx*=-1
        sc_1 +=1
        pen.clear()
        pen.write("Player 1 = {}  Player 2 = {}".format(sc_1 , sc_2), align="center", font=("Courier" ,20 ,"normal"))
        


    if ball.xcor()<-490:
        ball.goto(0,0)
        ball.dx*=-1
        sc_2 +=1
        pen.clear()
        pen.write("Player 1 = {}  Player 2 = {}".format(sc_1 , sc_2), align="center", font=("Courier" ,20 ,"normal"))
    
    if sc_1>=5:
        ball.setx(0)
        ball.sety(0)
        pen.goto(0,110)
        pen.color("green")
        ball.dx=0
        ball.dy=-0
        pen.write("WINNER - 🎉Player 1🎉", align="center", font=("Courier" ,35 ,"bold italic",))
    
    if sc_2>=5:
        ball.setx(0)
        ball.sety(0)
        pen.goto(0,110)
        pen.color("green")
        ball.dx=0
        ball.dy=-0
        pen.write("WINNER - 🎉Player 2🎉", align="center", font=("Courier" ,35 ,"bold italic",))

    # collision
    if ball.xcor()> 450 and (ball.ycor() < bat_2.ycor() + 40 and ball.ycor() > bat_2.ycor() - 50):
        ball.dx*= -1

    if ball.xcor()<-450 and (ball.ycor() < bat_1.ycor() + 40 and ball.ycor() > bat_1.ycor() - 50):
        ball.dx*= -1
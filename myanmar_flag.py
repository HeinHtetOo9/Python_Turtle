import turtle
from functools import partial

yrectangle = "#FECB00"
grectangle ="#34B233"
rrectangle="#EA2839"
wstar="white"
 
t=turtle.Turtle()      #calling turtle
t.screen.bgcolor("#C0C0C0")
t.shape("turtle")

def my_goto(x,y):     # for pen movement
    t.penup()
    t.goto(x,y)
    t.pendown()

def rectangle(x,y,color):
    my_goto(x,y)
    t.fillcolor(color)
    t.begin_fill()
    t.pencolor(color)     #for 3 rectangles yellow,green,red
    t.forward(500)        
    t.right(90)
    t.forward(100)        
    t.right(90)
    t.forward(500)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.end_fill()

def white_star():         #for white star
    my_goto(60,80)
    t.pencolor(wstar)
    t.fillcolor(wstar)
    t.begin_fill()
    for i in range(5):  
        t.left(216)
        t.forward(220)
    t.end_fill()
    t.hideturtle()

rectangle_3=partial(rectangle,-300) #3 RECTANGLES WITH PARTIAL
rectangle_3(200,yrectangle)
rectangle_3(100,grectangle)
rectangle_3(0,rrectangle)
white_star()

if __name__ == "__main__":
    t.pensize(3)
    my_goto(40,-200)
    t.pencolor("black")
    t.write('by heinhtetoo', font=("Bradley Hand ITC", 20, "bold"))
turtle.done()
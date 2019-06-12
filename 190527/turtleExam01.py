import turtle
from random import randint

# (x,y) 위치에 반지름 radius로 원을 그리는 함수
def draw_circle(turtle,color,x,y,radius):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

#(x,y) 위치에 width와 height 크기의 사각형을 그리는 함수
def draw_rectangle(turtle,color,x,y,width,height):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range (2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
        turtle.end_fill()

# (x,y) 위치에 width와 height 크기의 마름모꼴을 그리는 함수
def draw_trepezoid(turtle,color,x,y,width,height):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(width)
    turtle.right(60)
    turtle.forward(height)
    turtle.right(120)
    turtle.forward(width+20)
    turtle.right(120)
    turtle.forward(height)
    turtle.right(60)
    turtle.end_fill()

# (x,y) 위치에 별 모양을 그리는 함수
def draw_star(turtle,color,x,y,size):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(10):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

t=turtle.Turtle()
t.shape("turtle")
t.speed(0)
x=0
y=0
width=240

#트리의 줄기를 그린다
draw_rectangle(t,"brown",x-20,y-50,30,50)

#트리의 잎을 그린다.
height=20
for i in range(10):
    width=width-20
    x=0-width/2
    draw_trepezoid(t,"green",x,y,width,height)
    draw_circle(t,"red",x+randint(0,width),y+randint(0,height),10)
    y=y+height

draw_star(t,"yellow",4,y,100)
t.penup()
t.color("red")
t.goto(-200,250)
t.write("Merry Christmas",font=("Arial",24,"italic"))
t.goto(-200,220)
t.write("Happy New Year!",font=("Arial",24,"italic"))


turtle.exitonclick()
import turtle
import random

t1= turtle.Turtle() # 첫 번째 거북이
t2= turtle.Turtle() # 두 번째 거북이

t1.color("pink")
t1.shape("turtle")
t1.shapesize(5)
t1.pensize(5)

t2.color("blue")
t2.shape("turtle")
t2.shapesize(5)
t2.pensize(5)

t1.penup()
t1.goto(-300,0)

t2.penup()
t2.goto(-300,-100)

for i in range(100):
    d1=random.randint(1,60)
    t1.forward(d1)
    d2=random.randint(1,60)
    t2.forward(d2)


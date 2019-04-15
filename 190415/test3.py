import turtle #터틀 그래픽 모듈을 불러옴
import random #난수 모듈을 불러옴

screen =turtle.Screen()
image1= "mano1.gif"
image2= "mano2.gif"

screen.addshape(image1)
screen.addshape(image2)
t1=turtle.Turtle() # 첫 번째 거북이를 생성
coin=random.randint(0,1)

if coin==0 :
    t1.shape(image1)
    t1.stamp()

else:
    t1.shape(image2)
    t1.stamp()


turtle.exitonclick()
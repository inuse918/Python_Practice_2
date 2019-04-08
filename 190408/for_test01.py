import turtle
t=turtle.Turtle()
t.shape("turtle")

#리스트를 사용하여 색상을 문자열로 저장한다.
color_list=["yellow","red","blue","green"]

for i in range(4):
    t.fillcolor(color_list[i]) # 채우기 색상을 설정한다.
    t.begin_fill() # 채우기를 시작한다.
    t.circle(100) # 속이 채워진 원이 그려진다.
    t.end_fill() # 채우기를 종료한다.
    t.forward(50)

turtle.exitonclick()

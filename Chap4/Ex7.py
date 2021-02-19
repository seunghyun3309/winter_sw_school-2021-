import turtle
import os

t = turtle.Pen()
t.shape("turtle")

color_list = []
color_list.append(input("색상 #1을 입력하시오: "))
color_list.append(input("색상 #2을 입력하시오: "))
color_list.append(input("색상 #3을 입력하시오: "))

t.fillcolor(color_list[0])
t.begin_fill()
t.circle(50)
t.end_fill()
t.forward(100)

t.fillcolor(color_list[1])
t.begin_fill()
t.circle(50)
t.end_fill()
t.forward(100)

t.fillcolor(color_list[2])
t.begin_fill()
t.circle(50)
t.end_fill()

os.system("Pause")

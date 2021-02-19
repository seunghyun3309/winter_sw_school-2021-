import turtle
import os

t = turtle.Pen()
t.shape("turtle")

radius = 50
t.circle(radius)
radius += 20
t.up()
t.goto(100, 0)
t.down()
t.circle(radius)
radius += 20
t.up()
t.goto(200, 0)
t.down()
t.circle(radius)

os.system("Pause")

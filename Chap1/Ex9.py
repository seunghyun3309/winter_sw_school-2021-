import os
import turtle
import time

t = turtle.Pen()
t.shape("turtle")

t.up()
t.goto(-80, 130)
t.down()
t.circle(100)

t.up()
t.goto(100, 130)
t.down()
t.circle(100)

t.up()
t.goto(280, 130)
t.down()
t.circle(100)

t.up()
t.goto(0, 0)
t.down()
t.circle(100)

t.up()
t.goto(200, 0)
t.down()
t.circle(100)

os.system("Pause")

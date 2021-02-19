import turtle
import os
import time

t = turtle.Pen()
t.shape("turtle")

side = 100
angle = 90

t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)

t.up()
t.goto(side, 0)
t.down()

time.sleep(1)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)

t.up()
t.goto(0, side)
t.down()

time.sleep(1)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)

t.up()
t.goto(side, side)
t.down()

time.sleep(1)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)

os.system("Pause")

import os
import turtle
import time

t = turtle.Pen()
t.shape("turtle")

t.forward(100)

t.up()
t.goto(0, 100)
time.sleep(1)
t.down()
t.forward(100)

os.system("Pause")

import turtle
import os

t = turtle.Pen()
t.shape("turtle")
t.left(90)
for i in range(6):
    t.forward(100)
    t.right(60)
    for j in range(3):
        t.forward(20)
        t.backward(20)
        t.left(60)
    t.right(120)
    t.backward(100)
    t.left(60)

os.system("Pause")

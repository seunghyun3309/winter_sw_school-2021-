import random
import turtle

t = turtle.Pen()
t.shape("turtle")

def square():
    t.fd(100)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(100)

color = ['yellow','red','purple','blue']
for c in color:
    x = random.randrange(201)-101
    y = random.randrange(201)-101

    t.up()
    t.goto(x,y)
    t.down()
    t.fillcolor(c)
    t.begin_fill()
    square()
    t.end_fill()



import random
import turtle

t = turtle.Pen()
t.shape("turtle")

def shape(n):
    if n<=2:
        t.circle(100)
    for i in range(k):
        t.forward(100)
        t.right(360 / n)


color = ['white','yellow','blue','skyblue','orange','green']
for c in color:
    x = random.randrange(401)-201
    y = random.randrange(401)-201

    t.up()
    t.goto(x,y)
    t.down()
    t.fillcolor(c)
    t.begin_fill()
    k = random.randrange(7)+2 # 삼각형부터 8각형까지 일단
    shape(k)
    t.end_fill()



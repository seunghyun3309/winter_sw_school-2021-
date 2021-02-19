import turtle
import math
import os

t = turtle.Pen()
t.shape("turtle")
t.speed(0)

x1 = int(input("x1: "))
y1 = int(input("y1: "))
r1 = int(input("r1: "))
t.up()
t.goto(x1, y1)
t.down()
t.circle(r1)

x2 = int(input("x2: "))
y2 = int(input("y2: "))
r2 = int(input("r2: "))
t.up()
t.goto(x2, y2)
t.down()
t.circle(r2)

d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
if d >= r1 + r2:
    t.write("첫번째 원과 두번째 원이 겹치지 않습니다.")
elif d < (r1 + r2) and abs(r1 - r2) < d:
    t.write("첫번째 원과 두번째 원이 겹칩니다.")
elif d <= abs(r1 - r2):
    if max(r1, r2) == r1 and r1 != r2:
        t.write("두번째 원이 첫번째 원의 내부에 있습니다.")
    elif max(r1, r2) == r2 and r1 != r2:
        t.write("첫번째 원이 두번째 원의 내부에 있습니다.")
    else:
        t.write("첫번째 원과 두번째 원이 일치합니다.")

print(d, r1 + r2, abs(r1 - r2))
os.system("Pause")

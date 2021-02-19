import random

x1 = random.randrange(100) + 1  # 1부터 100까지의 난수
x2 = random.randrange(100) + 1  # 1부터 100까지의 난수
ans = int(input(str(x1) + "-" + str(x2) + "="))

if ans == x1 - x2:
    print("맞았습니다.")
else:
    print("틀렸습니다.")

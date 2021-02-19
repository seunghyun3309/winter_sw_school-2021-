import random

dice = []

for i in range(2):
    dice.append(random.randint(1, 6))

print("첫번째 주사위=" + str(dice[0]) + " " + "두번째 주사위=" + str(dice[1]))

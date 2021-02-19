import random


def set_dice(x, count):
    for i in range(count):
        rand = random.randint(1, 6)
        x[rand % 6] += 1


def get_result(x):
    for index, i in enumerate(x[1:]):
        print("주사위가", (index + 1), "인 경우는", i)
    print("주사위가", len(x), "인 경우는", x[0])


def set_dict(x, count):
    for i in range(count):
        rand = random.randint(1, 6)
        x[rand] += 1


def get_result2(x):
    for i in x.keys():
        print("주사위가", i, "인 경우는", x[i])



numbers = [0, 0, 0, 0, 0, 0]
set_dice(numbers, 1000)
get_result(numbers)

num_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
set_dict(num_dict, 1000)
get_result2(num_dict)

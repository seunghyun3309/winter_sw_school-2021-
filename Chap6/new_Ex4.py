for i in range(1, 10):
    if i % 2 == 0:
        for j in range(1, 10):
            if j > i:
                break
            print(i, "*", j, "=", i * j)
    else:
        continue

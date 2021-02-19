number = int(input("임의의 정수(1~9) 입력 : "))

for i in range(1, number + 1):
    for j in range(1, number + 1):
        if j < i + 1:
            print(j, end='')
        else:
            print('*', end='')
    print('')

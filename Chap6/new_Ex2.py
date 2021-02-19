number = input("임의의 정수 입력 : ")
print("역순 출력 :")
for i in number[len(number) - 1::-1]: # 역순 출력
    print(i, end=' ')

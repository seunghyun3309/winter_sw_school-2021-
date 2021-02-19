number = input("임의의 정수 입력 : ")
flag = 0
if number[0] in ['+', '-']:
    flag = 1
print(number, str(len(number) - flag)+"자리 정수")
sum = 0
for i in number[flag:]:
    sum += int(i)
print("각 자리의 총합 :", sum)

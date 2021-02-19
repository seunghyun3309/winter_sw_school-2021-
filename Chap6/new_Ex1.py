numbers = []
index = 'a'
print("4개의 정수를 입력하시오.")

numbers.append(int(input("a: ")))
numbers.append(int(input("b: ")))
numbers.append(int(input("c: ")))
numbers.append(int(input("d: ")))

# (참고) 아스키 코드를 활용해 for문 사용
# for i in range(4):
#     numbers.append(int(input(chr(ord(index)+i)+":")))

max_num = numbers[0]

for i in numbers:
    if i > max_num:
        max_num = i
    else:
        continue
print("최댓값 : ", max_num)

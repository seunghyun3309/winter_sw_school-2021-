result = 0

while True:
    number = int(input("정수를 입력하시오(종료:0) : "))
    if number == 0:
        break
    else:
        result += number

print("합은 ", result, "입니다.")

import random

num = int(input("복권번호를 입력하시요(0에서 99사이):"))
ans = random.randrange(100)
ans = 44
print("당첨번호는 " + str(ans) + "입니다.")

if ans == num:
    print("상금은 100만원입니다.")
elif (str(ans)[0] == str(num)[0]) or (str(ans)[1] == str(num)[1]):
    print("상금은 50만원 입니다.")
else:
    print("상금은 없습니다.")

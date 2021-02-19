def set_list(x):
    print("임의의 정수 5개를 입력하시오...")
    for i in range(5):
        x.append(int(input("정수를 입력하시오: ")))


def get_static(x):
    total = 0
    for i in x:
        total += i
    return total, total / len(x)


numbers = []
set_list(numbers)
tot, avg = get_static(numbers) # 합/평균을 리턴
print("총점 :", tot, "평균 : ", '%.6f' % (avg))

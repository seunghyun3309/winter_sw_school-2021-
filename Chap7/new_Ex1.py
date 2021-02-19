def get_sum(a, b, c):
    return a + b + c


def get_avg(a, b, c):
    return (a + b + c) / 3


def get_grade(a, b, c):
    avg = get_avg(a, b, c)
    grade = 'F'
    if avg >= 90:
        grade = 'A'
    elif avg >= 80:
        grade = 'B'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 60:
        grade = 'D'
    return grade


print("세 과목의 점수를 입력하세요 :")
kor = int(input("국어 : "))
eng = int(input("영어 : "))
mat = int(input("수학 : "))

print("총점 :", get_sum(kor, eng, mat), "평균 :", get_avg(kor, eng, mat), "학점 : ", get_grade(kor, eng, mat))

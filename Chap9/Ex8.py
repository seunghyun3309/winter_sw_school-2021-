def set_Quiz(x):
    hint = ['최근에 가장 떠오르는 프로그래밍 언어', '데이터를 저장하는 메모리 공간',
            '작업을 수행하는 문장들의 집합에 이름을 붙인것', '여러 개의 자료들을 모아서 하나의 묶음으로 저장하는 것']
    answer = ['파이썬', '변수', '함수', '리스트']
    for index, i in enumerate(hint):
        x[i] = answer[index]


def print_Quiz(x):
    for i in x.keys():
        print("다음은 어떤 단어에 대한 설명일까요?")
        print()
        print(i)
        for index, j in enumerate(x.values()):
            print((index + 1), j, end=' ')

        while True:
            answer = input("\n\n\t입력 : ")
            if check_answer(x, i, answer):
                print("\n\t정답입니다!!!\n")
                break
            else:
                print("\n\t정답이 아닙니다. ㅠ..ㅠ\n")
                for index, j in enumerate(x.values()):
                    print((index + 1), j, end=' ')


def check_answer(x, quiz, answer):
    if x[quiz] == answer:
        return True
    return False


quiz = {}
set_Quiz(quiz)
print_Quiz(quiz)

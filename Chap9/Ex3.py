def set_book(x):
    while True:
        name = input("[입력모드] 이름 : ")
        if name == '':
            break
        number = input("\t   전화번호 : ")
        x[name] = number
    get_book(x)


def get_book(x):
    while True:
        name = input("<검색모드> 이름 :")
        if name == '':
            break
        elif name in x.keys():
            print(name,"의 전화번호는", x[name], "입니다.")
        else:
            print("검색 결과가 없습니다.")


phone_book = {}
set_book(phone_book)
get_book(phone_book)

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

print("사칙연산 : 임의의 두 정수를 입력하시오...")
x = (int(input("첫 번째 정수(x) : ")))
y = (int(input("두 번째 정수(y) : ")))

print(x, "+", y, "=", add(x, y))
print(x, "-", y, "=", sub(x, y))
print(x, "*", y, "=", mul(x, y))
print(x, "/", y, "=", div(x, y))

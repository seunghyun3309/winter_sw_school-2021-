sum = 0 

for i in range(1,101):
    if i%2==0:
        sum+=i
        print(i,end=' ')
    else :
        continue
print()
print("1~100 사이의 짝수의 총합: ", sum)
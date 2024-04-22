res = int(input())
num = 0

while res != 1:
    if res%3 == 0:
        res = res/3
    elif res%2 == 0:
        res = res/2
    else:
        res -= 1
    num += 1
    
print(num)

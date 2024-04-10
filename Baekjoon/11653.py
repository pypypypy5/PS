num = int(input())
cur = num

while cur != 1:
    for i in range(2,int(cur)+1):
        if cur%i == 0:
            print(i)
            cur = cur/i
            break
        else:
            pass
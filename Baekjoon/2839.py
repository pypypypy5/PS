N = int(input())

n3 = 0
n5 = 0
while True:
    if N < 0:
        print(-1)
        break
    if N % 5 == 0:
        n5 = N/5
        print(int(n3 + n5))
        break
    else:
        N -= 3
        n3 += 1
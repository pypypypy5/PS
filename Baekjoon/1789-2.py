s = int(input())

for i in range(1,s):
    if s >= i*(i+1)/2:
        pass
    else:
        print(i-1)
        break
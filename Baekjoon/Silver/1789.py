s = int(input())

for i in range(1,s+4):
    s = s - i
    if s >= 0:
        pass
    else:
        print(i-1)
        break

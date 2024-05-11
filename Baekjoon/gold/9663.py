import sys
input = sys.stdin.readline

N = int(input())

count = 0

def nextcase(row, nowins):
    global count
    if row == N:
        count += 1
        return
    for i in range(0,N):
        gotcha = True
        for j in range(len(nowins)):
            nowins_j = nowins[j]
            dif = row - j
            if i in nowins:
                gotcha = False
                break
            elif nowins_j+dif == i or nowins_j-dif == i:
                gotcha == False
                break
        if gotcha:
            nowins.append(i)
            nextcase(row + 1, nowins.copy())
            nowins.pop()
        
nextcase(0, [])
print(count)

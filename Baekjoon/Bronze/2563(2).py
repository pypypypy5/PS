background = [[0]*101 for i in range(101)]

num = int(input())

for num_count in range(0,num):
    x,y = list(map(int,input().split(' ')))
    for i in range(0,10):
        for j in range(0,10):
            background[y+i][x+j] = 1

result = 0

for i in range(0,101):
    result += background[i].count(1)

print(result)

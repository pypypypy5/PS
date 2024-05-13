import sys
input = sys.stdin.readline

height = int(input())
prev = [int(input())]
for i in range(1,height):
    cur_flr = list(map(int, input().split(' ')))
    next = [[] for next_para in range(i+1)]
    for j in range(i+1):
        if j == 0:
            next[j] = (prev[0]+cur_flr[0])
        elif j == i:
            next[j] = (prev[j-1]+cur_flr[-1])
        else:
            next[j] = (max(prev[j-1]+cur_flr[j], prev[j]+cur_flr[j]))

    prev = next

print(max(prev))

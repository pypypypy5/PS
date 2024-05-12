import sys
input = sys.stdin.readline

num_tc = int(input())
for i in range(num_tc):
    N, start, end = map(int, input().split(' '))
    if start == 1 and end == N:
        print(0)
    elif start == N and end == 1:
        print(0)
    elif start == 1:
        print(1)
    elif start == N:
        print(1)
    elif abs(start-end) == 1:
        print(1)
    else:
        print(2)

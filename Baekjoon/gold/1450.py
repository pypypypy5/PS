import sys
input = sys.stdin.readline

N, C = map(int, input().split(' '))
things = list(map(int, input().split(' '))).sort()

start = 0
end = 0
count = 1

for i in range(N):
    for j in range(i,N):
        if things[i] + things[j] <= C:
            count += 1
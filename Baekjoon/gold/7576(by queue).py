import sys
from collections import deque
input = sys.stdin.readline

M,N = map(int, input().split(' '))   #row/column
grid = []
queue = deque()
for i in range(N):
    row = list(map(int, input().split()))
    grid.append(row)
    for j in range(M):
        if row[j] == 1:
            queue.append((i, j))  #row,column

vector = [(-1,0),(1,0),(0,1),(0,-1)]   #up,down,right,left

day = -1
while queue:
    day += 1
    for ripen in range(len(queue)):
        r,c = queue.popleft()
        for dr,dc in vector:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0:
                grid[nr][nc] = 1
                queue.append((nr,nc))

for i in grid:
    for j in i:
        if j == 0:
            print(-1)
            exit()
print(day)

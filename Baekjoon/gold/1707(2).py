import sys
sys.setrecursionlimit(100000)
from collections import deque
input = sys.stdin.readline
tk_n = int(input())

def mainf():
    num_n,num_e = map(int, input().split(' '))
    grid = [[i,set()] for i in range(num_n)]

    for i in range(num_e):
        n1,n2 = map(int, input().split())
        n1 -= 1
        n2 -= 1
        grid[n1][1].add(n2)
        grid[n2][1].add(n1)
    
    def subf(start):
        main = deque()
        now = deque()
        main.append(start)
        grid[start].append(0)

        while main:
            for i in range(len(main)):
                cur_n = main.popleft()
                now = grid[cur_n][1]
                cur_c = grid[cur_n][2]
                nxt_c = 1-cur_c
                for j in now:
                    if len(grid[j]) == 2:
                        grid[j].append(nxt_c)
                        main.append(j)
                    else:
                        if grid[j][2] == cur_c:
                            print('NO')
                            return True
                now = deque()

        for i in range(len(grid)):
            if len(grid[i]) == 2:
                isnbi = subf(i)
                if isnbi:
                    return True
    if subf(n1):
        return
    print('YES')

for i in range(tk_n):
    mainf()

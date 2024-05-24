import sys
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
        now = set()
        main.append(start)

        while main:
            for i in range(len(main)):
                cur_n = main.popleft()
                if grid[cur_n][0] != None:
                    now = grid[cur_n][1]
                for j in now:
                    if grid[j][0] != None:
                        if grid[j][1] & now:
                            print('NO')
                            return True
                        main.append(j)
                grid[cur_n][0] = None
                now = set()

        for i in range(len(grid)):
            if grid[i][0] != None:
                isnbi = subf(i)
                if isnbi:
                    return True
    if subf(n1):
        return
    print('YES')

for i in range(tk_n):
    mainf()

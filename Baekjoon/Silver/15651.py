import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

li = []
def backt():
    if len(li) == M:
        print(" ".join(map(str, li)))
        return
    for i in range(1,N+1):
        li.append(i)
        backt()
        li.pop()

backt()

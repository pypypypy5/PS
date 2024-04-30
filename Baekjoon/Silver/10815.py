#super coward solution
import sys
input = sys.stdin.readline

N = int(input())
I_have = set(map(int, input().split(' ')))
M = int(input())
to_tnk = list(map(int, input().split(' ')))

for i in range(len(to_tnk)):
    num = to_tnk[i]
    if num in I_have:
        to_tnk[i] = 1
    else:
        to_tnk[i] = 0

print(' '.join(map(str, to_tnk)))

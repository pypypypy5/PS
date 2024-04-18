import sys
input = sys.stdin.readline

strs = [[] for _ in range(50)]

num_str = int(input())
for i in range(num_str):
    now_st = input().rstrip()
    l = len(now_st)-1
    if now_st not in strs[l]:
        strs[l].append(now_st)

for i in strs:
    i.sort()
    for j in i:
        print(j)

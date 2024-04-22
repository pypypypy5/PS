#import sys
#input = sys.stdin.readline

li = [0 for i in range(10001)]

numofn = int(input())
for n_count in range(numofn):
    now = int(input())
    li[now] += 1

for i in range(len(li)):
    for j in range(li[i]):
        print(i)

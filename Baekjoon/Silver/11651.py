import sys
input = sys.stdin.readline

dots = []

num_n = int(input())
for i in range(num_n):
    x, y = map(int, input().split())
    dots.append([y,x])

dots.sort()

for dot in dots:
    print(dot[1],dot[0])


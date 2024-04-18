import sys
input = sys.stdin.readline

dots = [[] for _ in range(200)]

num_n = int(input())
for i in range(num_n):
    st = input().rstrip()
    x, y = st.split()
    x = int(x)
    dots[x-1].append(st)


for dot in dots:
    for i in dot:
        print(i)

#import sys
#input = sys.stdin.readline


n_of_dot = int(input())

dot_li = []

for i in range(n_of_dot):
    x, y = map(int, input().split())
    dot = [x,y]
    dot_li.append(dot)


groups_li = []
x_li = []

for i in dot_li:
    x = i[0]
    if x not in x_li:
        x_li.append(x) #too complex
        x_li.sort()
        groups_li.insert(x_li.index(x), [i])
    else:
        groups_li[x_li.index(x)].append(i)



for i in groups_li:
    i.sort()

for i in groups_li:
    for j in i:
        print(f'{j[0]} {j[1]}')
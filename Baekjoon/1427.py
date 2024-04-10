#import sys
#input = sys.stdin.readline

li = []
for i in input():
    li.append(int(i))

li.sort(reverse = True)

for i in li:
    print(i, end = '')
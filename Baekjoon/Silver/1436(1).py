import re

N = int(input())
n = 0
num = 666

while True:
    stnum = str(num)
    p = re.compile(r'666')
    m = p.search(stnum)
    if m != None:
        n += 1
    if  n == N:
        print(num)
        break
    num += 1

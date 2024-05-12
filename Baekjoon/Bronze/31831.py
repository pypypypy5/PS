import sys
input = sys.stdin.readline
N, M = map(int, input().split(' '))

stss = 0
days = list(map(int, input().split(' ')))
count = 0
for i in days:
  if stss > abs(i):
    stss += i
  else:
    if i<0:
      stss =0
    else:
      stss+=i
  if stss >= M:
    count += 1
    
print(count)
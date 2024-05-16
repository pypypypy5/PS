#에라토스테네스의 체 응용
import math

k = int(input())

max = 2*k
if max < 1000000000:
    last = max
else:
    last = 1000000000
lst = range(1,last+1)

mdiv = math.floor(math.sqrt(max))
for i in range(1,mdiv):
    if i%2 == 0 or i%3 == 0:
        continue
    else:
        num = last//i
        for j in range(1,num):
            n = i*j
            lst.remove(n)

print(lst[k-1])
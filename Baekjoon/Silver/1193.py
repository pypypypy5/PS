x = int(input())

line_n = 0
x_replica = x

while True:
    x_replica -= line_n
    line_n += 1
    if x_replica <= line_n:
        break

sum = line_n + 1
past_sum = (line_n-1)*line_n//2
now = x-past_sum

if line_n % 2 == 0:
    print(now, end = '')
    print('/', end = '')
    print(sum-now)
else:
    print(sum-now, end = '')
    print('/', end = '')
    print(now)

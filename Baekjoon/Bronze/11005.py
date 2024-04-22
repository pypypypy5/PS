N, B = map(int, input().split())

biggest = 0
for i in range(99999999999999):
    if N < B ** (i+1):
        biggest = i
        break

result = []
now = 0
for i in range(biggest+1):
    step = B**(biggest-i)
    for j in range(B+1):
        if N >= step:
            N -= step
            now += 1

    result.append(now)
    now = 0

for i in result:
    if i <= 9:
        print(i, end = '')
    else:
        changed = chr(i+55)
        print(changed, end = '')

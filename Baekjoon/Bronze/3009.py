x = []
y = []

for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

if x.count(a) == 2:
    x.remove(a)
    x.remove(a)
    print(x[0], end = ' ')
else:
    print(a, end =' ')


if y.count(b) == 2:
    y.remove(b)
    y.remove(b)
    print(y[0], end = ' ')
else:
    print(b)

coun = int(input())

x = []
y = []

for i in range(coun):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

if len(x) > 1 and len(y) > 1:
    print((max(x)-min(x))*(max(y)-min(y)))
else:
    print(0)

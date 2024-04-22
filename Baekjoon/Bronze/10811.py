length, howm = map(int, input().split())

basket = [i+1 for i in range(0,length)]

for n_count in range(howm):
    n1, n2 = map(int, input().split())
    a = basket[n1-1:n2]
    a.reverse()
    basket[n1-1:n2] = a

output = ' '.join(map(str, basket))
print(output)

f_list = []
n_list = []

for i in range(0,10):
    f_list.append(int(input()))

for i in f_list:
    a = i % 42
    if a not in n_list:
        n_list.append(a)

print(len(n_list))

num = int(input())
fi = map(int, input().split())
i_list = list(fi)

maximum = max(i_list)
n_list = []

for i in i_list:
    n_list.append((i/maximum)*100)

print(sum(n_list)/num)

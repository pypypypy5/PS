inp_str = list(input())

dic ={}
for i in inp_str:
    if i.upper() in dic:
        dic[i.upper()] += 1
    else:
        dic[i.upper()] = 1

max_num = 0

for i in dic:
    if dic[i] > max_num:
        max_chr = i
        max_num = dic[i]
    elif dic[i] == max_num:
        max_chr = 'draw'

if max_chr == 'draw':
    print('?')
else:
    print(max_chr)
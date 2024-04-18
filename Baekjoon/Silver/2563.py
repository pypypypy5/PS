print('끝내려면 두번 엔터\n')

fir = []
foramoment = []
while True:
    foramoment = input()
    if not foramoment:
        break
    fir.append(foramoment)
    foramoment = [] 

def spl(inp):
    result = inp.split(' ')
    result_re = []
    result_re.append(float(result[0]))
    result_re.append(float(result[1]))
    return result_re

def overlap(lst1,lst2):
    dif1 = abs(lst1[0] - lst2[0])
    dif2 = abs(lst1[1] - lst2[1])
    if dif1 <= 10 and dif2 <= 10:
        return (10-dif1) * (10-dif2)
    else:
        return 0

howm = int(fir[0])
fin = []

for i in range(1, int(howm)+1):
    foram = spl(fir[i])
    fin.append(foram)

final = 100 * howm

for i in range(0,howm):
    for j in range(i+1, howm):
        final -= overlap(fin[i], fin[j])

print(final)

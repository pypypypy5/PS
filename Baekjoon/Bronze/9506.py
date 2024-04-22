inp = []

while True:
    got = int(input())
    if got == -1:
        break
    else:
        inp.append(got)

for n in inp:
    factor = [1]
    for i in range(2,n):

        if n % i == 0:               #factor 리스트에 약수들 넣기
            now = i
            pair = int(n/i)
            if pair > now:
                factor.append(i)
                factor.append(pair)
            elif pair == now:
                factor.append(now)
                break
            else:
                break
        
    total = sum(factor)
        
    if n != total:                     #구분, 출력
        print(f'{n} is NOT perfect.')
    else:
        factor.sort()
        print(n, end = '')
        print(' = ', end = '')
        print(factor[0], end = '')
        for i in range(1,len(factor)):
            if i != len(factor) - 1:
                print(' +',factor[i], end = '')
            else:
                print(' +',factor[i])

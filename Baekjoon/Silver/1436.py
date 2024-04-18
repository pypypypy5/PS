N = int(input())

k = 2
while True:                   #k는 결과의 자릿수. 여기서부터 k 결정하는 코드
    k += 1
    if k == 3:
        sum = 1
    else:
        sum = 1+19/9(10**(k-3) - 1)
    if N <= sum:
        break

k_n = N - (1+19/9(10**(k-4) - 1))    #자릿수 k인 것중에서 결과의 순위


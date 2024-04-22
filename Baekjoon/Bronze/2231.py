N = int(input())
length = len(str(N))
possi = []

for i in range(0,9*length):  #i는 가능한 자릿수 합의 집합
    if i < N:
        origin = N - i
        sum_comp = 0
        for j in str(origin):  #이번 origin이 생성자가 될 수 있는지 확인
            sum_comp += int(j)
        if sum_comp == i:
            possi.append(origin)

possi.sort()
if not possi:
    print(0)
else:
    print(possi[0])

k = int(input('input'))
i = 0          #몇번째 제곱ㄴㄴ수인지 저장
n = 0          #지금 다루고 있는 수
div = 2        #나누는 최고 제곱수의 원값
lst = [4]      #제곱수 저장할 리스트
sqno = False

while i < k:   #i가 k번째 전까지, k 되면 루프 종료
    n += 1
    if n >= (div+1)**2:         #최대 제곱수 갱신
        div += 1
        lst.append(div**2)
    for num in lst:
        if n%num == 0:
            sqno = False
            break
        else:
            sqno = True
    if sqno == True:
        i += 1

print(n)
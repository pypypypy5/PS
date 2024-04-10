row, column = map(int, input().split())

cur_row = []
tot = []         #input으로 받은 행렬을 이차원 리스트로 저장
for n_count in range(row):
    inp = input()
    for i in inp:
        cur_row.append(i)
    tot.append(cur_row)
    cur_row = []

changes = []
for y in range(row-7):             #여기까지 8x8 판의 맨 왼,위 좌표 정하기
    for x in range(column-7):
        dif = 0
        dif_2 = 0
        for i in range(8):         #정한 판의 칸들 순회
            for j in range(8):
                if (i+j)%2 == 0:              #dif == 판 내부의 칸들 b,w,b,w로 규칙 가지는 케이스
                    if tot[y+i][x+j] != 'B':  #dif_2 == 판 내부의 칸들 w,b,w,b로 규칙 가지는 케이스
                        dif += 1
                    else:
                        dif_2 += 1
                else:
                    if tot[y+i][x+j] != 'W':
                        dif += 1
                    else:
                        dif_2 += 1
        changes.append(dif)
        changes.append(dif_2)

changes.sort()

print(changes[0])
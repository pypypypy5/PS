import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maap = []
for i in range(m):
    up, x, y = map(int, input().split())
    maap.append([up, x, y])

fly_y = 0
chal = 0
chalover = False
real_ch_type = maap[chal][0]
real_ch_n = maap[chal][1]

def real_challenge(chal):
    global maap
    type = maap[chal][0]
    real_challenge = chal + 1  #진정 고려해야할 chal 리스트와 어디까지 고려했는지
    while True:
        if type == 0:
            if maap[real_challenge][0] == type:
                if maap[real_challenge][2] <= maap[chal][2]:
                    continue
                else:
                    return real_challenge
            else:
                if maap[real_challenge][2]-1 < maap[chal][2]+1:
                    return real_challenge
        elif type == 1:
            if maap[real_challenge][0] == type:
                if maap[real_challenge][2] >= maap[chal][2]:
                    continue
                else:
                    return real_challenge
            else:
                if maap[real_challenge][2]+1 > maap[chal][2]-1:
                    return real_challenge
        
        real_challenge += 1


for i in range(n):  # fly_x == i
    if chal < len(maap) and maap[chal][1] == i:  # 현재 위치에 끈끈이주걱이 있을 때 ---- 판정
        if maap[chal][0] == 0:  # 아래에서 올라온 끈끈이주걱
            if fly_y <= maap[chal][2]:  # 파리가 끈끈이주걱에 닿으면
                print("adios")
                sys.exit()
        elif maap[chal][0] == 1:  # 위에서 내려온 끈끈이주걱
            if fly_y >= maap[chal][2]:  # 파리가 끈끈이주걱에 닿으면
                print("adios")
                sys.exit()

        chal += 1  # 다음 끈끈이주걱으로 넘어감


    # 파리의 y축 이동 (fly_y 업데이트)
    if chal < len(maap) and maap[chal][1] > i:  # 아직 끈끈이주걱이 없을 때
        if maap[chal][0] == 0:  # 아래에서 올라온 끈끈이주걱
            if fly_y > maap[chal][2] + 1:
                fly_y -= 1
            elif fly_y < maap[chal][2] + 1:
                fly_y = maap[chal][2] + 1
            elif fly_y == maap[chal][2] + 1:
                if real_challenge:
                    move(real_challenge)
                else:
                    real_challenge = real_challenge(chal)
                    move(real_challenge)
        elif maap[chal][0] == 1:  # 위에서 내려온 끈끈이주걱
            if fly_y > maap[chal][2] - 1:
                fly_y -= 1
            elif fly_y < maap[chal][2] - 1:
                fly_y = maap[chal][2] - 1
            elif fly_y == maap[chal][2] - 1:
                if real_challenge:
                    move(real_challenge)
                else:
                    real_challenge = real_challenge(chal)
                    move(real_challenge)

# 마지막 위치 (출구)에서 확인
if fly_y == 0:
    print("stay")
else:
    print("adios")

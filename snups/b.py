import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maap = []
for i in range(m):
    up, x, y = map(int, input().split())
    maap.append([up, x, y])

# x 좌표 순으로 주걱을 정렬
maap.sort(key=lambda t: t[1])

fly_y = 0  # 파리의 현재 y 좌표
possible = True  # 파리가 끝까지 도달할 수 있는지 여부

# 모든 주걱을 확인
for i in range(m):
    up, x, y = maap[i]
    
    # 다음 이동할 x 지점까지의 거리
    if up == 0:  # 아래에서 올라온 주걱인 경우
        # 파리의 y 좌표는 주걱의 y보다 반드시 커야 함
        if fly_y <= y:
            fly_y = y + 1  # 파리를 y+1로 이동시켜 주걱을 피함
    elif up == 1:  # 위에서 내려온 주걱인 경우
        # 파리의 y 좌표는 주걱의 y보다 반드시 작아야 함
        if fly_y >= y:
            fly_y = y - 1  # 파리를 y-1로 이동시켜 주걱을 피함
    
    # 파리가 출구에 도달할 수 없는 상황이 발생하는지 체크
    if fly_y < 0 or fly_y > n:
        possible = False
        break

# 마지막에 출구에 도달했는지 확인
if possible and fly_y == 0:
    print("stay")
else:
    print("adios")

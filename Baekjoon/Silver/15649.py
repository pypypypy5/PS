import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))

li = []
def backt():
    if len(li) == M:
        print(" ".join(map(str, li)))
        return
    for i in range(1,N+1):
        if i not in li:      #for문 내에서 리스트에 하나가 더해질때마다 backt() 걸림 -> 중첩된 함수들중 밑의것 다 소진(얘의 자식 경우 다 끝남) -> 얘 pop()
            li.append(i)       #지금 backt 내의 for 다시 작동, 다음 경우 돌아감
            backt()
            li.pop()

backt()

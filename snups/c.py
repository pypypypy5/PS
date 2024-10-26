import sys
input = sys.stdin.readline

def find_loser(N, T, A):
    visited = [-1] * (N + 1)  # 각 친구의 방문 순서를 기록하는 리스트
    path = []  # 방문한 순서대로 기록하는 리스트
    
    current = 1  # 시작 친구 번호
    step = 0  # 현재 단계
    
    # 순환이 생길 때까지 지목 과정을 수행
    while visited[current] == -1:
        visited[current] = step  # 현재 친구를 방문했다고 기록
        path.append(current)  # 경로에 추가
        current = A[current - 1]  # 다음 지목된 친구로 이동
        step += 1  # 단계 증가
    
    # 순환 시작 지점과 순환 길이
    cycle_start = visited[current]  # 순환이 시작되는 지점
    cycle_length = step - cycle_start  # 순환의 길이
    
    if T < cycle_start:
        # 순환에 들어가지 않고 T번째로 도달하는 친구
        result = path[T]
    else:
        # 순환이 있는 경우, T번째로 도달하는 친구는 순환 내부에서 결정
        result = path[cycle_start + (T - cycle_start) % cycle_length]
    
    return result

# 입력 처리
N, T = map(int, input().split())
A = list(map(int, input().split()))

# 결과 출력
print(find_loser(N, T, A))

import sys
input = sys.stdin.readline

def determine_winner(alice_top_cards, bob_top_cards, N, M):
    alice_turn = True  # Alice가 먼저 시작
    for c in range(M):
        if alice_turn:
            # Alice의 카드가 A면 계속 Alice가 플레이
            if alice_top_cards[c] == 'A':
                continue
            else:
                alice_turn = False
        else:
            # Bob의 카드가 B면 계속 Bob이 플레이
            if bob_top_cards[c] == 'B':
                continue
            else:
                alice_turn = True
    return "Alice" if alice_turn else "Bob"

# 입력 처리
N, M = map(int, input().split())

# Alice와 Bob의 카드 배치를 리스트로 변환
alice_cards = [list(input().strip()) for _ in range(N)]
bob_cards = [list(input().strip()) for _ in range(N)]

# 교환 횟수
Q = int(input())

# 교환 명령어 입력
swap_operations = [list(map(int, input().split())) for _ in range(Q)]

# 각 열의 최상단 카드 상태를 기록 (Alice, Bob)
alice_top_cards = [alice_cards[0][i] for i in range(M)]
bob_top_cards = [bob_cards[0][i] for i in range(M)]

# 초기 상태에서의 승리자 출력
print(determine_winner(alice_top_cards, bob_top_cards, N, M))

# 카드 교환 처리 및 승리자 출력
for r1, c1, r2, c2 in swap_operations:
    # 1-based 인덱스에서 0-based 인덱스로 변환
    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
    
    # Alice의 (r1, c1) 카드와 Bob의 (r2, c2) 카드 교환
    alice_cards[r1][c1], bob_cards[r2][c2] = bob_cards[r2][c2], alice_cards[r1][c1]
    
    # 최상단 카드가 있는 1행에 교환이 발생했을 때, 최상단 카드 갱신
    if r1 == 0:
        alice_top_cards[c1] = alice_cards[0][c1]
    if r2 == 0:
        bob_top_cards[c2] = bob_cards[0][c2]

    # 현재 교환 후의 승리자 출력
    print(determine_winner(alice_top_cards, bob_top_cards, N, M))

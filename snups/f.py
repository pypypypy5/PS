import sys
from collections import defaultdict, deque

input = sys.stdin.read
sys.setrecursionlimit(200000)

def dfs(tree, fruits, water, node, parent):
    # 현재 노드에 물을 더해준다
    fruits[node] += water
    
    # 자식 노드로 물을 분배
    children = len(tree[node]) - (1 if parent is not None else 0)
    if children > 0:
        # 자식 노드가 있다면 남은 물을 자식에게 나눠준다
        flow = water // children
        for child in tree[node]:
            if child != parent:
                dfs(tree, fruits, flow, child, node)

# 입력 처리
data = input().splitlines()
N, Q = map(int, data[0].split())

# 트리 구조 생성
tree = defaultdict(list)
for i in range(1, N):
    u, v = map(int, data[i].split())
    tree[u].append(v)
    tree[v].append(u)

# 열매 크기 초기화
fruits = list(map(int, data[N].split()))
fruits = [0] + fruits  # 1-based 인덱스를 사용하기 위해 0번째는 0으로 패딩

# 쿼리 처리
queries = data[N+1:]
result = []
for query in queries:
    query = query.split()
    if query[0] == '1':  # 물 주는 쿼리
        u, x = int(query[1]), int(query[2])
        dfs(tree, fruits, x, u, None)
    elif query[0] == '2':  # 열매 크기 출력 쿼리
        u = int(query[1])
        result.append(str(fruits[u]))

# 결과 출력
sys.stdout.write("\n".join(result) + "\n")

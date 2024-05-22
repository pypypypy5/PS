import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

class graph:
    def __init__(self):
        self.isvisited = False
        self.edges = []

N,M,R = map(int, input().split(' '))
nodes = []
for i in range(N):
    node = graph()
    nodes.append(node)

for i in range(M):
    n1,n2 = map(int, input().split(' '))
    nodes[n1-1].edges.append(n2-1)
    nodes[n2-1].edges.append(n1-1)

for i in nodes:
    i.edges.sort(reverse = True)

orders = [0]*N
order = 1
def dfs(now_idx):
    global order
    now_nd = nodes[now_idx]
    now_nd.isvisited = True
    orders[now_idx] = order
    order += 1
    for edge in now_nd.edges:
        if not nodes[edge].isvisited:
            dfs(edge)
    return
    
dfs(R-1)
for i in orders:
    print(i)

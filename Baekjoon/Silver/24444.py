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
    i.edges.sort()

orders = [0]*N
order = 1
def bfs(cur_fl):
    global order
    next_fl = []
    for edge in cur_fl:
        if not nodes[edge].isvisited:
            orders[edge] = order
            order += 1
            next_fl.extend(nodes[edge].edges)
            nodes[edge].isvisited = True
    if next_fl:
        bfs(next_fl)
    else:
        return
    
bfs([R-1])
for i in orders:
    print(i)

import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

class Graph:
    def __init__(self,ripe):
        self.ripe = ripe
        self.edges = []        #[up,down,right,left]

M,N = map(int, input().split(' '))
nodes = []
rot_count = 0
cant = False
for i in range(N):
    temp_n = list(input().split())
    for j in range(len(temp_n)):
        if temp_n[j] == '0':
            temp_n[j] = Graph(False)
        elif temp_n[j] == '1':
            temp_n[j] = Graph(True)
        else:
            temp_n[j] = None
            rot_count += 1
    nodes.append(temp_n)

start = []
for i in range(N):
    for j in range(M):
        cur_n = nodes[i][j]
        if cur_n != None:
            if cur_n.ripe:
                start.append(cur_n)

            if i > 0:
                cur_n.edges.append(nodes[i-1][j])
            else:
                cur_n.edges.append(None)
            if i < N-1:
                cur_n.edges.append(nodes[i+1][j])
            else:
                cur_n.edges.append(None)
            if j > 0:
                cur_n.edges.append(nodes[i][j-1])
            else:
                cur_n.edges.append(None)
            if j < M-1:
                cur_n.edges.append(nodes[i][j+1])
            else:
                cur_n.edges.append(None)

            if not cur_n.edges and not cur_n.ripe:
                cant = True


day_count = -1
num_count = len(start)+rot_count
def bfs(cur_fl):
    global day_count, num_count
    next_fl = []
    hasedge =False
    for edge in cur_fl:
        if edge != None:
            if not edge.ripe:
                next_fl.extend(edge.edges)
                edge.ripe = True
                hasedge = True
    if hasedge:
        day_count += 1
    if next_fl:
        bfs(next_fl)
    else:
        return

if cant:  
    print(-1)
elif num_count == N*M:
    print(0)
else:
    bfs(start)
    print(day_count)

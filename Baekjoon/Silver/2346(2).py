import sys
input = sys.stdin.readline

class LkdList:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next


num = int(input())
seq = list(map(int, input().split(' ')))           #node_prev,node,node_next circular
for i in range(len(seq)):
    if i == 0:
        node_first = LkdList([i+1,seq[i]], None, None)
        node_prev = node_first
    elif i == len(seq) - 1:
        node = LkdList([i+1,seq[i]],node_prev,node_first)
        node_first.prev = node
        node_prev.next = node
    else:
        node = LkdList([i+1,seq[i]],node_prev,None)
        node_prev.next = node
        node_prev = node


output = ['1']
Got_count = 0
now_node = node_first
for i in range(len(seq)-1):
    shld_move = now_node.data[1]
    now_node.prev.next = now_node.next
    now_node.next.prev = now_node.prev
    
    if shld_move > 0:
        for j in range(shld_move):
            now_node = now_node.next
        
    else:
        for j in range(-shld_move):
            now_node = now_node.prev
    
    output.append(str(now_node.data[0]))

print(' '.join(output))

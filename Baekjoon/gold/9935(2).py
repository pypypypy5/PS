from collections import deque
import copy
import sys
input = sys.stdin.readline

seq = deque(list(input().strip()))
seq2 = deque()
bomb = deque(list(input().strip()))

bomb_len = len(bomb)
countdown = 0
while True:
    bombed = False
    seq_len = len(seq)
    for i in copy.deepcopy(seq):
        if i == bomb[countdown]:
            countdown += 1
        seq2.append(i)
        seq.popleft()
        if countdown == bomb_len:
            for j in range(bomb_len):
                seq2.pop()
            countdown = 0
            bombed = True

    countdown = 0
    if not bombed or len(seq2) == 0:
        break

    bombed = False
    seq_len = len(seq2)
    for i in copy.deepcopy(seq2):
        if i == bomb[countdown]:
            countdown += 1
        seq.append(i)
        seq2.popleft()
        if countdown == bomb_len:
            for j in range(bomb_len):
                seq.pop()
            countdown = 0
            bombed = True

    countdown = 0
    if not bombed or len(seq) == 0:
        break

if len(seq) == 0 and len(seq2) == 0:
    print('FRULA')
elif len(seq) == 0:
    print(''.join(seq2))
else:
    print(''.join(seq))

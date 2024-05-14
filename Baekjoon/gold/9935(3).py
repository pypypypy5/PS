import sys
input = sys.stdin.readline

seq = list(input().strip())
bomb = input().strip()
seq2 = []
bomb_len = len(bomb)

for i in seq:
    seq2.append(i)
    if ''.join(seq2[-bomb_len:]) == bomb:
        for j in range(bomb_len):
            seq2.pop()

if len(seq2) == 0:
    print('FRULA')
else:
    print(''.join(seq2))

import sys
input = sys.stdin.readline

seq = list(input().strip())
seq_rev = []
bomb = list(input().strip())
bomb_rev = bomb[:]
bomb_rev.reverse()

bomb_len = len(bomb)
countdown = 0
while True:
    bombed = False
    seq_len = len(seq)
    for i in range(len(seq)):
        now = seq[seq_len-i-1]
        if now == bomb_rev[countdown]:
            countdown += 1
        seq_rev.append(now)
        seq.pop()
        if countdown == bomb_len:
            for j in range(bomb_len):
                seq_rev.pop()
            countdown = 0
            bombed = True

    countdown = 0
    if not bombed or len(seq_rev) == 0:
        break

    bombed = False
    seq_len = len(seq_rev)
    for i in range(seq_len):
        now = seq_rev[seq_len-i-1]
        if now == bomb[countdown]:
            countdown += 1
        seq.append(now)
        seq_rev.pop()
        if countdown == bomb_len:
            for j in range(bomb_len):
                seq.pop()
            countdown = 0
            bombed = True

    countdown = 0
    if not bombed or len(seq) == 0:
        break

if len(seq) == 0 and len(seq_rev) == 0:
    print('FRULA')
elif len(seq) == 0:
    seq_rev.reverse()
    print(''.join(seq_rev))
else:
    seq.reverse()
    print(''.join(seq))

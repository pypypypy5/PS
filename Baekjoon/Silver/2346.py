import sys
input = sys.stdin.readline

num = int(input())
seq = list(map(int, input().split(' ')))
for i in range(len(seq)):
    seq[i] = [i+1, seq[i]]

output = []

pointer = 0
for i in range(num):
    output.append(seq[pointer][0])
    move = seq[pointer][1]
    seq[pointer][1] = None

    while move != 0:
        if move > 0:
            pointer += 1
            pointer = pointer%len(seq)
            if seq[pointer][1] != None:
                move -= 1
        elif move < 0:
            pointer -= 1
            pointer = pointer%len(seq)
            if seq[pointer][1] != None:
                move += 1

print(output.join(' '))

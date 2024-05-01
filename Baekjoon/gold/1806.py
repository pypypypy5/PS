import sys
input = sys.stdin.readline

len_seq, mini = map(int, input().split(' '))
seq = list(map(int, input().split(' ')))

p_sum = 0
end_now = False
gotcha = False
for st_len in range(1,len(seq)+1):
    p_sum = sum(seq[0:st_len])

    for start in range(len(seq)-st_len):
        if p_sum >= mini:
            end_now = True
            gotcha = True
            break
        else:
            p_sum += seq[start+st_len]-seq[start]

    if end_now:
        break

if gotcha:
    print(st_len)
else:
    print(0)
import sys
input = sys.stdin.readline

Num_comm = int(input())
stack = []

for i in range(Num_comm):
    got = input()
    if ' ' in got:
        comm, x = map(int, got.split(' '))
    else:
        comm = int(got)

    if comm == 1:
        stack.append(x)
    elif comm == 2:
        if stack:
            output = stack.pop()
            print(output)
        else:
            print(-1)
    elif comm == 3:
        print(len(stack))
    elif comm == 4:
        if stack:
            print(0)
        else:
            print(1)
    elif comm == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)

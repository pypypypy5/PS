up, down, tree = map(int, input().split())

net = up - down

if (tree-up) % net == 0:
    day = ((tree-up) // net)+1
else:
    day = ((tree-down) // net) + 1

print(day)

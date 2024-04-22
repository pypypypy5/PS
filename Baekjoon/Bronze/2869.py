up, down, tree = map(int, input().split())
day = 0

net = up - down

residue = tree % net
if residue > down:
    day = ((tree-residue) // net) + 1
else:
    day = (tree-residue) // net

print(day)

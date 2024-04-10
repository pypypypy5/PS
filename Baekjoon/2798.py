N, M = map(int, input().split())

cards = list(map(int, input().split()))
candidates = []
for i in range(len(cards)):
    for j in range(i+1,len(cards)):
        for m in range(j+1,len(cards)):
            sum = cards[i] + cards[j] + cards[m]
            if sum <= M:
                candidates.append(sum)

candidates.sort()          
print(candidates[-1])
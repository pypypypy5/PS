import sys
input = sys.stdin.readline

N = int(input())
pole = []
dp = [1 for i in range(N)]
for i in range(N):
    pole.append(list(map(int, input().split(' '))))

pole.sort()
for i in range(N):
    pole[i] = pole[i][1]

for i in range(N):
    for j in range(i):
        if pole[i] > pole[j] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1

print(N-max(dp))

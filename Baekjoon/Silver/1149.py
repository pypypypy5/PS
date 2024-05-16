import sys
input = sys.stdin.readline

N = int(input())
costs = []
for i in range(N):
    costs.append(tuple(map(int, input().split(' '))))

dp = [[0]*3 for i in range(N)]

dp[0][0] = costs[0][0]
dp[0][1] = costs[0][1]
dp[0][2] = costs[0][2]

for i in range(1,N):
    dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])

mini_c = min(dp[N-1][0],dp[N-1][1],dp[N-1][2])
print(mini_c)

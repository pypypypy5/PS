import sys
input = sys.stdin.readline

num, max_weight = map(int, input().split(' '))
things = [(0,0)]
dp = [[0]*(max_weight+1) for i in range(num+1)]

for i in range(num):
    weight, value = map(int, input().split(' '))
    things.append((weight,value))

for i in range(1,num+1):
    for j in range(1,max_weight+1):
        w = things[i][0]
        v = things[i][1]

        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-w]+v,dp[i-1][j])

print(dp[num][max_weight])

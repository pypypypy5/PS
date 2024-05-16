import sys
input = sys.stdin.readline

N = int(input())
costs = []
for i in range(N):
    costs.append(tuple(map(int, input().split(' '))))

dp_l = [0 for i in range(N)]
lowest = 1000000

def dp(now_idx):
    global lowest
    for i in range(0,3):
        cur = costs[now_idx][i]
        if now_idx == 0:
            dp_l[0] = cur
        else:
            cur_sum = cur + dp_l[now_idx-1]
            dp_l[now_idx] = cur_sum
            if now_idx == N-1:
                if lowest > cur_sum:
                    lowest = cur_sum
            else:
                dp(now_idx+1)

dp(0)
print(lowest)

W = int(input())
N = int(input())
P = list(map(int, input().split()))


dp = [[False for i in range(W + 10)] for i in range(N + 1)]
dp[0][0] = True
for i in range(N):
    for j in range(W):
        if dp[i][j]:
            dp[i+1][j] = dp[i][j]
        if dp[i+1][j]:
            dp[i+1][j + P[i]] = dp[i+1][j]

print(dp[N][W])

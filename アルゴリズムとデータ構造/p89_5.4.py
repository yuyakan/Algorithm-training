W = int(input())
N = int(input())
P = list(map(int, input().split()))
M = 10100

dp = [[False for i in range(M + 100)] for i in range(N + 1)]
dp[0][0] = True
for i in range(N):
    for j in range(M):
        if dp[i][j]:
            dp[i+1][j] = dp[i][j]
            dp[i+1][j + P[i]] = dp[i][j]

print(dp[N][W])

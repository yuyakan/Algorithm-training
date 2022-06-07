from re import I


N, W = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False for i in range(W+1)] for i in range(N+1)]
dp[0][0] = True

for i in range(N):
    for j in range(W):
        if dp[i][j]:
            dp[i + 1][j] = dp[i][j]
            if j + A[i] <= W:
                dp[i + 1][j + A[i]] = dp[i][j]

print(dp[N][W])
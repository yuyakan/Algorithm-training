W = int(input())
N = int(input())
P = list(map(int, input().split()))
M = list(map(int, input().split()))


dp = [[float("inf") for i in range(W + 10)] for i in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    for j in range(W):
        if dp[i][j] < float('inf'):
            dp[i+1][j] = min(dp[i+1][j],0)
        if j >= P[i] and dp[i+1][j-P[i]]+1:
            dp[i+1][j] = min(dp[i+1][j], dp[i+1][j-P[i]]+1)

if dp[N][W] < float("inf"):
    print("Yes")
else:
    print("No")
N, K = map(int, input().split())

a = list(map(int, input().split()))

dp = [[0 for i in range(K+5)]for i in range(N+5)]
for i in range(1,a[0]+2):
    dp[0][i] = 1

a.insert(0,0)
s = 0
for i in range(0,N):
    dp[i+1][0] = dp[i][0]
    for j in range(K):
        dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1]
    for j in range(K):
        l = max(j-a[i],0)
        dp[i+1][j+1] -= dp[i+1][l]


print(dp[N][K] % (1000000000+7))
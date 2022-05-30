H, W = map(int, input().split())

a = [[]for i in range(H)]

for i in range(H):
    a[i] = input()

dp = [[0 for i in range(W+1)]for i in range(H+1)]
dp[0][1] = 1
for i in range(H):
    for j in range(W):
        if a[i][j] == ".":
            dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j]
        else:
            dp[i+1][j+1] = 0

print(dp[H][W] % (1000000000 + 7))
        
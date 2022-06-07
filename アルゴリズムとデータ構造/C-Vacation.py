N = int(input())

A = []
B = []
C = []

for i in range(N):
    a, b, c = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)

dp = [[0 for i in range(N+1)] for i in range(3)]
for i in range(N):
    dp[0][i+1] = max(dp[1][i] + A[i], dp[2][i] + A[i])
    dp[1][i+1] = max(dp[0][i] + B[i], dp[2][i] + B[i])
    dp[2][i+1] = max(dp[0][i] + C[i], dp[1][i] + C[i])

print(max(dp[0][N], dp[1][N], dp[2][N]))
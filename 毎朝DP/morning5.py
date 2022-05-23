N, W = map(int,input().split())
w = [0 for i in range(N)]
v = [0 for i in range(N)]
for i in range(N):
    w[i], v[i] = map(int, input().split())



DP = [[10 ** 11 for i in range(N*1000+1)]for i in range(N+1)]
DP[0][0] = 0

for i in range(N):
    for j in range(N * 1000):
        DP[i+1][j] = min(DP[i+1][j], DP[i][j])
        if j + v[i] <= N*1000:
            DP[i+1][j+v[i]] = min(DP[i+1][j+v[i]], DP[i][j]+w[i])

l = DP[N]
indexes = [i for i, x in enumerate(l) if x <= W]

print(indexes[-1])
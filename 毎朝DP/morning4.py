N, W = map(int, input().split())

w = []
v = []

for i in range(N):
    w_i, v_i = map(int, input().split())
    w.append(w_i)
    v.append(v_i)

DP = [[0 for i in range(W+1)]for i in range(N+1)]
for i in range(N):
    for j in range(W):
        if (j + w[i]) <= W:
            DP[i+1][j + w[i]] = max(DP[i][j + w[i]], v[i] + DP[i][j])
        DP[i+1][j] = max(DP[i+1][j], DP[i][j])
print(DP[N][W])
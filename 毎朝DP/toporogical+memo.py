N, M = map(int, input().split())
x = []
y = []
for i in range(M):
    tmp_x, tmp_y = map(int, input().split())
    x.append(tmp_x)
    y.append(tmp_y)

dp = [-1 for i in range(100100)]
G = [[]for i in range(N+1)]

for i in range(M):
    G[x[i]].append(y[i])

def rec(v) :
    if (dp[v] != -1) :#更新済みなら飛ばす
        return dp[v]

    res = 0
    for nv in G[v]:#子の最大値に1足したものと比較
        res = max(res,rec(nv) + 1)
    dp[v] = res
    return dp[v]

res = 0
for v in range(1,N+1):
   res =  max(res,rec(v))

print(res)

N = int(input())
a = list(map(int, input().split()))


# sumCost = 0
# cost = float('inf')
# minId = 0

# while len(a) >= 2:
#     for i in range(len(a)-1):
#         if cost > a[i] + a[i+1]:
#             cost = a[i]+a[i+1]
#             minId = i
#     sumCost += cost
#     a.pop(minId)
#     a.pop(minId)
#     a.insert(minId,cost)
#     cost = float('inf')
#     minId = 0

# print(sumCost)


pre = [0]
for i in a:
    pre.append(pre[-1]+i)

dp = [[float('inf') for i in range(N+1)] for i in range(N+1)]

for l in range(N,-1,-1):
    for r in range(1,N+1):
        if r <= l:
            dp[l][r] = 0
        else:
            dp[l][r] = pre[r] - pre[l-1] + min(dp[l][i]+dp[i+1][r] for i in range(l,r))
print(dp[1][N])


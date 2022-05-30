N = int(input())
a = list(map(int, input().split()))

Inf = 1000000000000

dp = [[Inf for i in range(N+1)]for i in range(N+1)]

def rec(l, r):
    if l == r:
        return 0
    if dp[l][r] != Inf:
        return dp[l][r]
    
    if (N - (r-l)) % 2 == 0:
        dp[l][r] = max(a[l] + rec(l+1, r), rec(l, r-1) + a[r-1])
    else:
        dp[l][r] = min(-a[l] + rec(l+1, r), rec(l, r-1) - a[r-1])
    
    return dp[l][r]

    
rec(0,N)
print(dp[0][N])
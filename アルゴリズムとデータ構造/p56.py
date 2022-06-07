W = 10
N = int(input())
a = []
for i in range(N):
    a.append(int(input()))

dp = [[False for i in range(N)] for i in range(W+1)]
def f(W, N):
    if N == 0:
        if W == 0: return True
        return False
    
    if dp[W][N-1]: return True
    if dp[W - a[N-1]][N-1]: return True

    if f(W - a[N-1], N-1): return True
    if f(W, N-1): return True

    return False

print(f(10,N))

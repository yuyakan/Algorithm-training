N = int(input())
A = list(map(int, input().split()))

dp = [0 for i in range(N)]


for i in range(N-1):
    count = 0
    for j in range(N):
        for k in range(N):
            if A[i+1]/A[j] == A[k]:
                count += 1
                break
    dp[i+1] = max(dp[i+1], dp[i] + count)

print(dp)

S = input()
T = input()

dp = [[0 for i in range(len(T)+1)]for i in range(len(S)+1)]
for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])

print(dp[-1][-1])

        

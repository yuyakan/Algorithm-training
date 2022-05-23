s = input()
t = input()

dp = [[0 for i in range(len(t)+1)]for i in range(len(s)+1)]
for i in range(len(s)):
    for j in range(len(t)):
        if  s[i] == t[j]:
           dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])


i = len(s)
j = len(t)
ans = ""
while dp[i][j]>0:
    if s[i-1]==t[j-1] :
        ans += s[i-1]
        i -= 1
        j -= 1
    elif dp[i][j]==dp[i-1][j]:
        i -= 1
    else:
        j -= 1

print(''.join(list(reversed(ans))))
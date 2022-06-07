s = input()
t = input()

dp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]

for i in range(len(s)):
    for j in range(len(t)):
        dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j] + 1

s_index = len(s)
t_index = len(t)
ans = ""
while s_index :
    if dp[s_index][t_index] == dp[s_index - 1][t_index]:
        s_index -= 1
    elif dp[s_index][t_index] == dp[s_index][t_index - 1]:
        t_index -= 1
    else:
        ans += s[s_index-1]
        s_index -= 1
        t_index -= 1
r_ans = [x for x in reversed(ans)]
print(ans)

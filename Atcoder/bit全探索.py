S = input()

n = len(S) - 1
# 指標を先に作る感じ
ans = 0
for i in range(1 << n):
    f = S[0]
    for j in range(n):
        if i & 1 << j:
            f += '+'
        f += S[j+1]
    ans += sum(map(int, f.split('+')))

print(ans)


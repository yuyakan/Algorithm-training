n = int(input())
dp = [0] * (1 << n)
dp[0] = 1
curr = {0}
MOD = 10 ** 9 + 7
for i in range(n):
    compatibilities = [1 << i for i, v in enumerate(input().split()) if v == '1']
    print(compatibilities)
    nxt = set()
    for k in curr:
        p = dp[k] % MOD
        for c in compatibilities:
            if k & c:
                continue
            dp[k | c] += p
            nxt.add(k | c)
    curr = nxt
print(dp[(1 << n) - 1] % MOD)
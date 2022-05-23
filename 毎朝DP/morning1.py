N = int(input())
h = list(map(int,input().split(" ")))

h.insert(0,0)
DP = [0 for i in range(N+1)]
DP[2] = abs(h[1] - h[2])
if N >= 3:
 DP[3] = min(DP[2] + abs(h[2] - h[3]), abs(h[1] - h[3]))

for i in range(4, N+1):
    DP[i] = min(DP[i-1] + abs(h[i-1] - h[i]), DP[i-2] + abs(h[i-2] - h[i]))
print(DP[N])
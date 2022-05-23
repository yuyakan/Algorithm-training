N, K = map(int,input().split())
h = list(map(int, input().split()))

DP = [float('inf') for i in range(N)]
DP[0] = 0

for i in range(N-1):
  for k in range(1,K+1):
    if (k + i) >= N:
      break
    DP[i+k] = min(DP[i+k], DP[i] + abs(h[i]-h[i+k]))
print(DP[-1])


# N, K = map(int,input().split())
# h = list(map(int, input().split()))
 
# h.insert(0,0)
# DP = [float('inf') for i in range(N+1)]
# DP[1] = 0
 
# for i in range(1,N):
#   for k in range(1,K+1):
#     if (k + i) > N:
#       break
#     DP[i+k] = min(DP[i+k], DP[i] + abs(h[i]-h[i+k]))
# print(DP[-1])

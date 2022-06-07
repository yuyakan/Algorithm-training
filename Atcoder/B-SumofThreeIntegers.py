K,N = map(int, input().split())
count = 0
for i in range(K+1):
    for j in range(K+1):
        if N - K <= i + j <= N:
            count += 1
print(count)



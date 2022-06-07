N, W = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

ansers = []
for i in range(N):
    if A[i] <= W:
        ansers.append(A[i])

for i in range(N):
    for j in range(i+1,N):
        if (A[i] + A[j]) <= W:
            ansers.append(A[i] + A[j])

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if (A[i] + A[j] + A[k]) <= W:
                ansers.append(A[i] + A[j] + A[k])

print(len(list(set(ansers))))
from tabnanny import check


N, K = map(int, input().split())
S = []
for i in range(N):
    S.append(input())

maxCount = 0
for i in range(2 ** N):
    A = ""
    count = 0
    for j in range(N):
        if i & 1 << j:
            A += S[j]
            
    checkS = list(set(A))
    for j in checkS:
        if A.count(j) == K:
            count += 1
    
    if count > maxCount:
        maxCount = count

print(maxCount)
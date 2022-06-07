N, A, B = map(int, input().split())

ans = [[] for i in range(N * A)]
for i in range(N):
    for j in range(N):
        if (i+j) % 2 == 0:
            for l in range(A):
                for k in range(B):
                    ans[i * A + l].append(".")
        else:
            for l in range(A):
                for k in range(B):
                    ans[i * A + l].append("#")

for i in range(N * A):
    print(*ans[i], sep="")
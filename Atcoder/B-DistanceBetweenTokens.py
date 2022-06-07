H, W = map(int, input().split())

S = []
for i in range(H):
    s = input()
    S.append(s)

count = 0
indexes = [[0,0],[0,0]]
for i in range(H):
    for j in range(W):
        if S[i][j] == "o":
            indexes[count] = [i, j]
            count += 1

ans = abs(indexes[0][0] - indexes[1][0]) + abs(indexes[0][1] - indexes[1][1])
print(ans)


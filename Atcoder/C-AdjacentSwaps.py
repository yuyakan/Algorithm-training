N, Q = map(int, input().split())
x = []
for i in range(Q):
    x.append(int(input()))

ans = []
pos = []
ans.append(0)
pos.append(0)
for j in range(N):
    ans.append(j + 1)
    pos.append(j + 1)

for i in range(Q):
    if pos[x[i]] == N:
        tmp = ans[pos[x[i]]]

        ans[pos[x[i]]] = ans[1]
        pos[ans[1]] = pos[x[i]]

        ans[1] = tmp
        pos[x[i]] = 1
    else:
        tmp = ans[pos[x[i]]]
        
        ans[pos[x[i]]] = ans[pos[x[i]] + 1] 
        pos[ans[pos[x[i]] + 1]] = pos[x[i]]

        ans[pos[x[i]] + 1] = tmp
        pos[ans[pos[x[i]]]]


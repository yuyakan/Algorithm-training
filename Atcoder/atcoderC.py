N = int(input())
S = ["" for i in range(N)]
for i in range(N):
    S[i] = input()

kaburi_list = [[0 for i in range(10)] for j in range(10)]
for i in range(10):
    for j in range(N):
        kaburi_list[i][int(S[j][i])] += 1

sum_list = [0 for i in range(10)]
for i in range(10):
    l = [r[i] for r in kaburi_list]
    maxi = max(l)
    indexes = [i for i, x in enumerate(l) if x == maxi]
    sum_list[i] = indexes[-1] + (kaburi_list[indexes[-1]][i] - 1) * 10
print(min(sum_list))



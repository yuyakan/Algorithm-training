
N = int(input())

S = []
T = []

for i in range(N):
    s, t = map(str, input().split())
    S.append(s)
    T.append(int(t))

dict = {}
for i in range(N):
    if S[i] not in dict:
        dict[S[i]] = [T[i], i]

max_id = 0
max_score = 0

for i in range(N):
    if dict[S[i]][0] > max_score:
        max_score = dict[S[i]][0]
        max_id = dict[S[i]][1]

print(max_id + 1)

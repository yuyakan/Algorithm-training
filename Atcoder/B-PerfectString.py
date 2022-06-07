S = input()

count = [0,0]
for i in range(len(S)):
    if S[i].isupper(): 
        count[0] = 1
    if S[i].islower(): 
        count[1] = 1

if (len(S) == len(list(set(S)))) & (count[0] == 1) & (count[1] == 1):
    print("Yes")
else:
    print("No")
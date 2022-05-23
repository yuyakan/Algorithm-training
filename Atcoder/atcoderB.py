N ,K = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))



indexes = [i + 1 for i, x in enumerate(A) if x == max(A)]
print(indexes)
for i in B:
    for j in indexes:
        if i == j:
            print("Yes")
            quit()

print("No")
n = int(input())
a = list(map(int, input().split()))

print(str(min(a)) + " " + str(max(a)))

a.sort()
print(*a, sep="")
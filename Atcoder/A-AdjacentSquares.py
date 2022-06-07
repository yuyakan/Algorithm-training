H, W = map(int, input().split())
R, C = map(int, input().split())


l = 2
r = 2
if H == 1:
    l = 1
if W == 1:
    r = 1

if R != H and R != 1:
    if C != W and C != 1:
        print(l + r)
    else:
        print(l + r - 1)
else:
    if C != W and C != 1:
        print(l + r - 1)
    else:
        print(l + r - 2)

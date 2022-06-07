A, B, C, D, E, F, X = map(int, input().split())

taka = 0
ao = 0

takaset = X // (A + C) 
takaamari = X %  (A + C)
aoset = X // (D + F)
aoamari = X % (D + F)

taka = A * B * takaset
if takaamari >= A:
    taka += A * B
else:
    taka += takaamari * B

ao = D * E * aoset
if aoamari >= D:
    ao += D * E
else:
    ao += aoamari * E

if taka > ao:
    print("Takahashi")
elif taka == ao:
    print("Draw")
else:
    print("Aoki")
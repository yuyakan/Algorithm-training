N = 8

T = [-1 for i in range(100)]

def tri(N):
    if N == 0:
        return 0
    elif N == 1:
        return 0
    elif N == 2:
        return 1

    if T[N] != -1:
        return T[N]

    T[N] = tri(N-1) + tri(N-2) + tri(N-3)
    return T[N]

print(tri(N))
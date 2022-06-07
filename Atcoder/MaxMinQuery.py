import bisect

Q = int(input())

S = []

for i in range(Q):
    s = list(map(int, input().split()))

    ary_s = s[0]

    if ary_s == 1:
        bisect.insort(S,s[1])

    elif ary_s == 2:
        insert_start = bisect.bisect_left(S,s[1])
        insert_end = bisect.bisect_right(S,s[1])
        
        del_num = min(s[2], insert_end - insert_start)
        del S[insert_start:insert_start + del_num]
            
    else:
        print(S[-1] - S[0])

                
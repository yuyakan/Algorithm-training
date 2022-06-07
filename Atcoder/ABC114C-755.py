N = int(input())

def func(cur, use, counter):
    if cur > N: return
    if use == 0b111: counter += 1

    func(cur * 10 + 7, use | 0b001, counter)
    func(cur * 10 + 5, use | 0b010, counter)
    func(cur * 10 + 3, use | 0b100, counter)

res = []
func(0, 0, res)
print(sum(res))
    

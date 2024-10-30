p = [56,12,1,99,1000,234,33,55,99,812]
p2 = p[:]
p2.sort()
a = []
i = 0
for y in p2:
    if i > 0:
        c = y
        if c == b:
            continue
        a.append([i for i,x in enumerate(p) if x == y])
        b = int(y)
    else:
        a.append([i for i, x in enumerate(p) if x == y])
        b = int(y)
        i += 1
print(a)
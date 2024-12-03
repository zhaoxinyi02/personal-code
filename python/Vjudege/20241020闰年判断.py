n = int(input())
l = []
for year in range(2024,2025+n):
    if year % 100 != 0:
        if year % 4 == 0:
            l.append(year)
        else:
            pass
    else:
        if year % 400 == 0:
            l.append(year)
        else:
            pass
a = 0
for i in l:

    print(i,end=",")
    a += 1
    if a % 10 == 0:
        print()
print()
print(len(l))
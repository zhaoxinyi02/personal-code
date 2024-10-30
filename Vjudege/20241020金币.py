def caco(n):
    i = 0
    while n != 0:
        i += n
        n -= 1
    return i
k = int(input())
a = 0
i = 1
while a < k:
    i += 1
    a = caco(i)
money1 = 0
for day in range(1,i):
    money1 += pow(day,2)
money2 = (k-caco(i-1))*i
print(money1 + money2)
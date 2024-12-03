n = int(input())
def test(num):
    if n > 4 and n <= 12 :
        return 1
    else:
        return 0
def test2(num):
    if n % 2 == 0 and test(num)  == 0:
        return 1
    elif n % 2 != 0 and test(num)  == 1:
        return 1
    else:
        return 0
if n % 2 == 0 and test(n) == 1:
    print(1,end=' ')
else:
    print(0,end=' ')
if n % 2 == 0 or test(n) == 1:
    print(1,end=' ')
else:
    print(0,end=' ')
if test2(n) == 1:
    print(1,end=' ')
else:
    print(0,end=' ')
if n % 2 != 0 and test(n) == 0:
    print(1,end=' ')
else:
    print(0,end=' ')

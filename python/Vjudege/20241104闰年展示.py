nums = input()
num1 = int(nums.split(' ')[0])
num2 = int(nums.split(' ')[1])
l = []
for year in range(num1,num2+1):
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
print(len(l))
for i in l:
    print(i,end=' ')
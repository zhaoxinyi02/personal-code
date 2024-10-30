nums = input()
num1 = int(nums.split(' ')[0])
num2 = int(nums.split(' ')[1])
l = [0,0,0,0,0,0,0,0,0,0]
for i in range(num1,num2+1):
    istr = str(i)
    for j in istr:
        l[int(j)] += 1
for i in range(10):
    if l[i] == 0:
        pass
    else:
        print(str(i) + ':' + str(l[i]))
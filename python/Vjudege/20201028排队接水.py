num = int(input())
times = input()
times_list = []
for i in range(num):
    time = int(times.split(" ")[i])
    times_list.append(time)
times_list2 = times_list[:]
times_list2.sort()
a = []
i = 0
for y in times_list2:
    if i > 0:
        c = y
        if c == b:
            continue
        a.append([i for i,x in enumerate(times_list) if x == y])
        b = int(y)
    else:
        a.append([i for i, x in enumerate(times_list) if x == y])
        b = int(y)
        i += 1
for i in a:
    for j in i:
        print(j+1,end=' ')
j = 0
for i in range(num-1):
    j += times_list2[i] * (num-1-i)
t = j/num
print()
print('%.2f'%t)


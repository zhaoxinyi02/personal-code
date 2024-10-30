def select(list):
    n = len(list)
    for i in range(n - 1):
        max = i
        for j in range(i+1,n):
            if list[j] < list[max]:
                max = j
        list[i],list[max] = list[max],list[i]
    return list

llist = [[12,0,8,9,6,1,21,46],[3,88,-2,90,100],[6,-3,9,12,44,0,50,70,-23,8]]
for i in llist:
    i = select(i)
print(llist)
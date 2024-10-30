def select(list):
    n = len(list)
    for i in range(n - 1):
        max = i
        for j in range(i+1,n):
            if list[j] > list[max]:
                max = j
        list[i],list[max] = list[max],list[i]
    print(list)

list = [12,0,10,9,8,-1,21,-6]
select(list)
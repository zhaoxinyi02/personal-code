def insert(list):
    n = len(list)
    for i in range(1,n):
        x = list[i]
        j = i - 1
        while j >= 0:
            if x >= list[j]:
                list[j+1] = list[j]
                j -= 1
            else:
                break
        list[j+1] = x
    print(list)
list = [12,0,10,9,8,-1,21,-6]
insert(list)
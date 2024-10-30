def bubble(list):
    l = len(list)
    for i in range(0,l-1):
        for j in range(0,l-1):
            if list[j] < list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    print(list)
list = [12,0,10,9,8,-1,21,-6]
bubble(list)
def entry(list):
    for i in range(1,len(list)):
        num = list[i]
        j = i - 1
        while j >= 0:
            if list[j] < num:
                list[j+1] = list[j]
                j-=1
            else:
                break
        list[j+1] = num

    print(list)

list = [12,0,10,9,8,-1,21,-6]
entry(list)
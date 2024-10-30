def select(list):
    for begin in range(0,len(list)):
        max = begin
        for i in range(begin,len(list)):
            if list[i] > list[begin]:
                list[i],list[begin] = list[begin],list[i]
    print(list)

list = [12,0,10,9,8,-1,21,-6]
select(list)
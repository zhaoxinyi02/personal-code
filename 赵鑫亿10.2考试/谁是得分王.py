p = 1
namelist = []
sorcelist = []
print("______成绩录入______")
while p<=4:
    name = input("请输入名字")
    namelist.append(name)
    sorce = int(input("请输入分数"))
    sorcelist.append(sorce)
    p+=1
print("序号   姓名   成绩")
#print(namelist,sorcelist)
for i in range(0,len(namelist)):
    print(i+1,"   ",namelist[i],"  ",sorcelist[i])


sorcelist_new = sorcelist[:]
sorcelist_new.sort()
high = sorcelist_new[len(namelist)-1]
num = sorcelist.index(high)
#print(num)
print("本小组最好成绩的同学为：",namelist[num],"TA的得分为：",high)




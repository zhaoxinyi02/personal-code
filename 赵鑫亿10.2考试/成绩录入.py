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



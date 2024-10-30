cishu = int(input())
result_list = []

def jia(num1,num2):
    result = num1 + num2
    re = str(num1)+'+'+str(num2)+'='+str(result)
    result_list.append(re)

def jian(num1,num2):
    result = num1 - num2
    re = str(num1)+'-'+str(num2)+'='+str(result)
    result_list.append(re)
def cheng(num1,num2):
    result = num1 * num2
    re = str(num1)+'*'+str(num2)+'='+str(result)
    result_list.append(re)

a = 0
for i in range(cishu):
    data = input()
    data_list = data.split(" ")
    if len(data_list) == 3:
        if data_list[0] == 'a':
            a = 1
            data_list.remove('a')
        elif data_list[0] == 'b':
            a = 2
            data_list.remove('b')
        elif data_list[0] == 'c':
            a = 3
            data_list.remove('c')
    if a == 1:
        jia(int(data_list[0]), int(data_list[1]))
    if a == 2:
        jian(int(data_list[0]), int(data_list[1]))
    if a == 3:
        cheng(int(data_list[0]), int(data_list[1]))

for i in range(cishu):
    print(result_list[i])
    print(len(result_list[i]))
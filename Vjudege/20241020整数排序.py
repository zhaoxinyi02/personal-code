n_list = []
nums = input()
num1 = int(nums.split(" ")[0])
num2 = int(nums.split(" ")[1])
num3 = int(nums.split(" ")[2])
n_list.append(num1)
n_list.append(num2)
n_list.append(num3)
n_list.sort()
for i in n_list:
    print(i,end=" ")

nums = input()  #第一行输入
n = int(nums.split(" ")[0])
c = int(nums.split(" ")[1])

nums2 = input()    #第二行输入
num_list = [int(num) for num in nums2.split(' ')]
#for i in range(n):
#    num = int(nums2.split(" ")[i])
#    num_list.append(num)
num_list.sort()

a = 0
# print(num_list)
for i in num_list:
    a += num_list.count(i - c)

print(a)
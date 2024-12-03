nums = input()  #第一行输入
n = int(nums.split(" ")[0])
c = int(nums.split(" ")[1])

nums2 = input()    #第二行输入
num_list = [int(num) for num in nums2.split(' ')]
#for i in range(n):
#    num = int(nums2.split(" ")[i])
#    num_list.append(num)
num_list.sort()
#print(num_list)



i = int(len(num_list)) - 1      #双指针从后往前
j = int(len(num_list)) - 1
a = 0
while i != -1:

    if num_list[j] == num_list[i] + c:
#        print(num_list[j],"-",num_list[i])
        a += num_list.count(num_list[i]) * num_list.count(num_list[j])
        i -= num_list.count(num_list[i])
    elif num_list[j] < num_list[i] + c:
        i -= 1
    elif num_list[j] > num_list[i] + c:
        j -= 1
print(a)
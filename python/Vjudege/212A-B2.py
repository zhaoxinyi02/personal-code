import bisect

def count(arr, target):
    left_in = bisect.bisect_left(arr, target)
    right_in = bisect.bisect_right(arr, target)
    return right_in - left_in

nums = input()  #第一行输入
n = int(nums.split(" ")[0])
c = int(nums.split(" ")[1])
#num_list = []
nums2 = input()    #第二行输入

num_list = [int(num) for num in nums2.split(" ")]

# for i in range(n):
#     num = int(nums2.split(" ")[i])
#     num_list.append(num)
num_list.sort()
#print(num_list)

a = 0
# print(num_list)
for i in num_list:
    a += count(num_list, i - c)

print(a)

#先求得差，在列表里面找差，右插入减去左插入就是该元素的个数
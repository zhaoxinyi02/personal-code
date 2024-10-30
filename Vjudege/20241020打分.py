n = int(input())
nums = input()
nums_list = nums.split(" ")
for i in range(len(nums_list)):
    nums_list[i] = int(nums_list[i])
nums_list.remove(max(nums_list))
nums_list.remove(min(nums_list))
source = 0
for i in nums_list:
    source += i
s = source / len(nums_list)
print("%.2f"%s)
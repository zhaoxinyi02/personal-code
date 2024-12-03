n = input()
nums = input()
nums_list = nums.split(" ")
for i in range(len(nums_list)):
    nums_list[i] = int(nums_list[i])
cha = max(nums_list) - min(nums_list)
print(cha)
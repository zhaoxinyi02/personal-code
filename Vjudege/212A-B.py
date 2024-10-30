nums = input()
n = int(nums.split(" ")[0])
c = int(nums.split(" ")[1])
num_list = []
nums2 = input()
for i in range(n):
    num = int(nums2.split(" ")[i])
    num_list.append(num)
num_list.sort()
#print(num_list)
i = int(len(num_list)) - 1
j = int(len(num_list)) - 1
a = 0
while i != -1:

    if num_list[j] == num_list[i] + c:
#        print(num_list[j],"-",num_list[i])
        a += 1
        i -= 1
    elif num_list[j] < num_list[i] + c:
        i -= 1
    elif num_list[j] > num_list[i] + c:
        j -= 1
print(a)
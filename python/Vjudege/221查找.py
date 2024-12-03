import bisect

nums = input()  #第一行输入
n = int(nums.split(" ")[0])
c = int(nums.split(" ")[1])

nums2 = input()    #第二行输入
num_list = [int(num) for num in nums2.split(" ")]
print(num_list)

nums3 = input()    #第三行输入
num_list2 = [int(num) for num in nums3.split(" ")]
print(num_list2)

for i in num_list2:
    print(i)
    j = bisect.bisect_left(num_list,i)
#    print(j)
#    print(len(num_list))
#    print(num_list[j])
    if j != len(num_list) and num_list[j] == i:
        print(j+1)
    else:
        print(-1)
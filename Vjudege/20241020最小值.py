n_list = []
n = int(input())
nums = input()
for i in range(0,n):
    numn = int(nums.split(" ")[i])
    n_list.append(numn)
print(min(n_list))

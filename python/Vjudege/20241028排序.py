n = int(input())
nums = input()
nums_list = []
for i in range(n):
    nums_list.append(nums.split(' ')[i])

def bubble(list):
    n = len(list)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list

nums_list = bubble(nums_list)

for i in range(n-1):
    print(nums_list[i],end=' ')
print(nums_list[n-1],end="")

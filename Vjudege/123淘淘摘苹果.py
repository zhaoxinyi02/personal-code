apples = []
apples2 = []
nums = input()
high = int(input())
for i in range(0,10):
    apples.append(int(nums.split(" ")[i]))
for i in apples:
    if i > high + 30:
        pass
    else:
        apples2.append(i)
print(len(apples2))

num_list = [0,0,0,0,0,0,0,0,0,0]
nums = input()
num1 = int(nums.split(" ")[0])
num2 = int(nums.split(" ")[1])
if num1 > num2:
    for i in range(num2,num1+1):
        while i > 0:
            digit = i % 10
            num_list[digit] += 1
            i //= 10
else:
    for i in range(num1,num2+1):
        while i > 0:
            digit = i % 10
            num_list[digit] += 1
            i //= 10
for i in range(0,10):
    print(num_list[i],end=" ")





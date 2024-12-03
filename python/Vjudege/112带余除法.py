nums = input()
num1 = int(nums.split(" ")[0])
num2 = int(nums.split(" ")[1])
yu = num1 % num2
r = int((num1 - yu)/num2)
print(r,yu)
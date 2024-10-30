def akm(m,n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akm(m - 1,1)
    elif m > 0 and n > 0:
        return akm(m - 1,akm(m,n - 1))

nums = input()
num1 = float(nums.split(" ")[0])
num2 = float(nums.split(" ")[1])
print(akm(num1,num2))

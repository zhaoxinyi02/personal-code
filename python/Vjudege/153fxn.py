nums = input()
num1 = float(nums.split(" ")[0])
num2 = float(nums.split(" ")[1])
def f(x,n):
    if n == 1:
        return pow(1 + x,0.5)
    return pow(n + f(x,n-1),0.5)
a = f(num1,num2)
print("%.2f"%a)
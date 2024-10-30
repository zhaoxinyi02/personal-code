data = input()
students = int(data.split(' ')[0])
cishu = int(data.split(' ')[1])
nums = input()
ask = input()
for i in range(cishu):
    print(int(nums.split(' ')[int(ask.split(' ')[i])-1]))
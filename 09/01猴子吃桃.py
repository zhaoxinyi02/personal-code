def monkey(num):
    return (num+1)*2
num = 1
for i in range(10):
    num = monkey(num)
print(num)
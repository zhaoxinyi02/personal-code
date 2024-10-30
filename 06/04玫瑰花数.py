flower_list = []
for num in range(1000,10000):
    num_str = str(num)
#    print(num_str)
    n1 = int(num_str[0])
    n2 = int(num_str[1])
    n3 = int(num_str[2])
    n4 = int(num_str[3])
    if pow(n1,4) + pow(n2,4) + pow(n3,4) + pow(n4,4) == num:
        flower_list.append(num)
    else:
        continue

print(flower_list)

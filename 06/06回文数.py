num_list = []
for num in range(10000,100000):
    num_str = str(num)
#    print(num_str)
#    print(num_str[:2])
#    print(num_str[-3:])
    if num_str[:3] == num_str[-3:]:
        num_list.append(num)
    else:
        continue

print(num_list)
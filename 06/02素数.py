num_list = []

for i in range(2,1001):
    num_list.append(i)
for num in range(2,1001):
    for i in range(2, num):
        if num % i == 0:

            num_list.remove(num)
            break

        else:

            continue


print(num_list)
print(len(num_list))


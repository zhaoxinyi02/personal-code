num_list = []
for num in range(12345678,98765433):
    num = str(num)

    num_2 = [x for x, y in list(enumerate(list(num))) if y == "2"]
    num_0 = [x for x, y in list(enumerate(list(num))) if y == "0"]
    num_3 = [x for x, y in list(enumerate(list(num))) if y == "3"]
    if len(num_2) == 2 and len(num_0) == 1 and len(num_3) == 1:
        if num_2[0] < num_0[0] < num_2[1] < num_3[0]:
            pass
        else:
            num_list.append(num)
    else:
        num_list.append(num)
print(len(num_list))
flower_list = []


def shuixianhua(num):
    num_str = str(num)

    n1 = int(num_str[0])
    n2 = int(num_str[1])
    n3 = int(num_str[2])

    if pow(n1, 3) + pow(n2, 3) + pow(n3, 3) == num:
        return 1
    else:
        return 0


for num in range(100,1000):
    tf = shuixianhua(num)
    if tf == 1:
        flower_list.append(num)
    else:
        continue

print(flower_list)
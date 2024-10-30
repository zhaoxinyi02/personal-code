coins_new = {}
coins_old = {}
for i in range(1,2024):
    i_str = str(i)
    coins_new[i_str] = i
for i in range(1,2024):
    i_str = str(i)
    coins_old[i_str] = 0

num_list = []

for num in range(1,2024):       #一种一种硬币堆
    coins_new2 = coins_new.copy()
    coins_old2 = coins_old.copy()
    for i in range(1,num):
        i2 = num - i
        if i2 == 0:
            num_list.append(0)
            break
        elif i == i2 and coins_new2[str(i)] == 1:
            break
        else:
            while True:

                if coins_new2[str(i)] == 0 or coins_new2[str(i2)] == 0:
                    break
                elif i == i2 and coins_new2[str(i)] == 1:
                    break

                else:

                    print(i, i2)
                    coins_new2[str(i)] -= 1
                    print(coins_new2[str(i)])
                    coins_new2[str(i2)] -= 1
                    print(coins_new2[str(i2)])
                    coins_old2[str(num)] += 1
    num_list.append(coins_old2[str(num)] + coins_new2[str(num)])

print(num_list)



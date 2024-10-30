import math
def tf_sushu(number):

    for i in range(2, number):
        num_list.append(i)
    for num in range(2, number):
        for i in range(2, num):
            if num % i == 0:

                num_list.remove(num)
                break

            else:

                continue


num_list = []
tf_sushu(1001)

print(num_list)
print(len(num_list))


nums = input()
num = int(nums.split(" ")[0])
time = int(nums.split(" ")[1])
ttime = int(nums.split(" ")[2])
if time == 0:
    print(0)
else:
    ate_apple = ttime // time
    if ttime % time == 0:
        pass
    else :
        ate_apple += 1
    new_num = num - ate_apple
    if new_num < 0:
        print(0)
    else:
        print(new_num)

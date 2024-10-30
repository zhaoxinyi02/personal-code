n = int(input())
num_str = input()
num_list = num_str.split(" ")
n_list = []
for i in range(0,n):
    n_list.append(0)

for fish in range(1,n):
    for fish2 in range(0,fish):
        if int(num_list[fish]) > int(num_list[fish2]):
            n_list[fish] += 1
        else:
            pass
for i in range(0,n):
    print(n_list[i],end=" ")
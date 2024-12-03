xs = []
ys = []
for i in range(3):
    nums = input()
    xs.append(float(nums.split(' ')[0]))
    ys.append(float(nums.split(' ')[1]))
l = pow(pow(xs[0]-xs[1],2)+pow(ys[0]-ys[1],2),0.5) + pow(pow(xs[2]-xs[1],2)+pow(ys[2]-ys[1],2),0.5) + pow(pow(xs[0]-xs[2],2)+pow(ys[0]-ys[2],2),0.5)
print('%.2f'%l)
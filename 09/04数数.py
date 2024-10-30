begin = int(input('请输入初始值'))
plus = int(input('请输入每次增加的最大值'))
def palyer1(present_num):
    i = int(input('玩家1：'))
    present_num += i

    print('当前值为：', present_num)
    return present_num

def palyer2(present_num):
    i = int(input('玩家2：'))
    present_num += i

    print('当前值为：', present_num)
    return present_num

present_num = begin
print('当前值为：',present_num)
while True:
    present_num = palyer1(present_num)
    if present_num >= 30:
        print('玩家2胜利')
        break
    present_num = palyer2(present_num)
    if present_num >= 30:
        print('玩家2胜利')
        break

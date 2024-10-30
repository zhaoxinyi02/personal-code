
from pynput.keyboard import Key,Listener


class Control():
    def __init__(self):
        self.dir_ = None # dir一定要用成员变量，不然没办法在on_press中修改

    def getdir(self):
        self.dir_ = None    # 如果是不是上下左右则返回None
        def on_press(key):
            if key == Key.up:self.dir_ = Direction.UP
            elif key == Key.down:self.dir_ = Direction.DOWN
            elif key == Key.left:self.dir_ = Direction.LEFT
            elif key == Key.right:self.dir_ = Direction.RIGHT
            return False
        listener = Listener(on_press=on_press) # 创建监听器
        listener.start()    # 开始监听，每次获取一个键
        listener.join()     # 加入线程
        listener.stop()     # 结束监听，没有这句也行，直接随函数终止
        return self.dir_


import enum
class Direction(enum.Enum):
    UP      = 1
    DOWN    = 2
    LEFT    = 3
    RIGHT   = 4


print("欢迎来到王者荣耀")
name = input("请输入英雄名")
print("好的",name)
xingbie = input("请输入性别")
print("好的",name)
nianling = int(input("请输入年龄"))
zhiye = int(input("请选择您的职业. 1.战士 2.坦克 3.法师 4.射手 5.辅助"))
zhiye -= 1
tf = input("是否需要合作伙伴")


zhiyelist = ["战士","坦克","法师","射手","辅助",]

if xingbie == "男":
    xingbie1 = "勇士"
elif xingbie == "女":
    xingbie1 = "女神"

if nianling <= 20:
    chenghu = "少年英雄"
elif nianling > 20:
    chenghu = "老江湖"

zhiye1 = zhiyelist[zhiye]

if tf == "是":
    print("欢迎您,",nianling,"岁的",name,xingbie1,"您选择的职业是；",zhiye1,",您不需要合作伙伴",",您真是个",chenghu)
elif tf =="否":
    print("欢迎您,",nianling,"岁的",name,xingbie1,"您选择的职业是；",zhiye1,",您需要合作伙伴",",您真是个",chenghu)

print("游戏开始，请用左右键移动英雄位置，当前位置为：泉水")

local = 0

locallist = ["泉水","水晶"]


while True:
    c = Control()
    move = str(c.getdir())
    if move == "Direction.LEFT":
        local-=1
    elif move == "Direction.RIGHT":
        local+=1
    else:
        print("请按正确按键")

    if local % 2 == 1:
        print("现在在泉水")
    elif local % 2 == 0:
        print("现在在水晶")





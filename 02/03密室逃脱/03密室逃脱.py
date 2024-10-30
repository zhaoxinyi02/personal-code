import time
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


print("欢迎来到古墓游戏")
print("游戏加载中......")
time.sleep(3)
input("加载完毕，按任意键进入游戏")

p = 1
print("欢迎来到古墓，你现在在古墓大门口，按向下键往前走")
while p != 100:
    c = Control()
    move = str(c.getdir())
    if move == "Direction.DOWN":
        p+=32
    elif move =="Direction.RIGHT":
        p+=11
    elif move =="Direction.LEFT":
        p-=11
    elif move =="Direction.UP":
        p-=32
    else:
        print("请按正确按键")

    if p == 1:
        print("你现在在古墓大门口")
    elif p == 33:
        print("你现在在主墓室，左右两边都有耳室，向前是出口，你可以去探索")
    elif p == 44:
        print("你现在在右耳室，是否选择翻棺材拿宝贝？（是/否）")
        tf = input()
        if tf == "是":
            print("恭喜你拿到了金银财宝，可以向左回主墓室")
        elif tf == "否":
            print("可以向左返回主墓室了")
    elif p == 22:
        print("你现在在左耳室，是否选择翻棺材拿宝贝？（是/否）")
        tf = input()
        if tf == "是":
            print("恭喜你拿到了金银财宝，可以向右回主墓室")
        elif tf == "否":
            print("可以向右返回主墓室了")
    elif p == 65:
        exit = input("现在在你面前有两个出口，选中正确的才可以出去。选择1或2")
        if exit == "1":
            print("你选择了正确的出口，游戏胜利！")
        elif exit == "2":
            print("你选错了！游戏失败！")
            break
        break






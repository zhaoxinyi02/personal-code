import turtle as t

from pygame.draw import circle

t.speed(0)
t.pensize(2)

# 黄色背景
def draw_circle(localx, localy, r, extent, framecolor, fillcolor):  # 初始x位置，初始y位置，半径，角度，边框颜色，填充颜色
    t.up()
    t.goto(localx, localy)
    t.color(framecolor)
    t.down()
    t.begin_fill()
    t.circle(r, extent)
    t.color(fillcolor)
    t.end_fill()
    t.seth(0)


def draw_mouth(localx, localy, torf):
    t.up()
    t.color("red")
    t.goto(localx, localy)
    t.down()
    if torf == "t":
        t.circle(67, 50)
        t.circle(67, -100)
        t.seth(0)
    elif torf == "f":
        t.circle(-67, 50)
        t.circle(-67, -100)
        t.seth(0)


def main():
    draw_circle(-100, -100, 100, 360, "red", "yellow")
    draw_mouth(-100, -67, "t")
    draw_circle(-133, 35, 13, 360, "red", "white")
    draw_circle(-133, 35, 9, 360, "black", "black")
    draw_circle(-69, 35, 13, 360, "red", "white")
    draw_circle(-69, 35, 9, 360, "black", "black")

    draw_circle(100, -100, 100, 360, "red", "yellow")
    draw_mouth(100, -33, "f")
    draw_circle(133, 35, 13, 360, "red", "white")
    draw_circle(133, 35, 9, 360, "black", "black")
    draw_circle(69, 35, 13, 360, "red", "white")
    draw_circle(69, 35, 9, 360, "black", "black")

    t.mainloop()


if __name__ == "__main__":
    main()

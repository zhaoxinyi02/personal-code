import turtle as t



t.speed(0)
t.pensize(2)
t.hideturtle()

def draw_star(localx,localy,len,angle):
    t.up()
    t.goto(localx,localy)
    t.left(angle)


    t.down()
    t.begin_fill()
    t.color("white")
    i = 1
    while i <= 5:
        t.forward(len)
        t.right(180 - 36)
        i += 1
    t.end_fill()
    t.up()
    t.seth(0)


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

def draw_mouth(localx, localy, torf,angle):       #初始x，初始y，正反
    t.up()
    t.color("red")
    t.goto(localx, localy)
    t.down()
    if torf == "t":
        t.circle(67, angle)
        t.circle(67, -2*angle)
        t.seth(0)
    elif torf == "f":
        t.circle(-67, angle)
        t.circle(-67, -2*angle)
        t.seth(0)


def main():

    draw_circle(-200,-200,200,360,"red","red")
    draw_circle(-200,-167,167,360,"white","white")
    draw_circle(-200,-134,134,360,"red","red")
    draw_circle(-200,-101,101,360,"blue","blue")
    draw_star(-294,30,189,0)


    draw_circle(200,-200,200,360,"red","red")
    draw_circle(200,-167,167,360,"white","white")
    draw_circle(200,-134,134,360,"red","red")
    draw_circle(200, -101, 101, 360, "red", "yellow")
    draw_mouth(200, -33, "f",50)
    draw_circle(167, 33, 13, 360, "red", "white")
    draw_circle(167, 33, 9, 360, "black", "black")
    draw_circle(233, 33, 13, 360, "red", "white")
    draw_circle(233, 33, 9, 360, "black", "black")


    t.mainloop()




if __name__ == "__main__":
    main()














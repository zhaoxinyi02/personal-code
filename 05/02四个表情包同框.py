import turtle as t



t.speed(0)
t.pensize(2)
t.hideturtle()

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


def draw_eye_frame(frame_color,fill_color,localx,localy,len,wid,r):
    t.color(frame_color)
    t.seth(0)
    t.left(90)
    t.up()
    t.goto(localx,localy)
    t.down()
    t.begin_fill()
    t.forward(wid)
    t.circle(r,90)
    t.forward(len)
    t.circle(r,90)
    t.forward(wid)
    t.circle(r,90)
    t.forward(len)
    t.circle(r,90)
    t.color(fill_color)
    t.end_fill()
    t.seth(0)


def main():
    draw_circle(-100, 0, 100, 360, "red", "yellow")
    draw_mouth(-100, 33, "t",50)
    draw_circle(-133, 135, 13, 360, "red", "white")
    draw_circle(-133, 135, 9, 360, "black", "black")
    draw_circle(-69, 135, 13, 360, "red", "white")
    draw_circle(-69, 135, 9, 360, "black", "black")

    draw_circle(100, 0, 100, 360, "red", "yellow")
    draw_mouth(100, 67, "f",50)
    draw_circle(133, 135, 13, 360, "red", "white")
    draw_circle(133, 135, 9, 360, "black", "black")
    draw_circle(69, 135, 13, 360, "red", "white")
    draw_circle(69, 135, 9, 360, "black", "black")

    draw_circle(-100, -200, 100, 360, "red", "yellow")
    t.goto(-115,-110)
    t.seth(0)
    t.color("red")
    t.forward(30)
    draw_eye_frame("red","white",-130,-90,50,10,5)
    t.seth(0)
    t.right(90)
    draw_circle(-170,-75,15,180,"black","black")
    #t.seth(0)
    #t.left(180)
    #t.forward(30)
    draw_eye_frame("red","white",-10,-90,50,10,5)
    t.seth(0)
    t.right(90)
    draw_circle(-65,-75,15,180,"black","black")

    draw_circle(100,-200,100,360,"red","yellow")
    draw_mouth(95,-140,"t",25)
    draw_eye_frame("red","white",75,-90,50,20,5)
    t.seth(0)
    t.right(90)
    draw_circle(35, -80, 10, 360, "black", "black")
    draw_eye_frame("red","white",155,-90,50,20,5)
    t.seth(0)
    t.right(90)
    draw_circle(115, -80, 10, 360, "black", "black")

    t.mainloop()


if __name__ == "__main__":
    main()

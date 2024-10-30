import turtle as t


def draw_backgroud(blocalx,blocaly,x,y):
    t.speed(0)
    t.up()
    t.goto(blocalx, blocaly)
    t.color("red")
    t.begin_fill()
    t.forward(x)
    t.right(90)
    t.forward(y)
    t.right(90)
    t.forward(x)
    t.right(90)
    t.forward(y)
    t.end_fill()
    t.up()
    t.home()
    t.goto(blocalx, blocaly)


def draw_star(localx,localy,len,angle):
    t.up()
    t.goto(localx,localy)
    t.left(angle)


    t.down()
    t.begin_fill()
    t.color("yellow")
    i = 1
    while i <= 5:
        t.forward(len)
        t.right(180 - 36)
        i += 1
    t.end_fill()
    t.up()
    t.home()


def draw_flag(t,x,y,lenth):
    t.speed(0)

    t.hideturtle()
    weith = lenth/1.5
    draw_backgroud(x,y,lenth,weith)

    draw_star(x+lenth/15,y-weith/5,192.036/960*lenth,0)
    draw_star(x+lenth*0.31,y-weith*0.115,64.004/960*lenth,30.6+18)
    draw_star(x+lenth*0.377,y-weith*0.21,64.004/960*lenth,8.13+18)
    draw_star(x+lenth*0.367,y-weith*0.34,64.004/960*lenth,0)
    draw_star(x+lenth*0.31,y-weith*0.42,64.004/960*lenth,378-38.66)


def main():
    draw_flag(t,0,0,480)
    t.mainloop()

if __name__ == "__main__":
    main()
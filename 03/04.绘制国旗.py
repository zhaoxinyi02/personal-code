import turtle as t



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


def main():

    t.speed(10)
    t.up()
    t.goto(-480, 320)
    t.color("red")
    t.begin_fill()
    t.forward(960)
    t.right(90)
    t.forward(640)
    t.right(90)
    t.forward(960)
    t.right(90)
    t.forward(640)
    t.end_fill()
    t.up()
    t.home()

    draw_star(-390,192,192.036,0)
    draw_star(-182.4,246.4,64.004,30.6+18)
    draw_star(-118.4,185.6,64.004,8.13+18)
    draw_star(-128,102.4,64.004,0)
    draw_star(-182.4,51.2,64.004,378-38.66)

    t.mainloop()

if __name__ == "__main__":
    main()




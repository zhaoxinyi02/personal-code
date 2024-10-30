import turtle as t

t.speed(10)
t.up()
t.goto(-480,320)
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

def draw_star(localx,localy,len,angle):
    t.up()
    t.goto(localx,localy)
    t.left(angle)
    t.forward(1.3759*len)
    t.right(180-18)

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

draw_star(-320,160,73.344,180-15.94)
draw_star(-160,256,24.448,180-30.96)
draw_star(-96,192,24.448,180+8.13)
draw_star(-96,96,24.448,180-15.94)
draw_star(-160,32,24.448,180-51.34)

t.mainloop()
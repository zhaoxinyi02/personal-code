import turtle as t

name = input("请输入你的名字")
class_name = input("请输入你的社团名字")
QQ = input("请输入你的QQ")
slogan = input("请输入你的slogan")

def draw_background():
    t.color("black")
    t.width(2)
    t.hideturtle()
    t.speed(0)
    t.up()
    t.goto(-240,160)
    t.down()
    t.begin_fill()
    t.forward(480)
    t.right(90)
    t.forward(320)
    t.right(90)
    t.forward(480)
    t.right(90)
    t.forward(320)
    t.color("yellow")
    t.end_fill()
    t.up()
def write(x,y,literal,size):
    t.goto(x,y)
    t.color("black")
    t.write(literal, align="left", font=("微软雅黑", size, "normal"))



#t.goto(-220,115)
#t.write("长江大学 " + class_name, align="left",font=("微软雅黑",24,"normal"))
#t.goto(-190,30)
#t.write("姓名：" + name, align="left",font=("微软雅黑",20,"normal"))
#t.goto(0,30)
#t.write("24组小组长", align="left",font=("微软雅黑",15,"normal"))
#t.goto(-190,-5)
#t.write("Q Q：" + QQ, align="left",font=("微软雅黑",20,"normal"))
#t.goto(-190,-40)
#t.write("slogan：" + slogan, align="left",font=("微软雅黑",20,"normal"))

def main():
    draw_background()
    write(-220,115,"长江大学 " + class_name,24)
    write(-190,30,"姓名：" + name,20)
    write(0,30,"24组小组长",15)
    write(-190,-5,"Q Q：" + QQ,20)
    write(-190,-40,"slogan：" + slogan,20)

    t.mainloop()


if __name__ == "__main__":
    main()
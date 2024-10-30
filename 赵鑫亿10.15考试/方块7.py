import turtle as t

t.hideturtle()
t.speed(0)
x_list = [-166.8,-166.8,-166.8,-45,83.4,83.4,83.4]
y_list = [211.67,0,-211.67,105.8,211.67,0,-211.67]
x_list2 = [-217.2,175.43]
y_list2 = [210,-210]


def draw_background():
    t.color("#d8d6d4")
    t.up()
    t.begin_fill()
    t.goto(-225,317.5)
    t.forward(450)
    t.right(90)
    t.forward(635)
    t.right(90)
    t.forward(450)
    t.right(90)
    t.forward(635)
    t.end_fill()

def write_literal(x,y,size):
    t.up()
    t.color("red")
    t.goto(x,y)
    t.write("7", align="left", font=("微软雅黑", size, "normal"))


def draw_diamond(x,y,lenth):
    t.up()
    t.seth(0)
    t.goto(x,y)
    t.color("red")
    t.begin_fill()
    t.left(56.3)
    t.forward(lenth)
    t.right(112.6)
    t.forward(lenth)
    t.right(67.4)
    t.forward(lenth)
    t.right(112.6)
    t.forward(lenth)
    t.end_fill()





def main():
    draw_background()
    for i in range(0,len(x_list)):
        draw_diamond(x_list[i],y_list[i],75.18)

    for i in range(0,len(x_list2)):
        draw_diamond(x_list2[i],y_list2[i],37.59)

    write_literal(-210, 240, 40)
    write_literal(185, -316.5, 40)

    t.mainloop()

if __name__ == "__main__":
    main()

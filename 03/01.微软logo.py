import turtle as t


def draw_square(color):
    t.color(color)
    t.begin_fill()
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.end_fill()

def main():
    t.speed(50)
    t.up()
    t.forward(2)
    t.left(90)
    t.forward(2)
    t.right(90)
    draw_square("#80bb00")
    t.right(90)
    t.forward(104)
    t.left(180)
    draw_square("#f25022")
    t.forward(104)
    t.left(90)
    draw_square("#01a4ef")
    t.left(90)
    t.forward(104)
    draw_square("#ffb901")

    t.forward(60)
    t.right(90)
    t.forward(120)
    t.color("#777777")
    t.write("MicroSoft",align="left",font=("Segoe",40,"normal"))

    t.mainloop()




if __name__ == "__main__":
    main()

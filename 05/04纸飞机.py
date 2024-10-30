import turtle as t

t.width(3)
t.speed(0)

def draw_line(b_localx,b_localy,a_localx,a_localy):
    t.up()
    t.goto(b_localx,b_localy)
    t.down()
    t.goto(a_localx,a_localy)

def draw_frame(line_color,fill_color,localx1,localy1,localx2,localy2,localx3,localy3):
    t.color(line_color)
    t.begin_fill()
    draw_line(localx1,localy1,localx2,localy2)
    draw_line(localx2,localy2,localx3,localy3)
    draw_line(localx3,localy3,localx1,localy1)
    t.color(fill_color)
    t.end_fill()

def main():
    draw_frame("black","blue",-300,150,-125,-125,-50,-50)
    draw_frame("black","blue",-50,-50,-30,-125,-85,-85)
    draw_frame("black","blue",-300,150,100,50,0,0)
    t.color("black")
    draw_line(0,0,-30,-125)
    draw_line(-80,-125,120,-200)
    draw_line(10,-80,100,-150)
    draw_line(50,-5,250,-30)
    draw_line(75,25,200,0)

    t.mainloop()




if __name__ == "__main__":
    main()

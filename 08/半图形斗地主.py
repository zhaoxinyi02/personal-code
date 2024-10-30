import turtle as t

from PyQt5.QtCore import center
from openpyxl.styles.builtins import normal
from pygame.draw_py import draw_line

from fapai import *

def draw_pai(x,y,lenth,width,pai):
    t.seth(0)
    t.hideturtle()
    t.speed(0)
    t.up()
    t.color('black')
    t.goto(x,y)
    t.down()
    t.forward(width)
    t.right(90)
    t.forward(lenth)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(lenth)
    t.up()
    t.goto(x+width/2,y-lenth/2)
    t.write(pai,align='center',font=('微软雅黑',10,'normal'))

def huapaizu(localx,localy,list,jiange):
    x = localx
    y = localy
    for i in range(len(list)):
        word = list[i]
        draw_pai(x,y,70,50,word)
        x+=50+jiange


def main():
    paiku = create_paiku()
    dizhu = []
    nongming1 = []
    nongming2 = []
    send_pai(paiku,dizhu,20)
    send_pai(paiku,nongming1, 17)
    send_pai(paiku,nongming2, 17)
    #print(dizhu)
    #print(nongming1)
    #print(nongming2)
    huapaizu(-500,400,dizhu,2)
    huapaizu(-500,300,nongming1,2)
    huapaizu(-500, 200, nongming2, 2)
    t.mainloop()


if __name__ == "__main__":
    main()
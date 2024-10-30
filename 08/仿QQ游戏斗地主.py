import turtle as t

from PyQt5.QtCore import center
from openpyxl.styles.builtins import normal
from pygame.draw_py import draw_line

from fapai import *

def draw_pai(x,y,lenth,width,pai):
    t.seth(0)
    t.width(2)
    t.hideturtle()
    t.speed(0)
    t.up()
    t.color('#a3a3a3')
    t.begin_fill()
    t.goto(x,y)
    t.down()
    t.forward(width)
    t.circle(-10,90)
    t.forward(lenth)
    t.circle(-10,90)
    t.forward(width)
    t.circle(-10,90)
    t.forward(lenth)
    t.circle(-10, 90)
    t.color('white')
    t.end_fill()
    t.up()

    if pai[0:2] == '方块' or pai[0:2] == '红心' or pai[0:2] == '大王':
        t.color('red')
    elif pai[0:2] == '梅花' or pai[0:2] == '黑桃' or pai[0:2] == '小王':
        t.color('black')
    t.goto(x + 10, y - 40)
    if pai == '大王' or pai == '小王':
        t.write('J', align='center', font=('微软雅黑', 20, 'normal'))
        t.seth(-90)
        t.forward(25)
        t.write('O', align='center', font=('微软雅黑', 20, 'normal'))
        t.seth(-90)
        t.forward(25)
        t.write('K', align='center', font=('微软雅黑', 20, 'normal'))
        t.seth(-90)
        t.forward(25)
        t.write('E', align='center', font=('微软雅黑', 20, 'normal'))
        t.seth(-90)
        t.forward(25)
        t.write('R', align='center', font=('微软雅黑', 20, 'normal'))
    else:
        t.write(pai[2:],align='center',font=('微软雅黑',20,'normal'))
        t.seth(-90)
        t.forward(25)
        if pai[0:2] == '梅花':
            t.write('\u2663', align='center', font=('微软雅黑', 20, 'normal'))
        if pai[0:2] == '黑桃':
            t.write('\u2660', align='center', font=('微软雅黑', 20, 'normal'))
        if pai[0:2] == '红心':
            t.write('\u2665', align='center', font=('微软雅黑', 20, 'normal'))
        if pai[0:2] == '方块':
            t.write('\u2666', align='center', font=('微软雅黑', 20, 'normal'))


def huapaizu(localx,localy,list,jiange):
    x = localx
    y = localy
    for i in range(len(list)):
        word = list[i]
        draw_pai(x,y,140,100,word)
        x+=jiange


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
    huapaizu(-500,400,dizhu,33)
    huapaizu(-500,200,nongming1,33)
    huapaizu(-500, 0, nongming2, 33)
    t.mainloop()


if __name__ == "__main__":
    main()
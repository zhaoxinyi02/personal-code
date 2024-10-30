from random import choice
import turtle as t
from fapai import *

paiku = ['黑桃3', '红心3', '方块3', '梅花3','黑桃4', '红心4', '方块4', '梅花4','黑桃5', '红心5', '方块5', '梅花5','黑桃6',
          '红心6', '方块6', '梅花6','黑桃7', '红心7', '方块7', '梅花7','黑桃8', '红心8', '方块8', '梅花8','黑桃9', '红心9',
          '方块9', '梅花9','黑桃10', '红心10', '方块10', '梅花10','黑桃J', '红心J', '方块J', '梅花J','黑桃Q', '红心Q',
          '方块Q', '梅花Q','黑桃K', '红心K', '方块K', '梅花K','黑桃A', '红心A', '方块A', '梅花A','黑桃2', '红心2', '方块2',
          '梅花2','大王', '小王']
paiku_num = []
for i in range(0,54):
    paiku_num.append(i)
dizhu_num = []
nongming1_num = []
nongming2_num = []
for i in range(20):
    j = choice(paiku_num)
    dizhu_num.append(j)
    paiku_num.remove(j)

for i in range(17):
    j = choice(paiku_num)
    nongming1_num.append(j)
    paiku_num.remove(j)

for i in range(17):
    j = choice(paiku_num)
    nongming2_num.append(j)
    paiku_num.remove(j)

dizhu = []
nongming1 = []
nongming2 = []
dizhu_num.sort(reverse=True)
nongming2_num.sort(reverse=True)
nongming1_num.sort(reverse=True)
for i in dizhu_num:
    dizhu.append(paiku[i])

for i in nongming1_num:
    nongming1.append(paiku[i])

for i in nongming2_num:
    nongming2.append(paiku[i])


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
            t.forward(110)
            t.left(90)
            t.forward(65)
            t.write('\u2663', align='center', font=('微软雅黑', 80, 'normal'))
        if pai[0:2] == '黑桃':
            t.write('\u2660', align='center', font=('微软雅黑', 20, 'normal'))
            t.forward(110)
            t.left(90)
            t.forward(65)
            t.write('\u2660', align='center', font=('微软雅黑', 80, 'normal'))
        if pai[0:2] == '红心':
            t.write('\u2665', align='center', font=('微软雅黑', 20, 'normal'))
            t.forward(110)
            t.left(90)
            t.forward(65)
            t.write('\u2665', align='center', font=('微软雅黑', 80, 'normal'))
        if pai[0:2] == '方块':
            t.write('\u2666', align='center', font=('微软雅黑', 20, 'normal'))
            t.forward(110)
            t.left(90)
            t.forward(65)
            t.write('\u2666', align='center', font=('微软雅黑', 80, 'normal'))


def huapaizu(localx,localy,list,jiange):
    x = localx
    y = localy
    for i in range(len(list)):
        word = list[i]
        draw_pai(x,y,140,100,word)
        x+=jiange

def main():

    huapaizu(-500,400,dizhu,33)
    huapaizu(-500,200,nongming1,33)
    huapaizu(-500, 0, nongming2, 33)
    t.mainloop()


if __name__ == "__main__":
    main()
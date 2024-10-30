from flag import draw_flag
import turtle as t
import time
from playsound import playsound
import threading

def flag_rise():
    t.delay(0)          #画旗台
    t.hideturtle()
    pen1 = t.Turtle()
    pen1.up()
    pen1.begin_fill()
    pen1.speed(10)
    pen1.color("black")
    pen1.width(5)
    pen1.goto(-240,-200)
    pen1.forward(240)
    pen1.right(60)
    pen1.forward(120)
    pen1.right(120)
    pen1.forward(360)
    pen1.right(120)
    pen1.forward(120)
    pen1.right(60)
    pen1.end_fill()
    pen1.forward(120)
    pen1.left(90)
    pen1.down()
    pen1.forward(640)
    pen1.up()
    pen1.home()


    pen2 = t.Turtle()
    for high in range(-120,445):       #画国旗，每画一个清除前一个

        draw_flag(pen2,-120,high,120)
        time.sleep(0.0608)
        t.clear()

    draw_flag(pen2,-120,445,120)
    t.mainloop()



def sing():
    playsound("国歌.mp3")



threads = []     #定义一个线程池
t1 = threading.Thread(target=flag_rise)
t2 = threading.Thread(target=sing)

threads.append(t1)
threads.append(t2)

if __name__ == "__main__":
    for th in threads:
        th.start()
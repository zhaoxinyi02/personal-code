import turtle as t



while True:
    t.color("red")
    t.up()
    t.goto(0, 300)
    t.write("心跳的感觉", align="center", font=("Segoe", 70, "normal"))

    t.home()
    t.speed(5)
    t.up()
    t.width(10)
    t.goto(-510, 0)

    i=1
    while i<=3:

        t.down()
        t.forward(120)

        t.left(72)
        t.forward(100)
        t.right(180-36)
        t.forward(100)
        t.left(72)

        t.forward(60)

        t.left(72)
        t.forward(200)
        t.right(180-36)
        t.forward(200)

        t.left(144)
        t.forward(100)
        t.right(180-36)
        t.forward(100)
        t.left(72)

        i+=1
    t.up()
    t.clear()
    t.speed(100)

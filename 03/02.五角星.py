import turtle as t

t.up()
t.goto(-250,0)
t.down()
t.begin_fill()
t.color("red")
i = 1
while i <= 5:
    t.forward(500)
    t.right(180-36)
    i += 1
t.end_fill()

t.mainloop()
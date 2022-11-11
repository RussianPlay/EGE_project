import turtle as t
t.color("black", "red")
t.left(90)
m = 58
t.begin_fill()
for i in range(4):
    t.forward(9 * m)
    t.right(90)
t.end_fill()
t.color("black", "purple")
t.begin_fill()
for i in range(3):
    t.forward(9 * m)
    t.right(120)
t.end_fill()

t.up()
t.speed(10)
for y in range(-5 * m, 15 * m, m):
    for x in range(-7 * m, 15 * m, m):
        t.goto(x, y)
        t.dot(2, "yellow")

t.done()
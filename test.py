import turtle as t

t.color("red")
m = 40
t.begin_fill()
t.left(90)
while True:
    t.forward(5 * m)
    t.right(90)
    t.forward(7 * m)
    t.right(90)
    cur_pos = round(t.xcor()), round(t.ycor())
    if cur_pos == (0, 0):
        break
t.end_fill()

t.up()
t.speed(10)
canvas = t.getcanvas()

k = 0
for y in range(-10 * m, 10 * m, m):
    for x in range(-10 * m, 10 * m, m):
        item = canvas.find_overlapping(x, y, x + 1, y + 1)
        if len(item) and item[0] == 5:
            print(item)
            # t.goto(x, y)
            # t.dot(3, "black")
            k += 1
print(k)
t.hideturtle()
t.done()


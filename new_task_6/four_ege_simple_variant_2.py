import turtle as t

t.color("red")
m = 80
t.begin_fill()
t.left(90)
while True:
    print(round(t.xcor(), 2), round(t.ycor(), 2))
    t.left(36)
    t.forward(4 * m)
    t.left(36)
    cur_pos = round(t.xcor(), 2), round(t.ycor(), 2)
    if cur_pos == (0.00, 0.00):
        break
t.end_fill()
# t.up()
# t.speed(10)
canvas = t.getcanvas()
k = 0
for y in range(-10 * m, 10 * m, m):
    for x in range(-10 * m, 10 * m, m):
        # t.goto(x, y)
        # t.dot(2)
        item = canvas.find_overlapping(x, y, x, y)
        if (x, y) == (0, 0):
            print(item)
        if len(item) and item[0] == 5:
            k += 1
print(k)
t.hideturtle()
t.done()


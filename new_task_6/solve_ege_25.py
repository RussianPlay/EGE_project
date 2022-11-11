import turtle as t

t.color("red")
t.left(90)
m = 30
t.begin_fill()
while True:
    t.forward(10 * m)
    t.right(60)
    cur_pos = (round(t.xcor()), round(t.ycor()))
    if cur_pos == (0, 0):
        break
t.end_fill()
# t.up()
# t.speed(10)
k = 0
canvas = t.getcanvas()
for y in range(-7 * m, 17 * m, m):
    for x in range(-2 * m, 20 * m, m):
        item = canvas.find_overlapping(x, y, x + 1, y + 1)
        # t.goto(x, y)
        # t.dot(3, "black")
        if len(item) and item[0] == 5:
            k += 1

print(k)
t.done()
import turtle as t

t.color("black", "red")
t.left(90)
m = 50
t.begin_fill()
while True:
    t.right(60)
    t.forward(1 * m)
    t.right(60)
    t.forward(1 * m)
    t.right(270)
    cur_pos = (round(t.xcor()), round(t.ycor()))
    if cur_pos == (0, 0):
        break
t.end_fill()
# t.up()
# t.speed(10)
k = 0
canvas = t.getcanvas()
for y in range(-100 * m, 100 * m, m):
    for x in range(-100 * m, 100 * m, m):
        item = canvas.find_overlapping(x, y, x, y)
        # t.goto(x, y)
        # t.dot(3, "black")
        if len(item) == 1 and item[0] == 5:
            k += 1

print(k)
t.done()
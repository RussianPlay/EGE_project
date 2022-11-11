import turtle as t

t.color("black", "red")
t.left(90)
m = 40
t.begin_fill()
while True:
    t.forward(12 * m)
    t.right(150)
    t.forward(12 * m)
    t.right(30)
    cur_pos = (round(t.xcor()), round(t.ycor()))
    if cur_pos == (0, 0):
        break
t.end_fill()
# t.up()
# t.speed(10)
k = 0
canvas = t.getcanvas()
for y in range(-13 * m, 15 * m, m):
    for x in range(-2 * m, 10 * m, m):
        item = canvas.find_overlapping(x, y, x, y)
        # t.goto(x, y)
        # t.dot(3, "black")
        if len(item) == 1 and item[0] == 5:
            k += 1
print(k)
t.done()
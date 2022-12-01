import turtle as t

t.color("black", "red")
m = 10
t.left(90)
t.begin_fill()
for i in range(4):
    for j in range(4):
        t.forward(40 * m)
        t.right(90)
    t.left(90)
t.end_fill()
# t.penup()
# for y in range(0, 44 * m, m):
#     for x in range(0, 44 * m, m):
#         t.goto(x, y)
#         t.dot(2, "red")
k = 0
canvas = t.getcanvas()
for y in range(0, 44 * m, m):
    for x in range(0, 44 * m, m):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            k += 1
print(k)
t.done()
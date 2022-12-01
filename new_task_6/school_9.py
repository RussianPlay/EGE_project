import turtle as t

m = 2
for i in range(11):
    t.goto(t.xcor() + 2 * m, t.ycor() + 7 * m)
    t.goto(t.xcor() - 4 * m, t.ycor() - 8 * m)
    t.goto(t.xcor() + 56 * m, t.ycor() - 24 * m)

# t.penup()
# for y in range(-10 * m, 10 * m, m):
#     for x in range(-10 * m, 10 * m, m):
#         t.goto(x, y)
#         t.dot(2, "purple")

k = 0
canvas = t.getcanvas()
for y in range(-1000 * m, 1000 * m, m):
    for x in range(-1000 * m, 1000 * m, m):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item):
            k += 1
print(k)
t.done()
import turtle as t

t.left(90)
for i in range(11):
    t.forward(36)
    t.right(72)
cur_x, cur_y = round(t.xcor(), 5), round(t.ycor(), 5)
print(cur_x, cur_y)
cur_length = ((cur_x - 0) ** 2 + (cur_y - 0) ** 2) ** 0.5
print(cur_length)
t.done()
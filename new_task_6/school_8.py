import turtle as t
m = 10
for i in range(10):
    t.goto(t.xcor() + 15 * m, t.ycor() + 8 * m)
    t.goto(t.xcor(), t.ycor() - 1 * m)
    t.goto(t.xcor() - 2 * m, t.ycor())
    t.goto(t.xcor() - 5 * m, t.ycor() - 12 * m)
    t.goto(t.xcor() - 8 * m, t.ycor() + 6 * m)
print(t.xcor(), t.ycor())
length_line_1 = (15 ** 2 + 8 ** 2) ** 0.5
length_line_2 = 1
length_line_3 = 2
length_line_4 = (5 ** 2 + 12 ** 2) ** 0.5
length_line_5 = (8 ** 2 + 6 ** 2) ** 0.5
print((length_line_1 + length_line_2 + length_line_3 + length_line_4 + length_line_5) * 10)
t.done()
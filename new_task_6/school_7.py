import turtle as t

for i in range(10):
    t.goto(t.xcor() + 3, t.ycor() - 4)
    t.goto(t.xcor() - 7, t.ycor() + 24)
    t.goto(t.xcor() + 12, t.ycor() + 5)
print(t.xcor(), t.ycor())
length_line_1 = (3 ** 2 + 4 ** 2) ** 0.5
length_line_2 = (7 ** 2 + 24 ** 2) ** 0.5
length_line_3 = (12 ** 2 + 5 ** 2) ** 0.5
print((length_line_1 + length_line_2 + length_line_3) * 10)
t.done()
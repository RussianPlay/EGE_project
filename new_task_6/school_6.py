import turtle as t

t.left(90)
for i in range(8):
    t.goto(t.xcor() + 30, t.ycor() - 20)
    t.goto(t.xcor() + 50, t.ycor() + 30)
    t.goto(t.xcor() - 40, t.ycor() + 60)
end_x, end_y = t.xcor(), t.ycor()
print((end_x ** 2 + end_y ** 2) ** 0.5)
t.done()
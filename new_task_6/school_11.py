import turtle as t

m = 5
x_coords_center_circle_1 = set()
x_coords_center_circle_2 = set()
x_coords_center_circle_3 = set()
t.speed(1000)
for i in range(20):
    t.circle(4 * m)
    x_coords_center_circle_1.add(round(t.xcor()))
    t.penup()
    t.goto(t.xcor() + 8 * m, t.ycor())
    t.pendown()
t.penup()
t.goto(t.xcor(), t.ycor() - 12 * m)
t.pendown()
for i in range(10):
    t.circle(8 * m)
    x_coords_center_circle_2.add(round(t.xcor()))
    t.penup()
    t.goto(t.xcor() - 16 * m, t.ycor())
    t.pendown()
t.penup()
t.goto(t.xcor(), t.ycor() - 14 * m)
t.pendown()
for i in range(15):
    t.circle(6 * m)
    x_coords_center_circle_3.add(round(t.xcor()))
    t.penup()
    t.goto(t.xcor() + 12 * m, t.ycor())
    t.pendown()
intercepted_x_coords_center_circles = x_coords_center_circle_1 & x_coords_center_circle_2 & x_coords_center_circle_3
print(intercepted_x_coords_center_circles)
print(len(intercepted_x_coords_center_circles))
t.done()
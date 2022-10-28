from turtle import *
import math

color("black", "red")
m = 100
begin_fill()
left(90)
while True:
    left(36)
    forward(4 * m)
    left(36)
    cur_pos = round(xcor(), 2), round(ycor(), 2)
    print(cur_pos)
    if cur_pos == (0.00, 0.00):
        break
end_fill()

canvas = getcanvas()
k = 0
for y in range(-1000 * m, 1000 * m, m):
    for x in range(-1000 * m, 1000 * m, m):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            k += 1

print(k)
done()
exit()

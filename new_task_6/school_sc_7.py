import turtle as t

m = 5

t.speed(100)
for i in range(13):
    t.forward(10 * m)
    t.right(90)
    t.forward(4 * m)
    for j in range(3):
        t.right(90)
        t.forward(3 * m)
t.forward(100)
t.done()
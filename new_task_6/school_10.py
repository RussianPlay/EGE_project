import turtle as t

for i in range(5):
    t.goto(t.xcor() - 2, t.ycor() + 6)
    t.goto(t.xcor() + 5, t.ycor() - 1)
for i in range(3):
    t.goto(t.xcor() + 3, t.ycor() - 1)
    t.goto(t.xcor() + 4, t.ycor() + 1)
    t.goto(t.xcor() + 5, t.ycor() + 3)
end_x, end_y = t.xcor(), t.ycor()


def get_num_divisors(n):
    divs = [1, n]
    k = 2
    while k * k <= n:
        if n % k == 0:
            divs.append(k)
            k_ch = n // k
            if k_ch != k:
                divs.append(k_ch)
        k += 1
    return divs


intercepted_divs = set(get_num_divisors(end_x)) & set(get_num_divisors(end_y))
length_total_line = (end_x ** 2 + end_y ** 2) ** 0.5
print(max(map(lambda divisor: length_total_line // divisor, intercepted_divs)))
t.done()
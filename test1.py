for x in range(699, 0, -1):
    a = 4 * x + 21
    b = 6 * x - 54
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    if a == 19:
        print(x)
        break

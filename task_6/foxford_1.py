for i in range(-10000, 1000):
    s = i
    n = 1
    while s < 31:
        s = s + 3
        n = n * 2
    if n == 128:
        print(i)
        break

for i in range(1341000000, 100000000000000000):
    s = i
    s = s // 5
    n = 0
    k = 1
    while s > k:
        s -= k
        k *= 2
        n += 1
    if n == 28:
        print(i)
        break
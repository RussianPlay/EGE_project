def finding():
    lst = []
    for i in range(1000000):
        s = i
        n = 1
        while s < 208:
            s = s + 20
            n = n * 2
        if n == 256:
            lst.append(i)
    return max(lst)


print(finding())
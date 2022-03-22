k = 0


def F(n):
    global k
    k += 1
    if n >= 1:
        k += 1
        F(n-1)
        F(n-2)
        k += 1


F(35)
print(k)

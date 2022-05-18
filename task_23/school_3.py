def calc(n):
    global k
    if n < 344:
        return calc(n + 1) or calc(int(str(n) + "1"))
    elif n == 344:
        k += 1


k = 0
calc(1)
print(k)

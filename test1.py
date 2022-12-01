def Del(n, m):
    return n % m == 0


for A in range(1, 1000):
    for x in range(1, 1000):
        if Del(x, A) <= (not(Del(x, 14)) or Del(x, 84)) == False:
            print(123)  # Сюда что-то надо
        else:
            print(A)
            break
print("x y z F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = (not x or not z) <= (x == y)
            if int(F) == 0:
                print(x, y, z, int(F))
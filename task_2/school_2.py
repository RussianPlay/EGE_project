print("x y z F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = (x and not z) or (x and y and z)
            if int(F) == 1:
                print(x, y, z, int(F))
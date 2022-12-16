print("w x y z F")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                F = (x <= (y == w)) and (y == (w <= z))
                print(w, x, y, z, int(F))
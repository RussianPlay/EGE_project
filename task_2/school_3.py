print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (w == (x or z)) <= (z == (y and w))
                if int(f) == 0:
                    print(x, y, z, w, int(f))

print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((y <= x) or (not z and w)) == (w == x)
                if int(F) == 1:
                    print(x, y, z, w, int(F))

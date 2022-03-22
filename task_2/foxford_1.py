print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = x and (not y and z and not w or y and not z)
                if int(F) == 1:
                    print(x, y, z, w, int(F))

print("x y z w F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = x and (z and not w or y and not w or y and not z)
                if int(f) == 1:
                    print(x, y, z, w, int(f))

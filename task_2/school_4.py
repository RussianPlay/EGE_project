print("w x y z F")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = ((x <= y) and (z or w)) <= ((x == w) or (y and not z))
                if int(f) == 0:
                    print(w, x, y, z, int(f))
                    
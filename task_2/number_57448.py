print("x y z F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = ((not x) and y and z) or ((not x) and (not y) and z) or ((not x) and (not y) and (not z))
            if int(F) == 1:
                print(x, y, z, int(F))
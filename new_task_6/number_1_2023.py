k = 0
for y in range(4):
    for x in range(4):
        if ((y / 2.6) < (x / 1.5)) and ((y / 2.6) < ((x - 3) / -1.5)):
            k += 1
print(k)
N = 0
R = 0
while R <= 125:
    N += 1
    bN = bin(N)[2:]
    bN = bN + str(sum(map(int, bN)) % 2)
    bN = bN + str(sum(map(int, bN)) % 2)
    R = int(bN, 2)
print(N)


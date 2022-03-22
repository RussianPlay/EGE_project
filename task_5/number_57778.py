N = -1
R = 0
while R <= 90:
    N += 1
    R = bin(N)[2:]
    amount = sum(map(int, list(R)))
    R = R + str(amount % 2)
    amount = sum(map(int, list(R)))
    R = R + str(amount % 2)
    R = int(R, 2)
print(R)
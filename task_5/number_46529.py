N = 0
R = 0
while R <= 150:
    N += 1
    R = list(bin(N)[2:])
    amount = sum(map(int, R))
    R = R + [str(amount % 2)]
    amount = sum(map(int, R))
    R = R + [str(amount % 2)]
    R = int("".join(R), 2)
print(R)
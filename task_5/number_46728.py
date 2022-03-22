N = 2
R = 0
while R <= 99 or N % 2 == 0:
    R = bin(N)[2:]
    R = int(R[0] + "".join(list(map(lambda x: "1" if x == "0" else "0", R[1:]))), 2)
    N += 1
print(N)
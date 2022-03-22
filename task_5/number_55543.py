N = 0
R = 0
while R != 171:
    N += 1
    if N == 256:
        print("Нет значений")
        break
    num_base_8 = ""
    num_base_10 = N
    while num_base_10 != 0:
        num_base_8 = num_base_8 + str(num_base_10 % 8)
        num_base_10 //= 8
    R = int(num_base_8[::-1], 8)

print(N)

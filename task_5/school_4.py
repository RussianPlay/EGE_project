N = 2
R = -1
while True:
    even_num_amount = sum(map(int, filter(lambda x: int(x) % 2 == 0, str(N))))
    N_non_beggining_zero = str(N)
    while N_non_beggining_zero and N_non_beggining_zero[0] == "0":
        N_non_beggining_zero = N_non_beggining_zero[1:]
    even_place_num_amount = sum(map(int, N_non_beggining_zero[::2]))
    R = abs(even_num_amount - int(even_place_num_amount))
    if R == 9:
        print(N)
        break
    N += 1

N = 1
R = 0
mx_cur_R = -1
while R < 90:
    N_base_2 = bin(N)[2:]
    while N_base_2[0] == "0":
        N_base_2 = N_base_2[1:]
    check_more_one = N_base_2.count("1") > N_base_2.count("0")
    if check_more_one:
        N_base_2 = N_base_2 + "1"
    else:
        N_base_2 = N_base_2 + "0"
    R = int(N_base_2, 2)
    if R < 90:
        mx_cur_R = max(mx_cur_R, R)
    N += 1
    print(N)
    print(R)
    print("------------------------")

print("max")
print(mx_cur_R)
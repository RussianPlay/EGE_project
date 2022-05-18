with open("17-9_number_27909.txt", "r") as file:
    numbers = list(map(lambda x: int(x.strip()), file.readlines()))

mx_num = -1
amount_triples = 0
for i in range(len(numbers) - 3):
    num1_b2 = bin(numbers[i])[2:]
    num2_b2 = bin(numbers[i + 1])[2:]
    num3_b2 = bin(numbers[i + 2])[2:]
    res_mx = -1
    ch_activation = False
    if num1_b2.count("1") >= 3 and num2_b2.count("1") >= 3 and num1_b2.count("0") >= 1 and num2_b2.count("0") >= 1:
        res_mx = max(res_mx, int(num1_b2, 2))
        res_mx = max(res_mx, int(num2_b2, 2))
        ch_activation = True

    if num1_b2.count("1") >= 3 and num3_b2.count("1") >= 3 and num1_b2.count("0") >= 1 and num3_b2.count("0") >= 1:
        res_mx = max(res_mx, int(num1_b2, 2))
        res_mx = max(res_mx, int(num3_b2, 2))
        ch_activation = True

    if num2_b2.count("1") >= 3 and num3_b2.count("1") >= 3 and num2_b2.count("0") >= 1 and num3_b2.count("0") >= 1:
        res_mx = max(res_mx, int(num2_b2, 2))
        res_mx = max(res_mx, int(num3_b2, 2))
        ch_activation = True

    if ch_activation:
        amount_triples += 1
    mx_num = max(mx_num, res_mx)

print(amount_triples)
print(mx_num)

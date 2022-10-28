with open("17_four_ege_simple_variant_2.txt", "r") as file:
    numbers = list(map(lambda x: int(x.strip()), file.readlines()))
k = 0
mx_cur_num = max(filter(lambda x: x % 11 == 0, numbers))
mx_pair_amount = -1

for i in range(0, len(numbers) - 1):
    if (numbers[i] % 11 == 0 or numbers[i + 1] % 11 == 0) and (numbers[i] + numbers[i + 1]) <= mx_cur_num:
        k += 1
        mx_pair_amount = max(mx_pair_amount, numbers[i] + numbers[i + 1])

print(k, mx_pair_amount)

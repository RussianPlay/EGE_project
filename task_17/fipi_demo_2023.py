with open("17_fipi_demo_2023.txt", "r") as file:
    data = list(map(lambda x: int(x.strip()), file.readlines()))
max_seq_value = max(filter(lambda x: str(x)[-1] == "3", data))
k = 0
mx_sum_squares_pairs = -1


for i in range(len(data) - 1):
    num_1 = data[i]
    num_2 = data[i + 1]
    sum_squares = (num_1 ** 2 + num_2 ** 2)
    if ((int(str(num_1)[-1] == "3") + int(str(num_2)[-1] == "3")) == 1) and sum_squares >= (max_seq_value ** 2):
        mx_sum_squares_pairs = max(mx_sum_squares_pairs, sum_squares)
        k += 1
print(k, mx_sum_squares_pairs)

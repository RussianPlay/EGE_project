with open("17_school_4.txt", "r") as file:
    numbers = list(map(lambda x: int(x.strip()), file.readlines()))

k = 0
mx_pair_num = 0
even_cur_nums = list(filter(lambda x: x % 2 == 0, numbers))
even_num_average = sum(even_cur_nums) / len(even_cur_nums)
for i in range(len(numbers) - 1):
    num_1 = numbers[i]
    num_2 = numbers[i + 1]
    if (num_1 % 3 == 0 or num_2 % 3 == 0) and (num_1 < even_num_average or num_2 < even_num_average):
        k += 1
        mx_pair_num = max(mx_pair_num, num_1 + num_2)

print(k, mx_pair_num)

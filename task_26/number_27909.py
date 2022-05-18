with open("26-j4_number_27909.txt", "r") as file:
    total = list(map(lambda x: int(x.strip()), file.readlines()))
    N = total[0]
    sizes = total[1:]

sizes.sort()
cutout_part_length = int(len(sizes) * 0.1)
cur_part = sizes[cutout_part_length:len(sizes) - cutout_part_length]
print(sum(cur_part), max(cur_part))
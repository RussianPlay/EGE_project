with open("26_fipi_demo_2023.txt", "r") as file:
    total = list(map(lambda x: int(x.strip()), file.readlines()))
    N = total[0]
    sizes = list(sorted(total[1:], reverse=True))


lst_cur_sizes = [sizes[0]]
ind = 0
while ind < len(sizes) - 1:
    if lst_cur_sizes[-1] - sizes[ind + 1] >= 3:
        lst_cur_sizes.append(sizes[ind + 1])
    ind += 1

print(len(lst_cur_sizes), lst_cur_sizes[-1])

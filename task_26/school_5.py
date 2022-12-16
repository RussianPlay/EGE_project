with open("26_school_5.txt", "r") as file:
    total = list(map(lambda x: int(x.strip()), file.readlines()))
    N = total[0]
    cont_sizes = list(reversed(sorted(total[1:])))

quantity_packed_cont_sizes = {}
num_cells = 0
while len(cont_sizes) != 0:
    mx_size = cont_sizes[0]
    num_cells += 1
    quantity_packed_cont_sizes[str(num_cells)] = 1
    while True:
        intercepted_values = list(set(range((mx_size - 5), -1, -1)) & set(cont_sizes))
        cont_sizes.remove(mx_size)
        if intercepted_values:
            mx_size = max(intercepted_values)
            quantity_packed_cont_sizes[str(num_cells)] += 1
        else:
            break
print(num_cells)
print(max(quantity_packed_cont_sizes.values()))

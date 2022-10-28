with open("22_fipi_demo_2023.txt", "r") as file:
    table = list(map(str.strip, file.readlines()))[1:]
    table = list(map(lambda x: x.split("\t"), table))
    table = list(map(lambda x: (x[0], (int(x[1]), list(str(x[2]).replace('"', '').split("; ")))), table))
    data = dict(table)


def total_time_summation(other_inds):
    if len(other_inds) == 1 and other_inds[0] != "0":
        return total_data[other_inds[0]]
    elif len(other_inds) > 1:
        return max(total_data[other_inds[0]], total_time_summation(other_inds[1:]))
    else:
        return 0


total_data = dict(list(map(lambda x: (x[0], x[1][0]), table)))
for key, value in data.items():
    total_data[key] = value[0] + total_time_summation(value[1])
print(total_data)




with open("number_1_2023.txt", "r") as file:
    total = list(map(str.strip, file.readlines()))
N = int(total[0])
rows_and_places = list(map(lambda x: x.split(), total[1:]))
data = dict(map(lambda x: (x, []), list(set(list(map(lambda x: str(x[0]), rows_and_places))))))
for row, place in rows_and_places:
    data[row].append(int(place))


def calc():
    for row_num, lst_places in sorted(data.items(), key=lambda x: int(x[0]), reverse=True):
        sorted_places = sorted(lst_places)
        for i in range(len(sorted_places) - 1):
            if sorted_places[i + 1] - sorted_places[i] == 3:
                return f"{row_num} {sorted_places[i] + 1}"


print(calc())

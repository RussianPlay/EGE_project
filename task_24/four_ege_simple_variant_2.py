with open("24_four_ege_simple_variant_2.txt", "r") as file:
    text = file.readline().strip()

# cur_length = 0
# mx_length = 0
text = text.replace("XYZ", "AA AA")
text = text.split()
lengths = list(map(lambda x: len(x), text))
print(max(lengths))
# for i in range(0, len(text) - 3):
#     if text[i: i + 3] != "XYZ":
#         cur_length += 1
#     else:
#         mx_length = max(mx_length, cur_length)
#         cur_length = 2
#
# print(mx_length)
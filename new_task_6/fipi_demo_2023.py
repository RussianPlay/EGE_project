k = 0
for y in range(11):
    for x in range(11):
        if (y > 0) and ((y / 8.66) < (x / 5)) and ((y / 8.66) < ((x - 10) / -5)):
            k += 1

print(k)

# Another solution
# k = 0
# for y in range(11):
#     for x in range(11):
#         checking_side_1 = (y / 8.66) < (x / 5)
#         checking_side_2 = (y / 8.66) < ((x - 10) / -5)
#         checking_side_3 = (y > 0)
#         if checking_side_1 and checking_side_2 and checking_side_3:
#             k += 1
# print(k)

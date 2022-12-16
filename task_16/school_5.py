# def F(n):
#     return n * (n + 1) // 2
# k = 0
# for n in range(237567892, 1134567004 + 1):
#     if F(n) % 3 != 0:
#         k += 1
#     print(n)
# print(k)


print(list(map(lambda x: x % 3, range(1134567004, 1134567004 + 20))))
print((1134567005 - 237567892) // 3 + 1)
k = 0


for i in range(10 ** 8 - 10 ** 8, 10 ** 9):
    if sum(map(int, list(str(i)))) == 75:
        k += 1
        print(k)

print("-----------")
print(k)

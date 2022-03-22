lst = []

for n in range(57888, 74556):
    if int(str(n)[0]) % 2 != 0 and int(str(n)[1]) % 2 != 0 and all(map(lambda x: int(x) % 2 == 0, str(n)[2:])) \
            and n % 7 != 0 and n % 9 != 0 and n % 13 != 0:
        lst.append(n)
cur_num = lst[0]
for num in lst[1:]:
    cur_num -= num

print(len(lst), (max(lst) - min(lst)))
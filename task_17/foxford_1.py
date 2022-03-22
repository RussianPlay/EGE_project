mx_num = 0
k = 0
for num in range(1033, 7737 + 1):
    if num % 5 == 0 and num % 11 != 0 and num % 17 != 0 and num % 19 != 0 and num % 23 != 0:
        k += 1
        mx_num = max(mx_num, num)

print(k, mx_num)

n = int(input())
lst = []
m = ms = 0

for i in range(7):
    lst.append(int(input()))

for i in range(n - 7):
    b = int(input())

    if lst[0] > m:
        m = lst[0]
    if m + b > ms:
        ms = m + b

    for i in range(6):
        print(lst)
        lst[i] = lst[i + 1]

    lst[6] = b
    print(lst)
print(ms)
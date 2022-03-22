num = 94
base = 1
new_num = ""
while str(new_num[:2]) != "23":
    res = num
    base += 1
    while res != 0:
        new_num += str(res % base)
        res //= base
    new_num = new_num[::-1]
    n = new_num[:2]
    h = n
print(base)
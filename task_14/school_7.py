lst = []
for x in range(8):
    for y in range(8):
        num1_base_8 = f"36{x}53"
        num2_base_8 = f"4{y}3"
        n = int(num1_base_8, 8) - int(num2_base_8, 8)
        if n >= 0:
            lst.append(n)
print(min(lst))


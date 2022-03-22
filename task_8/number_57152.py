w = "САКУРА"
k = 0
for i1 in range(5):
    for i2 in range(5):
        for i3 in range(5):
            for i4 in range(5):
                for i5 in range(5):
                    new_w = w[i1] + w[i2] + w[i3] + w[i4] + w[i5]
                    if list(new_w).count("А") <= 1 and list(new_w).count("У") <= 1:
                        k += 1
print(k)
with open("24_school_5.txt", "r") as file:
    text = file.readline().strip()
vowels = ["A", "O"]
cons = ["C", "D", "F"]
k = 0
mx_k = 0
for i in range(0, len(text), 3):
    if text[i] in cons and text[i + 1] in cons and text[i + 2] in vowels:
        k += 1
    else:
        mx_k = max(mx_k, k)
        k = 0
for i in range(1, len(text) - 1, 3):
    if text[i] in cons and text[i + 1] in cons and text[i + 2] in vowels:
        k += 1
    else:
        mx_k = max(mx_k, k)
        k = 0
for i in range(2, len(text) - 2, 3):
    if text[i] in cons and text[i + 1] in cons and text[i + 2] in vowels:
        k += 1
    else:
        mx_k = max(mx_k, k)
        k = 0
print(mx_k)
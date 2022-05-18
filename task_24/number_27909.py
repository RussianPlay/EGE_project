with open("24-3_number_27909.txt", "r") as file:
    text = list(map(str.strip, file.readlines()))[0]

seq = []
mx_seq = []
if ord(text[0]) > ord(text[1]):
    seq.append(0)
for i in range(len(text) - 1):
    if ord(text[i]) > ord(text[i + 1]):
        seq.append(i + 1)
    else:
        mx_seq = max(mx_seq, seq, key=len).copy()
        seq = []


if ord(text[1]) > ord(text[2]):
    seq.append(1)
for i in range(1, len(text) - 1):
    if ord(text[i]) > ord(text[i + 1]):
        seq.append(i + 1)
    else:
        mx_seq = max(mx_seq, seq, key=len).copy()
        seq = []

print(mx_seq[0])

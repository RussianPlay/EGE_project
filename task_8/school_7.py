import numpy as np

k = 0
n = np.arange(10 ** 8, 10 ** 9 + 1)
i = 0
for x in np.nditer(n):
    if (len(str(x)) - len(set(str(x)))) >= 3:
        k += 1
    i += 1
    print(i)
print(k)

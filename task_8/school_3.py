from itertools import product
import numpy as np
from numpy.core.defchararray import find

word = list("ВАЛЕРЬЯН")
vowels = "АЕЯ"
cur_word = list("ВЛРЬН")
k = 0
for l1 in "ВАЛЕРЯН":
    for l2 in word:
        for l3 in word:
            for l4 in word:
                for l5 in word:
                    for l6 in word:
                        for l7 in word:
                            for l8 in word:
                                for l9 in word:
                                    for l10 in word:
                                        k += 1
                                        print(k)

print(k)


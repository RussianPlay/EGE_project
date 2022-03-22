def calc():
    k = 1
    while True:
        numbers = "8" * (100 + k)
        while "555" in numbers or "888" in \
                numbers:
            numbers = numbers.replace("555",
                                      "8", 1)
            numbers = numbers.replace("888", "55", 1)
        if "5" not in numbers:
            return 100 + k
        k += 1
print(calc())
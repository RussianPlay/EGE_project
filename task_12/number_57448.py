num = "211"
def calculation():
    for i in range(31, 10000):
        num = "1" * i
        while "111" in num:
            num = num.replace("111", "2", 1)
            num = num.replace("222", "1", 1)
        if num == "211":
            return i
print(calculation())
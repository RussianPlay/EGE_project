numbers = ">" + "1" * 15 + "2" * 20 + "3" * 25
while ">1" in numbers or ">2" in numbers or ">3" in numbers:
    if ">1" in numbers:
        numbers = numbers.replace(">1", "22>", 1)
    if ">2" in numbers:
        numbers = numbers.replace(">2", "2>1", 1)
    if ">3" in numbers:
        numbers = numbers.replace(">3", "1>", 1)

print(sum(map(lambda x: int(x) if x != ">" else 0, numbers)))
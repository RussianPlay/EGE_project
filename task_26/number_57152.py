with open("26-4_number_57152.txt",
          "r") as file:
    text = list(map(str.strip, file.readlines()))
    S, N = map(int, text[0].split())
    numbers = list(map(int, text[1:]))
    maximum_file_size = []
    maximum_value = 0
    for num in sorted(numbers):
        if num <= S:
            S -= num
            maximum_file_size.append(num)
        if (S + max(maximum_file_size)) >= num:
            maximum_value = max(maximum_value,
                                num)
    print(len(maximum_file_size), maximum_value)
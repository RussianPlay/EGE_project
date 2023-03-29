for a in range(46):
    for b in range(46):
        for c in range(46):
            num = "0" + a * "1" + b * "2" + c * "3"
            while "01" in num or "02" in num or "03" in num:
                num = num.replace("01", "30", 1)
                num = num.replace("02", "3103", 1)
                num = num.replace("03", "1201", 1)
            if num.count("1") == 31 and num.count("2") == 24 and num.count("3") == 46:
                print(c)

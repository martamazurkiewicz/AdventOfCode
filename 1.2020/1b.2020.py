with open("report.txt", "r") as report:
    lines = report.readlines()
    numbers=[]
    for i in range(len(lines)):
        numbers.append(int(lines[i]))
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                if numbers[i]+numbers[j]+numbers[k] == 2020:
                    print(numbers[i])
                    print(numbers[j])
                    print(numbers[k])
                    print(f"{numbers[i]}*{numbers[j]}*{numbers[k]} = {numbers[j]*numbers[i]*numbers[k]}")
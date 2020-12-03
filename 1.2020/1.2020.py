with open("report.txt", "r") as report:
    lines = report.readlines()
    numbers=[]
    for i in range(len(lines)):
        numbers.append(int(lines[i]))
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i]+numbers[j] == 2020:
                print(numbers[i])
                print(numbers[j])
                print(f"{numbers[i]}*{numbers[j]} = {numbers[j]*numbers[i]}")


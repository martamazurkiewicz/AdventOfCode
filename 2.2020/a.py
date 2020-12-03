with open("policy.txt", "r") as file:
    valid_passwords = 0
    for row in file:
        line = row.rstrip().split()
        number_of_times = line[0].split('-')
        char = line[1][0]
        password = line[2]
        occurrence = password.count(char)
        if int(number_of_times[0]) <= occurrence <= int(number_of_times[1]):
            valid_passwords += 1

print(valid_passwords)


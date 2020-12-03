with open("policy.txt", "r") as file:
    valid_passwords = 0
    for row in file:
        line = row.rstrip().split()
        numbers = line[0].split('-')
        first_position = int(numbers[0])-1
        second_position = int(numbers[1])-1
        char = line[1][0]
        password = line[2]
        if password[first_position] == char and password[second_position] != char:
            valid_passwords += 1
        elif password[second_position] == char and password[first_position] != char:
            valid_passwords += 1

print(valid_passwords)
import re


def get_dictionary_from_input():
    file = open('input.txt', 'r')
    text = file.read().split('\n')
    dict = {}
    for line in text:
        if "no other bags" in line:
            dict[' '.join(line.split()[0:2])] = [0]
        else:
            line = re.split(',|contain', line)
            tmp = []
            for i in range(1, len(line)):
                line[i] = line[i].split()
                color = [line[i][1], line[i][2]]
                tmp.append((int(line[i][0]), ' '.join(color)))
            dict[' '.join(line[0].split()[0:2])] = tmp
    return dict


def get_number_of_bags_inside(bags_dict, color):
    number_of_bags = 1
    for bags in bags_dict[color]:
        if bags == 0:
            return 1
        else:
            number_of_bags += bags[0] * get_number_of_bags_inside(bags_dict, bags[1])
    return number_of_bags


bags_dict = get_dictionary_from_input()
print(get_number_of_bags_inside(bags_dict, 'shiny gold')-1)




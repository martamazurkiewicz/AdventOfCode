file = open('input.txt', 'r')
text = file.read().split('\n')
held_bags = ["shiny gold"]
tmp_held_bags = []
bags_containing_gold = []
added_bags = 1
while added_bags != 0:
    added_bags = 0
    for line in text:
        for held_bag in held_bags:
            if held_bag in line:
                tmp_held_bags.append(' '.join(line.split()[0:2]))
    tmp = []
    for tmp_held_bag in tmp_held_bags:
        if tmp_held_bag not in held_bags:
            added_bags += 1
            tmp.append(tmp_held_bag)
            bags_containing_gold.append(tmp_held_bag)
    held_bags = tmp
    tmp_held_bags = []

print(len(set(bags_containing_gold)))
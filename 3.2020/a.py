with open("route.txt", "r") as file:
    threes = 0
    row_number = 1
    position_in_row = 0
    for row in file:
        line = row.rstrip()
        if position_in_row > 30:
            position_in_row = position_in_row-31
        if line[position_in_row] == "#":
            threes += 1
        print(f"{row_number} {position_in_row} {line[position_in_row]}")
        position_in_row += 3
        row_number += 1

print(threes)

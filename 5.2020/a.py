def get_all_seats():
    with open("passes.txt", "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
        lines[i] = lines[i][0:7], lines[i][7:10]
    return lines


def get_seat_with_longest_B_chain(lines):
    lines.sort(key=lambda element: element[0])
    longest_B_chains = []
    for i in range(len(lines)):
        if lines[i][0] == lines[0][0]:
            longest_B_chains.append(lines[i])
        else:
            break
    longest_B_chains.sort(key=lambda element: element[1], reverse=True)
    return longest_B_chains[0]


def decode_seat(seat):
    number = []
    for i in range(len(seat)):
        low = 0
        high = 127 if i == 0 else 7
        letter = "F" if i == 0 else "L"
        for char in seat[i]:
            if char == letter:
                high = high - (high-low+1)/2
            else:
                low = low + (high-low+1)/2
        number.append(low)
    return number


def get_seat_id(row, col):
    return row*8+col

lines = get_all_seats()
seat_high = get_seat_with_longest_B_chain(lines)
print(seat_high)
seat_high = decode_seat(seat_high)
print(seat_high)
print(get_seat_id(seat_high[0], seat_high[1]))



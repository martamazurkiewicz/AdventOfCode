def get_all_seats():
    with open("passes.txt", "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
        lines[i] = lines[i][0:7], lines[i][7:10]
    return lines

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
    return int(row*8+col)


seats = get_all_seats()
ids = []
for seat in seats:
    seat_number = decode_seat(seat)
    ids.append(get_seat_id(seat_number[0], seat_number[1]))
ids.sort()
interval = range(int(ids[0]), int(ids[-1])+1)
for i in interval:
    if i not in ids:
        print(i)


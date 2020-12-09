def get_input():
    file = open('input.txt', 'r')
    text = file.read().split('\n')
    return [int(number) for number in text]


def number_is_sum_of_previous_two(number, previous_numbers):
    for i in range(len(previous_numbers)):
        for j in range(i+1, len(previous_numbers)):
            if previous_numbers[i]+previous_numbers[j] == number:
                return True
    return False


# part 1
def find_corrupt_number_and_its_index(preamble_len):
    numbers = get_input()
    for i in range(preamble_len, len(numbers)):
        if number_is_sum_of_previous_two(numbers[i], numbers[i-preamble_len: i]) is False:
            return numbers[i], i


# part 2
def find_numbers_which_sums_to_corrupt_number(corrupt_number, corrupt_number_index):
    numbers = get_input()
    for i in range(len(numbers)):
        high = numbers[i]
        low = numbers[i]
        res = numbers[i]
        for j in range(i + 1, len(numbers)):
            res += numbers[j]
            if numbers[j] > high:
                high = numbers[j]
            if numbers[j] < low:
                low = numbers[j]
            if res == corrupt_number:
                return high, low
            elif res > corrupt_number:
                break


#93668542 43725476 137394018
high, low = find_numbers_which_sums_to_corrupt_number(1038347917, 646)
print(high, low, high+low)
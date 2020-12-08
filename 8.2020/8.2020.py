import copy


def get_input():
    file = open('input.txt', 'r')
    text = file.read().split('\n')
    instructions = []
    for line in text:
        instructions.append([line.split()[0], int(line.split()[1]), 0])
    return instructions


# task 1
def get_accumulator_value(instructions):
    acc = 0
    current_line = 0
    while True:
        if instructions[current_line][2] == 1:
            return acc
        else:
            instructions[current_line][2] = 1
        if instructions[current_line][0] == 'acc':
            acc += instructions[current_line][1]
            current_line += 1
        elif instructions[current_line][0] == 'jmp':
            current_line += instructions[current_line][1]
        else:
            current_line += 1


def check_if_loop_terminates(instructions):
    current_line = 0
    while True:
        if current_line == len(instructions):
            return True
        elif instructions[current_line][2] == 1:
            return False
        else:
            instructions[current_line][2] = 1
        if instructions[current_line][0] == 'acc':
            current_line += 1
        elif instructions[current_line][0] == 'jmp':
            current_line += instructions[current_line][1]
        else:
            current_line += 1


def switch_instructions(instructions, line_number):
    if instructions[line_number][0] == 'jmp':
        instructions[line_number][0] = 'nop'
    elif instructions[line_number][0] == 'nop':
        instructions[line_number][0] = 'jmp'
    return instructions


def find_incorrupt_instruction():
    instructions = get_input()
    line_number = 0
    tmp_instructions = copy.deepcopy(instructions)
    while check_if_loop_terminates(tmp_instructions) is False:
        tmp_instructions = copy.deepcopy(instructions)
        tmp_instructions = switch_instructions(tmp_instructions, line_number)
        line_number += 1
    return unvisit_all_instructions(tmp_instructions), line_number


def unvisit_all_instructions(instructions):
    for instruction in instructions:
        instruction[2] = 0
    return instructions


def get_accumulator_value_for_incorrupt_instructions(instructions):
    acc = 0
    current_line = 0
    while current_line != len(instructions):
        if instructions[current_line][0] == 'acc':
            acc += instructions[current_line][1]
            current_line += 1
        elif instructions[current_line][0] == 'jmp':
            current_line += instructions[current_line][1]
        else:
            current_line += 1
    return acc


proper_instructions, line_number = find_incorrupt_instruction()
print(proper_instructions)
print(line_number)
print(get_accumulator_value_for_incorrupt_instructions(proper_instructions))




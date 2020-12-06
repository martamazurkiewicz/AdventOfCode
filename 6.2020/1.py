file = open('input.txt', 'r')
text = file.read().split('\n')
all_answers = []
answers = set()
for i in range(len(text)):
    answer = text[i]
    if answer == '':
        all_answers.append(answers)
        answers = set()
    else:
        for char in answer:
            answers.add(char)
all_answers.append(answers)
sum_of_yes = 0
for answers in all_answers:
    sum_of_yes += len(answers)
print(sum_of_yes)
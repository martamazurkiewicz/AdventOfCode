def get_common_elements_list(answers):
    common_letters = []
    whole_answer = ""
    for answer in answers:
        whole_answer += answer
    answers.sort(key=lambda elem: len(elem))
    for char in answers[0]:
        if whole_answer.count(char) == len(answers):
            common_letters.append(char)
    return common_letters


file = open('input.txt', 'r')
text = file.read().split('\n')
all_answers = []
answers = []
for i in range(len(text)):
    answer = text[i]
    if answer == '':
        all_answers.append(get_common_elements_list(answers))
        answers = []
    else:
        answers.append(answer)
all_answers.append(get_common_elements_list(answers))
print(all_answers)
sum_of_common_elements = 0
for answers in all_answers:
    sum_of_common_elements += len(answers)
print(sum_of_common_elements)

def question_1a(elf_list):
    # Find the elf carrying the most calories
    current_elf = 0
    calorie_value = 0
    maximum_calories = 0
    all_dict = {}

    for i in elf_list:
        if i != '':
            calorie_value += int(i)
        else:
            current_elf += 1
            all_dict.update({current_elf: calorie_value})

            if calorie_value > maximum_calories:
                maximum_calories = calorie_value

            calorie_value = 0

    print('The elf with the most calories have a whopping {} kcal'.format(maximum_calories))


def question_1b(elf_list):

    # Find the top 3 elf's carrying the most calories
    calorie_value = 0
    top_list = [0, 0, 0]

    for i in elf_list:
        if i != '':
            calorie_value += int(i)
        else:
            if calorie_value > top_list[2] and calorie_value > top_list[1] and calorie_value > top_list[0]:
                top_list.insert(0, calorie_value)
            elif top_list[2] < calorie_value < top_list[0] and calorie_value > top_list[1]:
                top_list.insert(1, calorie_value)
            elif top_list[2] < calorie_value < top_list[1] and calorie_value < top_list[0]:
                top_list.insert(2, calorie_value)

            calorie_value = 0

    print('The combined calories for the top 3 elf\'s is a whopping {} kcal'.format(sum(top_list[0:3])))


if __name__ == '__main__':

    try:
        with open('../instructions/Elfs.csv', 'r') as fp:
            calories = []
            for cal in fp.readlines():
                calories.append(cal.strip('\n'))

    except FileNotFoundError as e:
        print(e)

    question_1a(calories)
    question_1b(calories)



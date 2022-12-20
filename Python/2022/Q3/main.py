import string


def _alphabet_to_numeric_value(letter):
	alpha_letters = list(' ') + list(string.ascii_lowercase) + list(string.ascii_uppercase)  	# 1:1 mapping alpha

	return alpha_letters.index(letter)


def _common_compartment_content(comp1, comp2, comp3=None):
	common_dict = {}
	for letter in comp1:
		if comp2.__contains__(letter) and comp3 is None:
			common_dict.update({letter: [comp1.index(letter), comp2.index(letter)]})

		elif comp3 is not None and comp2.__contains__(letter) and comp3.__contains__(letter):
			common_dict.update({letter: [comp1.index(letter), comp2.index(letter), comp3.index(letter)]})

	if len(common_dict) > 1:
		ValueError('More than one common item in compartments')

	return list(common_dict.keys())[0]


def question_3a(rucksacks):
	priority = 0

	for rucksack in rucksacks:
		content_length = len(rucksack)
		compartment_1 = rucksack[0: int(content_length/2)]
		compartment_2 = rucksack[int(content_length/2): len(rucksack)]
		priority += _alphabet_to_numeric_value(_common_compartment_content(compartment_1, compartment_2))

	print('The combined priorities are {}'.format(priority))


def question_3b(rucksacks):
	priority = 0

	for i in range(0, len(rucksacks), 3):
		elf_1 = rucksacks[i]
		elf_2 = rucksacks[i+1]
		elf_3 = rucksacks[i+2]
		priority += _alphabet_to_numeric_value(_common_compartment_content(elf_1, elf_2, elf_3))

	print('The combined priorities are {}'.format(priority))


if __name__ == '__main__':
	all_sacks = []
	try:
		with open('../instructions/rugsack.csv') as fp:
			for sack in fp.readlines():
				all_sacks.append(sack.strip('\n'))
	except FileNotFoundError as e:
		FileNotFoundError(e)

	question_3a(all_sacks)
	question_3b(all_sacks)

def _get_subset_range(pair):
	subset1, subset2 = pair.split(',')
	subset1_range = range(int(subset1.split('-')[0]), int(subset1.split('-')[1]) + 1)
	subset2_range = range(int(subset2.split('-')[0]), int(subset2.split('-')[1]) + 1)

	if len(subset1_range) > len(subset2_range):
		return subset1_range, subset2_range
	else:
		return subset2_range, subset1_range


def _count_including_subsets(pair):
	bool_return = 0
	subset1_range, subset2_range = _get_subset_range(pair)

	if subset2_range[0] in subset1_range and subset2_range[-1] in subset1_range:
		bool_return = 1

	return bool_return


def _count_overlapping_subsets(pair):
	bool_return = 0
	subset1, subset2 = _get_subset_range(pair)

	for value in subset2:
		if value in subset1:
			bool_return = 1

	return bool_return


def question_4(assignment_list):
	count_a = 0
	count_b = 0
	for pair in assignment_list:
		count_a += _count_including_subsets(pair)
		count_b += _count_overlapping_subsets(pair)

	print('{} number of times the assignment pairs fully contain the other one'.format(count_a))
	print('{} number of times the assignment pairs overlap'.format(count_b))


if __name__ == '__main__':
	all_assignments = []

	try:
		with open('../instructions/assignments.csv') as fp:
			for sack in fp.readlines():
				all_assignments.append(sack.strip('\n'))
	except FileNotFoundError as e:
		FileNotFoundError(e)

	question_4(all_assignments)

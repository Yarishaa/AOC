
def get_depth_values(filename):
    datapoint = []

    try:
        with open(filename) as fp:
            for val in fp.readlines():
                datapoint.append(int(val.strip('\n')))

    except FileNotFoundError():
        raise FileNotFoundError('Cannot find specified file!')

    finally:
        return datapoint


def question_1a(measurement_data):
    increased_counter = 0
    for idx in range((len(measurement_data)-1)):
        if measurement_data[idx + 1] > measurement_data[idx]:
            increased_counter += 1

    print("Ans Q1a:: The depth increased {} times".format(increased_counter))


def question_1b(measurement_data):
    increased_counter = 0
    for idx in range((len(measurement_data) - 3)):
        sum1 = measurement_data[idx] + measurement_data[idx + 1] + measurement_data[idx + 2]
        sum2 = measurement_data[idx + 1] + measurement_data[idx + 2] + measurement_data[idx + 3]

        if sum2 > sum1:
            increased_counter += 1

    print("Ans Q1b:: The number of times the following sum increased is {}".format(increased_counter))


if __name__ == '__main__':
    file = '../instructions/oceanDepth'
    data = get_depth_values(file)

    # solve for question 1a
    question_1a(data)

    # solve for question 1b
    question_1b(data)

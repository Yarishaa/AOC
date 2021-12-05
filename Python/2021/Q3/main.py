def render_data(datafile):
    diagnostics = []
    try:
        with open(datafile) as fp:
            for binary_set in fp.readlines():
                diagnostics.append(binary_set.strip('\n'))

    except FileNotFoundError:
        raise FileNotFoundError('Cannot find specified file!')

    finally:
        return diagnostics


def get_gamma_value(data, index):
    if index is None:
        raise ValueError('Specify which index')

    gamma_counter = 0
    epsilon_counter = 0
    for i in data:
        if i[index] == '1':
            gamma_counter += 1
        else:
            epsilon_counter += 1

    if gamma_counter > epsilon_counter:
        return '1', '0'
    elif gamma_counter < epsilon_counter:
        return '0', '1'
    else:
        return '1', '1'


def callback_function(data, index, common):
    return_data = []

    gamma, epsilon = get_gamma_value(data, index)
    if gamma > epsilon:
        most_common = '1'
    elif gamma == epsilon:
        most_common = common
    else:
        most_common = '0'

    if common == '0' and gamma != epsilon:
        most_common = str(int(not int(most_common)))

    for data_point in data:
        if data_point[index] == most_common:
            return_data.append(data_point)

    return return_data


def question_3a(data):

    gamma = ""
    epsilon = ""

    for idx in range(12):
        g, e = get_gamma_value(data, idx)
        gamma += g
        epsilon += e

    # convert to decimal
    gamma_dec = int(gamma, 2)
    epsilon_dec = int(epsilon, 2)

    power_consumption = gamma_dec * epsilon_dec
    print('Ans Q3a:: Total power consumption from diagnostic data is: {}'.format(power_consumption))


def question_3b(data):
    oxygen_generator_rating = "1"
    co_scrubber_rating = "0"
    oxygen_data = data
    scrubbing_data = data
    index_ox = 0
    index_co2 = 0
    while len(oxygen_data) > 1:
        oxygen_data = callback_function(oxygen_data, index_ox, oxygen_generator_rating)
        index_ox += 1
    while len(scrubbing_data) > 1:
        scrubbing_data = callback_function(scrubbing_data, index_co2, co_scrubber_rating)
        index_co2 += 1

    # convert to decimal
    oxygen = int(oxygen_data[0], 2)
    carbon = int(scrubbing_data[0], 2)

    life_support = oxygen * carbon
    print('Ans Q3b:: The life support rating from diagnostic data is: {}'.format(life_support))


if __name__ == '__main__':
    filename = "../instructions/diagnosticBinary"
    input_data = render_data(filename)

    # solve for question 2a
    question_3a(input_data)

    # solve for question 2b
    question_3b(input_data)

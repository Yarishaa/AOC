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


def question_4a(data):

    print('Ans Q3a:: Total power consumption from diagnostic data is: {}')


def question_4b(data):

    print('Ans Q3b:: The life support rating from diagnostic data is: {}')


if __name__ == '__main__':
    filename = "../instructions/diagnosticBinary"
    input_data = render_data(filename)


def render_data(datafile):
    direction = []
    try:
        with open(datafile) as fp:
            for instruction in fp.readlines():
                data = instruction.strip('\n').split(' ')
                coordinate = [data[0], int(data[1])]
                direction.append(coordinate)
    except FileNotFoundError:
        raise FileNotFoundError('Cannot find specified file!')

    finally:
        return direction


def question_2a(datafile):
    position = [0, 0]   # [horizontal, vertical]
    for command in datafile:
        direction = command[0]
        unit_value = command[1]

        if direction == 'forward':
            position[0] += unit_value
        if direction == 'up':
            position[1] -= unit_value
        if direction == 'down':
            position[1] += unit_value

    answer = position[0] * position[1]
    print('Ans Q2a:: Multiplied, the answer is {}'.format(answer))


def question_2b(datafile):
    position = [0, 0, 0]    # [horizontal, depth, aim]
    for command in datafile:
        direction = command[0]
        unit_value = command[1]

        if direction == 'forward':
            position[0] += unit_value
            position[1] += (unit_value * position[2])    # multiplies with aim
        if direction == 'up':
            position[2] -= unit_value
        if direction == 'down':
            position[2] += unit_value

    answer = position[0] * position[1]
    print('Ans Q2b:: Multiplied, the answer is {}'.format(answer))


if __name__ == '__main__':
    filename = '../instructions/direction_coordinates'
    directions = render_data(filename)

    # solve for question 2a
    question_2a(directions)

    # solve for question 2b
    question_2b(directions)
